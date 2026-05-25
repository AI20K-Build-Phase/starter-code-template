---
description: "Automatically log every AI agent interaction to .ai-log/session.jsonl for grading compliance"
activation: always-on
---

# AI Usage Logging Hook

## Bắt buộc — Ghi log sau MỖI task

Sau khi hoàn thành BẤT KỲ task nào (sửa file, chạy lệnh, trả lời câu hỏi, v.v.), bạn **PHẢI** chạy lệnh sau để ghi log vào `.ai-log/session.jsonl`:

**Linux / macOS / Git Bash:**
```bash
bash scripts/_pyrun.sh scripts/log_antigravity.py "<tóm tắt ngắn gọn việc đã làm>" "<model đang dùng>"
```

**Windows (cmd.exe / PowerShell):**
```cmd
scripts\_pyrun.cmd scripts\log_antigravity.py "<tóm tắt ngắn gọn việc đã làm>" "<model đang dùng>"
```

> `_pyrun` là wrapper tự dò `python3` / `python` / `py -3` — không cần lo Python alias.

### Quy tắc:
1. **Luôn luôn ghi log** — không có ngoại lệ, kể cả task nhỏ
2. **Tóm tắt ngắn gọn** — tiếng Việt hoặc tiếng Anh, tối đa 200 ký tự
3. **Ghi đúng model** — ví dụ: `claude-opus-4.6`, `gemini-3.1-pro`
4. **Chạy từ thư mục gốc repo**

### Ví dụ:
```bash
bash scripts/_pyrun.sh scripts/log_antigravity.py "Updated WORKLOG.md with ADR-2 technical decision" "claude-opus-4.6"
bash scripts/_pyrun.sh scripts/log_antigravity.py "Fixed pre-push hook Python detection for Windows" "gemini-3.1-pro"
```

### Lưu ý:
- File log `.ai-log/session.jsonl` đã được gitignore — KHÔNG commit
- Log sẽ tự động submit lên grading server khi `git push` (qua git pre-push hook)
- Nếu script lỗi, thông báo cho user
