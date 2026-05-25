#!/usr/bin/env python3
"""
Antigravity IDE log scanner — extracts AI usage logs from Antigravity's
conversation history stored in ~/.gemini/antigravity/brain/.

Antigravity does NOT have a hook API. This script bridges the gap by scanning
Antigravity's local brain data and extracting log entries.

Usage:
  python scripts/log_antigravity.py --auto              # Auto-scan recent sessions
  python scripts/log_antigravity.py --hours 72           # Scan last 72 hours
  python scripts/log_antigravity.py --conversation-id <id>  # Scan specific conversation
  python scripts/log_antigravity.py --all                # Scan all unlogged conversations

How it works:
  1. Finds Antigravity brain directory (~/.gemini/antigravity/brain/)
  2. For each conversation dir, checks multiple strategies to match this repo
  3. Extracts user prompts from .system_generated/messages/ JSON files
  4. Writes entries to .ai-log/session.jsonl
"""
import json
import os
import sys
import subprocess
import argparse
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Fix Windows console encoding
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

VN_TZ = timezone(timedelta(hours=7))

BRAIN_PATHS = {
    "win32": Path.home() / ".gemini" / "antigravity" / "brain",
    "darwin": Path.home() / ".gemini" / "antigravity" / "brain",
    "linux": Path.home() / ".gemini" / "antigravity" / "brain",
}


