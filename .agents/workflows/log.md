---
description: "Ghi log sử dụng AI thủ công cho mọi tool (ChatGPT, Gemini Web, v.v.)"
---

# Ghi log AI thủ công

Chạy lệnh sau để ghi log:

// turbo
1. Chạy script ghi log tương tác (interactive mode):
```bash
python scripts/log_manual.py
```

Hoặc nếu muốn ghi nhanh (one-line):
```bash
python scripts/log_manual.py --tool "<tên tool>" --prompt "<mô tả việc đã làm>"
```

Ví dụ:
```bash
python scripts/log_manual.py --tool chatgpt --prompt "Brainstorm UI layout for verify page"
python scripts/log_manual.py --tool gemini-web --prompt "Research risk scoring algorithms"
```
