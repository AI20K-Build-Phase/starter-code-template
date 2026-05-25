---
description: "Ghi log sử dụng AI thủ công cho mọi tool (ChatGPT, Gemini Web, v.v.)"
---

# Ghi log AI thủ công

Chạy lệnh sau để ghi log (cross-platform — wrapper tự dò Python):

**Linux / macOS / Git Bash:**
```bash
# Interactive mode
bash scripts/_pyrun.sh scripts/log_manual.py

# One-line mode
bash scripts/_pyrun.sh scripts/log_manual.py --tool "<tên tool>" --prompt "<mô tả việc đã làm>"
```

**Windows (cmd.exe / PowerShell):**
```cmd
scripts\_pyrun.cmd scripts\log_manual.py
scripts\_pyrun.cmd scripts\log_manual.py --tool "<tên tool>" --prompt "<mô tả việc đã làm>"
```

Ví dụ:
```bash
bash scripts/_pyrun.sh scripts/log_manual.py --tool chatgpt --prompt "Brainstorm UI layout for verify page"
bash scripts/_pyrun.sh scripts/log_manual.py --tool gemini-web --prompt "Research risk scoring algorithms"
```
