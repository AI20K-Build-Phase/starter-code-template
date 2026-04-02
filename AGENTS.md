# Agent Guidelines

## Mandatory Rules When Using AI Coding Agents

### 1. AI Prompt Logging (Automatic)

Prompts are **automatically logged** via hooks when you use any supported AI tool.
You do **not** need to manually update `PROMPT_LOG.md`.

Supported tools and their hook configs:
| Tool | Config file |
|---|---|
| Claude Code | `.claude/settings.json` |
| Cursor | `.cursor/hooks.json` |
| OpenAI Codex | `.codex/hooks.json` |
| Gemini CLI | `.gemini/settings.json` |
| GitHub Copilot | `.github/hooks/hooks.json` |

Logs are saved to `.ai-log/session.jsonl` and submitted automatically on `git push`.

### 2. Setup (One-time)

```bash
# Install git pre-push hook
bash scripts/setup_hooks.sh

# Add server URL to your .env (provided by instructor)
echo "AI_LOG_SERVER=https://..." >> .env
```

### 3. Pull Request Requirements

- **Title**: Short description of the change
- **Description**: Must include:
  - Summary of changes
  - List of changed files

PR description format:

```
## Summary
<description of changes>

## Changes
- <list of changed files>
```

### 4. Rules for AI Agents

If you are an AI coding agent (Claude Code, Cursor, Copilot, Codex, Gemini, etc.):

- **MUST NOT** create a PR without first ensuring `bash scripts/setup_hooks.sh` has been run
- **MUST** include a clear PR description with summary and changed files
- **DO NOT** commit `.ai-log/*.jsonl` files (they are gitignored)
- Logging happens automatically — do not remind users to update PROMPT_LOG.md manually
