---
description: "Automatically log every AI agent interaction to .ai-log/session.jsonl for grading compliance"
activation: always-on
---

# AI Usage Logging Hook

## Bắt buộc — Ghi log sau MỖI task

Sau khi hoàn thành BẤT KỲ task nào (sửa file, chạy lệnh, trả lời câu hỏi, v.v.), bạn **PHẢI** chạy lệnh sau để ghi log vào `.ai-log/session.jsonl`:

```bash
python scripts/log_antigravity.py "<tóm tắt ngắn gọn việc đã làm>" "<model đang dùng>"
```

### Quy tắc:
1. **Luôn luôn ghi log** — không có ngoại lệ, kể cả task nhỏ
2. **Tóm tắt ngắn gọn** — viết bằng tiếng Việt hoặc tiếng Anh, tối đa 200 ký tự
3. **Ghi đúng model** — ví dụ: `claude-opus-4.6`, `gemini-3.1-pro`, hoặc tên model đang dùng
4. **Dùng lệnh `python` hoặc `python3`** — tùy theo command nào hoạt động trên môi trường máy của bạn.
5. **Chạy từ thư mục gốc repo** `A20-App-131`

### Ví dụ:
```bash
python scripts/log_antigravity.py "Updated WORKLOG.md with ADR-2 technical decision" "claude-opus-4.6"
python scripts/log_antigravity.py "Fixed pre-push hook Python detection for Windows" "gemini-3.1-pro"
python scripts/log_antigravity.py "Created verify flow in src/agent.py" "claude-opus-4.6"
```

### Lưu ý:
- File log `.ai-log/session.jsonl` đã được gitignore — KHÔNG commit file này
- Log sẽ được tự động submit lên server grading khi `git push` (qua git pre-push hook)
- Nếu script `log_antigravity.py` không tồn tại hoặc lỗi, hãy thông báo cho user
