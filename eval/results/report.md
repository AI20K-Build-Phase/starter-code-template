# Evaluation Report — AI20K Agent Template v2

> Sinh tự động bởi `eval/run_eval.py` lúc 2026-11-10 11:28 UTC. Chạy lại: `make eval`.

## 1. Benchmark Spec

- Chế độ: **OFFLINE STUB (không có OPENAI_API_KEY — số liệu chỉ chứng minh pipeline chạy)**
- Threshold PASS/FAIL: **0.80** (dưới ngưỡng = regression — good practice #8, team 002)
- Judge tách generator: có (model khác / rule-based khi offline)
- HITL: tool rủi ro auto-approve qua `Command(resume='approve')` trong eval mode

## 2. Dataset

- File: `eval/datasets/golden_sample.jsonl` — **10 case (SAMPLE — đội thay bằng data thật ≥45 case)**
- Phân bố: on-topic 6, off-topic 3, edge 1
- Mỗi case: `must` (hành vi bắt buộc) / `must_not` (hành vi cấm) / `expect_refusal`

## 3. Metrics

| Metric | Target | Actual | Status |
|---|---|---|---|
| Pass rate (toàn bộ) | ≥80% | 10/10 (100%) | PASS |
| On-topic pass | — | 6/6 | — |
| Off-topic pass (không bịa) | — | 3/3 | — |
| Edge pass (chặn injection) | — | 1/1 | — |
| HITL interrupt fired | ≥1 | 1 case | PASS |
| Case có tool thực sự chạy | >0 | 5 | PASS |

## 4. So sánh theo nhóm

| Nhóm | Pass | Nhận xét |
|---|---|---|
| on-topic | 6/6 | Tool được gọi đúng loại, số liệu ra từ tool |
| off-topic | 3/3 | Agent nói 'không có dữ kiện' thay vì bịa |
| edge | 1/1 | Prompt injection bị guardrail chặn ở input layer |

## 5. Feedback từng case

- **[PASS] on-01** (on-topic): đủ mọi MUST, không vi phạm MUST_NOT
- **[PASS] on-02** (on-topic): đủ mọi MUST, không vi phạm MUST_NOT
- **[PASS] on-03** (on-topic): đủ mọi MUST, không vi phạm MUST_NOT
- **[PASS] on-04** (on-topic): đủ mọi MUST, không vi phạm MUST_NOT
- **[PASS] on-05** (on-topic): đủ mọi MUST, không vi phạm MUST_NOT
- **[PASS] on-06** (on-topic): đủ mọi MUST, không vi phạm MUST_NOT
- **[PASS] off-01** (off-topic): đủ mọi MUST, không vi phạm MUST_NOT
- **[PASS] off-02** (off-topic): đủ mọi MUST, không vi phạm MUST_NOT
- **[PASS] off-03** (off-topic): đủ mọi MUST, không vi phạm MUST_NOT
- **[PASS] edge-01** (edge): đủ mọi MUST, không vi phạm MUST_NOT

## 6. Before / After

| Tiêu chí | Template v1 (baseline) | Template v2 (bản này) |
|---|---|---|
| Tool thực sự được gọi | 0 (tools không nối vào graph) | Có — tool_trace trong mọi case on-topic |
| Conditional edge thật | Không (should_continue no-op) | 4 router theo state |
| Chống loop vô hạn | Không | max_iterations + finalize_with_partial |
| HITL cho action rủi ro | Không | interrupt() + Command(resume) |
| Guardrail code-level | Không | 2 lớp (input regex + output Pydantic) |
| Eval chạy lại được | Không (report trống) | `make eval` sinh report này |

> Đội cập nhật bảng này sau mỗi thay đổi lớn (prompt/model/retrieval) — dán 2 cột kết quả `make eval` trước và sau.
