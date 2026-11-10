"""Safety node — defence-in-depth guardrail (C1 + C6, inspire team 005).

Pattern: guardrail nằm ở CẢ prompt LẪN code. Node này check DANGER_KEYWORDS
trước khi query đi vào LLM. Nếu trigger → short-circuit trả cảnh báo ngay, KHÔNG
qua LLM (tránh LLM "quên" safeguard khi bị jailbreak).

Đây là lớp CODE; prompt (safeguards.md) là lớp PROMPT. Hai lớp độc lập.
"""

from __future__ import annotations

import re

from src.agents.state import AgentState

# Từ khoá nguy hiểm — short-circuit bypass LLM. Inspire team 005 DANGER_KEYWORDS.
# Tuỳ domain, team bổ sung (y tế, pháp lý, tự hại, ...).
DANGER_KEYWORDS: tuple[str, ...] = (
    "tự hại",
    "muốn chết",
    "ra máu",
    "đau bụng dữ dội",
    "khó thở",
    "vỡ ối",
    "giết",
    "bomba",
    "suicide",
)

# Ranh giới từ bên trái: từ khoá phải bắt đầu một từ, nên không khớp bên trong từ khác.
# Vẫn bắt được các dạng biến đổi của từ (khớp theo tiền tố).
_DANGER_PATTERN = re.compile(r"\b(?:" + "|".join(re.escape(kw) for kw in DANGER_KEYWORDS) + r")")

DANGER_RESPONSE = (
    "⚠️ Cảnh báo an toàn: tôi phát hiện từ khoá nhạy cảm trong câu hỏi của bạn. "
    "Nếu đây là tình huống khẩn cấp, hãy liên hệ ngay cơ sở y tế / đường dây nóng "
    "phù hợp. Tôi không thể tư vấn khẩn cấp."
)


async def safety_node(state: AgentState) -> dict:
    """Check danger keywords. Nếu trigger → bypass LLM, trả cảnh báo."""
    query = (state.get("query") or "").lower()
    hit = _DANGER_PATTERN.search(query) is not None
    if hit:
        return {
            "safety_flag": "danger",
            "bypass": True,
            "response": DANGER_RESPONSE,
            "analysis": "blocked_by_safety_node",
        }
    return {"safety_flag": "ok", "bypass": False}