def git(cmd):
    try:
        return subprocess.check_output(
            cmd.split(), shell=False, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return ""


def get_brain_dir() -> Path | None:
    env_path = os.environ.get("ANTIGRAVITY_BRAIN_DIR")
    if env_path:
        p = Path(env_path)
        if p.exists():
            return p
    p = BRAIN_PATHS.get(sys.platform, BRAIN_PATHS["linux"])
    return p if p.exists() else None


def get_repo_identifiers() -> list[str]:
    """Get identifiers to match conversations to this repo."""
    identifiers = []
    remote = git("git remote get-url origin")
    if remote:
        repo_name = remote.split("/")[-1].replace(".git", "")
        identifiers.append(repo_name)
        parts = remote.rstrip("/").split("/")
        if len(parts) >= 2:
            identifiers.append(f"{parts[-2]}/{parts[-1]}".replace(".git", ""))
    cwd = Path.cwd()
    identifiers.append(cwd.name)
    identifiers.append(str(cwd).replace("\\", "/").lower())
    identifiers.append(str(cwd).lower())
    return [i for i in identifiers if i]


def get_logged_entry_ids(log_file: Path) -> set[str]:
    """Read already-logged entry IDs from session.jsonl."""
    logged = set()
    if not log_file.exists():
        return logged
    with open(log_file, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                if entry.get("tool") == "antigravity":
                    eid = entry.get("entry_id", "")
                    if eid:
                        logged.add(eid)
                    sid = entry.get("session_id", "")
                    if sid:
                        logged.add(sid)
            except json.JSONDecodeError:
                pass
    return logged


def _text_contains_repo(text: str, repo_ids: list[str]) -> bool:
    """Check if text contains any repo identifier."""
    text_lower = text.lower()
    for rid in repo_ids:
        if rid.lower() in text_lower:
            return True
    return False


def scan_conversation(conv_dir: Path, repo_ids: list[str]) -> dict | None:
    """
    Scan a conversation directory to determine if it's related to this repo.
    Uses multiple strategies with increasing search depth.
    """
    conv_id = conv_dir.name
    if not re.match(r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$", conv_id):
        return None

    # Strategy 1: Check metadata.json files (small, fast)
    for meta_file in conv_dir.glob("*.metadata.json"):
        try:
            content = meta_file.read_text(encoding="utf-8", errors="ignore")
            if _text_contains_repo(content, repo_ids):
                return _extract_conversation_data(conv_dir, conv_id)
        except Exception:
            pass

    # Strategy 2: Check artifact markdown files (full content, not just head)
    for artifact in conv_dir.glob("*.md"):
        if artifact.name.endswith(".metadata.json"):
            continue
        try:
            content = artifact.read_text(encoding="utf-8", errors="ignore")
            if _text_contains_repo(content, repo_ids):
                return _extract_conversation_data(conv_dir, conv_id)
        except Exception:
            pass

    # Strategy 3: Check step content files for workspace references
    steps_dir = conv_dir / ".system_generated" / "steps"
    if steps_dir.exists():
        try:
            for step_dir in steps_dir.iterdir():
                content_file = step_dir / "content.md"
                if content_file.exists():
                    content = content_file.read_text(encoding="utf-8", errors="ignore")[:20000]
                    if _text_contains_repo(content, repo_ids):
                        return _extract_conversation_data(conv_dir, conv_id)
        except Exception:
            pass

    # Strategy 4: Check overview.txt logs
    overview = conv_dir / ".system_generated" / "logs" / "overview.txt"
    if overview.exists():
        try:
            content = overview.read_text(encoding="utf-8", errors="ignore")[:50000]
            if _text_contains_repo(content, repo_ids):
                return _extract_conversation_data(conv_dir, conv_id)
        except Exception:
            pass

    return None


def _extract_conversation_data(conv_dir: Path, conv_id: str) -> dict:
    """Extract metadata and prompts from a conversation directory."""
    data = {
        "conversation_id": conv_id,
        "conv_dir": conv_dir,
        "prompts": [],
        "model": "gemini",
    }

    # Get timestamp from directory modification time
    try:
        mtime = conv_dir.stat().st_mtime
        data["timestamp"] = datetime.fromtimestamp(mtime, tz=VN_TZ).isoformat()
    except Exception:
        data["timestamp"] = datetime.now(VN_TZ).isoformat()

    # Extract user prompts from messages/ directory
    msgs_dir = conv_dir / ".system_generated" / "messages"
    if msgs_dir.exists():
        try:
            for msg_file in sorted(msgs_dir.iterdir()):
                if not msg_file.name.endswith(".json"):
                    continue
                try:
                    msg = json.loads(msg_file.read_text(encoding="utf-8", errors="ignore"))
                    sender = msg.get("sender", "")
                    # Skip system messages
                    if sender == "system":
                        continue
                    content = msg.get("content", "").strip()
                    ts = msg.get("timestamp", "")
                    if content and len(content) > 3:
                        data["prompts"].append({
                            "text": content[:1000],
                            "timestamp": ts,
                        })
                except (json.JSONDecodeError, KeyError):
                    pass
        except Exception:
            pass

    # If no messages found, try extracting task summary from artifacts
    if not data["prompts"]:
        for artifact_name in ["task.md", "walkthrough.md", "implementation_plan.md"]:
            artifact = conv_dir / artifact_name
            if artifact.exists():
                try:
                    content = artifact.read_text(encoding="utf-8", errors="ignore")
                    for line in content.split("\n"):
                        line = line.strip()
                        if line.startswith("# "):
                            data["prompts"].append({
                                "text": line.replace("# ", "").strip()[:200],
                                "timestamp": data["timestamp"],
                            })
                            break
                except Exception:
                    pass

    # Fallback — at least one entry
    if not data["prompts"]:
        data["prompts"].append({
            "text": f"Antigravity session {conv_id[:8]}",
            "timestamp": data["timestamp"],
        })

    return data


def create_log_entries(conv_data: dict, logged_ids: set[str]) -> list[dict]:
    """Create standardized log entries — one per user prompt."""
    student = git("git config user.email")
    if not student:
        student = os.environ.get("USERNAME", os.environ.get("USER", "unknown"))

    repo = git("git remote get-url origin").split("/")[-1].replace(".git", "")
    branch = git("git rev-parse --abbrev-ref HEAD")
    commit = git("git rev-parse --short HEAD")

    conv_id = conv_data["conversation_id"]
    entries = []

    for i, prompt in enumerate(conv_data["prompts"]):
        entry_id = f"antigravity-{conv_id}-{i:03d}"
        if entry_id in logged_ids:
            continue

        ts = prompt.get("timestamp", conv_data.get("timestamp", ""))
        # Convert UTC timestamp to VN timezone if needed
        if ts and ts.endswith("Z"):
            try:
                dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                ts = dt.astimezone(VN_TZ).isoformat()
            except Exception:
                pass

        entry = {
            "ts": ts or datetime.now(VN_TZ).isoformat(),
            "tool": "antigravity",
            "event": "UserPrompt",
            "entry_id": entry_id,
            "session_id": conv_id,
            "model": conv_data.get("model", "gemini"),
            "repo": repo or Path.cwd().name,
            "branch": branch,
            "commit": commit,
            "student": student,
            "prompt": prompt["text"],
            "response_summary": "",
        }
        entries.append(entry)

    return entries


def main():
    parser = argparse.ArgumentParser(
        description="Antigravity IDE log scanner — extract AI usage from conversation history"
    )
    parser.add_argument("--auto", action="store_true", help="Auto-scan recent sessions (default)")
    parser.add_argument("--hours", type=int, default=24, help="Hours to look back (default: 24)")
    parser.add_argument("--conversation-id", help="Scan a specific conversation by ID")
    parser.add_argument("--all", action="store_true", help="Scan all conversations")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be logged")

    # Legacy support: positional args for manual logging
    parser.add_argument("summary", nargs="?", help=argparse.SUPPRESS)
    parser.add_argument("model", nargs="?", help=argparse.SUPPRESS)

    args = parser.parse_args()

    # Legacy mode: log_antigravity.py "summary" "model"
    if args.summary and not args.auto and not args.conversation_id and not args.all:
        _legacy_log(args.summary, args.model or "antigravity")
        return

    if not args.auto and not args.conversation_id and not args.all:
        args.auto = True

    brain_dir = get_brain_dir()
    if not brain_dir:
        print("[antigravity-log] No brain directory found.", file=sys.stderr)
        sys.exit(0)

    log_dir = Path(os.environ.get("AI_LOG_DIR", ".ai-log"))
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "session.jsonl"

    logged_ids = get_logged_entry_ids(log_file)
    repo_ids = get_repo_identifiers()
    if not repo_ids:
        print("[antigravity-log] Cannot determine repo identity.", file=sys.stderr)
        sys.exit(0)

    cutoff = None
    if args.auto or args.hours:
        cutoff = datetime.now(tz=VN_TZ) - timedelta(hours=args.hours)

    all_entries = []

    if args.conversation_id:
        conv_dir = brain_dir / args.conversation_id
        if not conv_dir.exists():
            print(f"[antigravity-log] Conversation not found: {args.conversation_id}", file=sys.stderr)
            sys.exit(1)
        conv_data = _extract_conversation_data(conv_dir, args.conversation_id)
        all_entries.extend(create_log_entries(conv_data, logged_ids))
    else:
        try:
            conv_dirs = [d for d in brain_dir.iterdir() if d.is_dir()]
        except PermissionError:
            sys.exit(0)

        for conv_dir in conv_dirs:
            conv_id = conv_dir.name
            if not re.match(r"^[a-f0-9-]{36}$", conv_id):
                continue

            if cutoff and not args.all:
                try:
                    mtime = datetime.fromtimestamp(conv_dir.stat().st_mtime, tz=VN_TZ)
                    if mtime < cutoff:
                        continue
                except Exception:
                    continue

            conv_data = scan_conversation(conv_dir, repo_ids)
            if conv_data:
                entries = create_log_entries(conv_data, logged_ids)
                all_entries.extend(entries)

    if not all_entries:
        print("[antigravity-log] No new Antigravity sessions found for this repo.", file=sys.stderr)
        sys.exit(0)

    if args.dry_run:
        print(f"\n[antigravity-log] DRY RUN — Would log {len(all_entries)} entries:\n")
        for entry in all_entries:
            print(f"  [{entry['ts'][:19]}] {entry['prompt'][:100]}")
        sys.exit(0)

    with open(log_file, "a", encoding="utf-8") as f:
        for entry in all_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"[antigravity-log] Logged {len(all_entries)} Antigravity prompt(s).", file=sys.stderr)
    for entry in all_entries:
        print(f"  [{entry['ts'][:19]}] {entry['prompt'][:80]}", file=sys.stderr)


def _legacy_log(summary: str, model: str):
    """Backward-compatible manual logging mode."""
    ts = datetime.now(VN_TZ).isoformat()
    entry = {
        "ts": ts,
        "tool": "antigravity",
        "event": "TaskComplete",
        "entry_id": f"antigravity-{datetime.now(VN_TZ).strftime('%Y%m%d-%H%M%S')}",
        "model": model,
        "repo": git("git remote get-url origin").split("/")[-1].replace(".git", ""),
        "branch": git("git rev-parse --abbrev-ref HEAD"),
        "commit": git("git rev-parse --short HEAD"),
        "student": git("git config user.email") or os.environ.get("USERNAME", os.environ.get("USER", "unknown")),
        "prompt": summary[:1000],
        "response_summary": f"[Antigravity] {summary[:500]}",
    }
    log_dir = Path(os.environ.get("AI_LOG_DIR", ".ai-log"))
    log_dir.mkdir(exist_ok=True)
    with open(log_dir / "session.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"[antigravity-log] Logged: {summary[:80]}...", file=sys.stderr)


if __name__ == "__main__":
    main()
