# PROJECT_CONTEXT.md (C5)

> Inspire team 001 (Memio) — Quick Rehydrate + Current Invariants.
> Đây là file agent đọc ĐẦU TIÊN khi resume session. Giữ < 60 giây để đọc.

## 0. Quick Rehydrate (≤ 60s)

- **Project**: [TÊN PRODUCT CỦA TEAM] — [1 câu mô tả].
- **Stack**: Python 3.12 / FastAPI / LangGraph / LangChain / [frontend?].
- **Dev**: `uvicorn src.main:app --reload` (backend), `[lệnh frontend]`.
- **Test**: `make test`. **Eval**: `python eval/run_eval.py`.
- **Env**: copy `.env.example` → `.env`, thêm `OPENAI_API_KEY` (optional — mock-first).

## 0.1 Current Invariants (để không drift)

- **Source of truth kỹ thuật**: code trong `src/`. File `.md` chỉ tóm tắt — khi mâu thuẫn,
  **CODE WINS**. Inspire team 011 source-of-truth rule.
- **Agent flow**: `src/agents/graph.py` (safety → retrieve → synthesize → validate).
- **Prompts**: `prompts/*.md` (external, `{{placeholder}}`).
- **Safety**: DANGER_KEYWORDS ở `nodes/safety_node.py` (cập nhật theo domain app).

## 0.2 Known Ambiguities / Mismatches (inspire team 011)

Liệt kê chỗ doc-vs-code lệch để agent không tin doc stale:
- [team điền khi phát hiện mismatch, vd: "PRD nói dùng Gemini nhưng code đang OpenAI"]

## 1. Quyết định kỹ thuật (link ADR)

Xem `WORKLOG.md` mục ADR. Mỗi quyết định lớn ghi theo format:
`[ADR-XXX] Context / Options / Decision / Consequences` (inspire team 010).

## 2. Cập nhật file này

Khi đổi stack/invariant → UPDATE FILE NÀY TRƯỚC, rồi mới sửa code. File này là contract
giữa các session agent.
