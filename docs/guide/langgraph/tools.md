---
title: "Agent Tools"
description: "Tạo tools cho LangGraph agent"
weight: 3
---

## Tool Definition

```python
from langchain_core.tools import tool

@tool
def search_knowledge(query: str) -> str:
    """Tìm kiếm thông tin trong knowledge base.

    Args:
        query: Câu hỏi cần tìm kiếm

    Returns:
        Kết quả tìm kiếm dạng text
    """
    results = vector_store.similarity_search(query, k=3)
    return "\n".join([r.page_content for r in results])
```

## Nguyên tắc

1. **Luôn có docstring** — Agent dùng docstring để quyết định khi nào gọi tool
2. **Type hints cho tất cả params** — Giúp agent truyền đúng kiểu data
3. **Return string** — Agent dễ parse kết quả
4. **Error handling bên trong tool** — Không throw, return error message

## Tool Types

### Search Tool (RAG)

```python
@tool
def search_documents(query: str) -> str:
    """Tìm kiếm tài liệu liên quan."""
    docs = vector_store.similarity_search(query, k=5)
    if not docs:
        return "Không tìm thấy tài liệu liên quan."
    return "\n---\n".join([d.page_content for d in docs])
```

### API Call Tool

```python
@tool
def call_external_api(endpoint: str, params: dict) -> str:
    """Gọi API ngoài."""
    try:
        response = httpx.post(endpoint, json=params)
        return response.text
    except Exception as e:
        return f"API error: {e}"
```

### Calculator Tool

```python
import ast
import operator

from langchain_core.tools import tool

# Whitelist toán tử. Không bao giờ truyền output của LLM vào eval(): nó có thể chạy code tuỳ ý.
_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

def _eval_node(node: ast.AST) -> float:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval_node(node.left), _eval_node(node.right))
    raise ValueError("biểu thức không được hỗ trợ")

@tool
def calculate(expression: str) -> str:
    """Tính biểu thức số học an toàn (không dùng eval)."""
    try:
        return str(_eval_node(ast.parse(expression, mode="eval").body))
    except (SyntaxError, ValueError, ZeroDivisionError) as e:
        return f"Calculation error: {e}"
```

> ⚠️ **LƯU Ý:** Không bao giờ gọi `eval()` với input đến từ LLM hoặc người dùng: nó có thể chạy code tuỳ ý, và `{"__builtins__": {}}` không làm nó an toàn. Whitelist AST ở trên chỉ cho phép số và bốn phép toán cơ bản. Bản thật của project là `calculate` trong `src/agents/tools/knowledge.py`.

## Thêm Tools vào Agent

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools([search_documents, calculate])
```
