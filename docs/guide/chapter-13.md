---
title: "Nộp bài Demo Day"
weight: 13
---

# Chương 13: Nộp bài Demo Day

> 📊 **Bằng chứng cohort —** Phản hồi Ban Giám Khảo (BGK) cohort 1 ghi lại ba con số nói lên tất cả: **video demo thiếu ở 11/11 đội** (tức 100% đội không có), **82% đội thiếu bằng chứng đánh giá hiệu quả** (evaluation evidence), **64% đội thiếu pitch deck**. Không đội nào mất điểm vì "AI kém thông minh" — phần lớn điểm mất vì **thiếu deliverables** và **demo không chuẩn bị**. Chương này là bản đồ để bạn không lặp lại.

## 13.1 Mười deliverables BTC yêu cầu — kèm số liệu thật từ cohort trước

Ban Tổ Chức (BTC) AI20K yêu cầu mỗi đội nộp **10 deliverables** cho Demo Day. Bảng dưới đây gắn từng deliverable với tình trạng thật của cohort trước (theo phản hồi BGK cohort 1) — để bạn biết chính xác mình đang cạnh tranh ở đâu:

| # | Deliverable | Tình trạng cohort trước | Vì sao đội hay thiếu | Mẹo hoàn thành nhanh |
|---|-------------|------------------------|----------------------|----------------------|
| 1 | Source Code (GitHub repo) | Phần lớn có | Ngại push code dở | Push ngay tuần 1, không đợi hoàn hảo |
| 2 | README.md | Phần lớn có | Viết cuối cùng khi hết giờ | Dùng template, 30 phút là xong 80% |
| 3 | Architecture Diagram | Thường thiếu | Coi là "vẽ cho đẹp" | Vẽ bằng Mermaid ngay trong README (30 phút) |
| 4 | AI Logs (LangSmith/screenshot) | Phần lớn có | Không biết config | Chỉ cần 3 env vars của LangSmith, không thêm code |
| 5 | Live URL | Thường có | Deploy để ngày cuối | Deploy tuần 1 dù chỉ có `/health`, fix dần |
| 6 | Video Demo | **Thiếu 11/11 đội (100%)** | Để cuối, sợ quay, không ai nhận việc | Quay bằng Loom/OBS 1 buổi chiều tuần 5 — đội có video là đội hiếm |
| 7 | Pitch Deck | **Thiếu ~64% đội** | Viết slide khó hơn viết code | Theo template 10 slides ở mục 13.8, mỗi slide 1 câu chủ đề |
| 8 | Development Journal | Phần lớn có | Ghí chú mỗi ngày thấy "thừa" | 2-3 câu mỗi ngày, tổng 10 phút/ngày |
| 9 | Worklog (commit history) | Phần lớn có | Không biết nộp sao | `git log --oneline > docs/worklog.md` — 1 lệnh |
| 10 | Evaluation Evidence | **Thiếu ~82% đội** | Không biết đo gì, đo thế nào | Theo chương 10 mục 10.5 — golden dataset + bảng metrics |

Phân tích nhanh: deliverables dễ nhất là AI Logs và Worklog — không cần code phức tạp, chỉ cần discipline. Ba deliverables thiếu nhiều nhất — Video Demo (100% thiếu), Evaluation Evidence (82% thiếu), Pitch Deck (64% thiếu) — lại chính là ba thứ **đội nào làm được thì gần như chắc chắn vượt phần lớn các đội còn lại**. Đây không phải vòng đua code; đây là vòng đua hoàn thiện deliverables.

Mỗi deliverable cần được đặt đúng vị trí trong GitHub repository:

```
project-root/
├── README.md              ← Deliverable #2
├── docs/
│   ├── architecture.md    ← Deliverable #3 (hoặc .png/.pdf)
│   ├── video-demo.md      ← Deliverable #6 (link YouTube)
│   ├── pitch-deck.pdf     ← Deliverable #7
│   ├── journal.md         ← Deliverable #8
│   ├── worklog.md         ← Deliverable #9
│   └── evaluation.md      ← Deliverable #10
├── src/                   ← Deliverable #1 (Source Code)
├── tests/                 ← Cho Evaluation Evidence
├── .github/workflows/     ← Bonus cho DevOps
├── Dockerfile             ← Bonus cho DevOps
└── docker-compose.yml     ← Bonus cho DevOps
```

> 🔑 **ĐIỂM CHÍNH:** 10/10 deliverables = điểm tối đa ở tiêu chí "Hoàn thành deliverables". Nhiều đội mất điểm không phải vì code kém mà vì thiếu deliverables. Thực tế cohort trước: chỉ cần có Video Demo + Evaluation Evidence, bạn đã khác biệt so với gần như toàn bộ các đội khác cùng cohort.

### Chi tiết từng deliverable

**1. Source Code:** Push toàn bộ code lên GitHub. Repo có cấu trúc rõ ràng, `.gitignore` đúng, không chứa secrets, không chứa file lớn (>10MB). BTC sẽ clone và chạy thử — đảm bảo code chạy được sau khi set env vars.

**2. README.md:** File README là ấn tượng đầu tiên. Phải có: tên dự án, mô tả, screenshot/gif, hướng dẫn cài đặt, cách chạy, cấu trúc thư mục, tech stack, team members. Vì sao đội hay thiếu: viết khi hết giờ. Mẹo: viết README tuần 1 và cập nhật theo — không viết từ đầu tuần 6.

**3. Architecture Diagram:** Sơ đồ kiến trúc thể hiện bạn hiểu hệ thống. Dùng draw.io (miễn phí), Mermaid (trong README), hoặc Excalidraw. Vẽ rõ: Frontend, Backend API, LangGraph Agent, Vector Store, External APIs. Vì sao hay thiếu: đội coi đây là việc "trang trí". Thực tế BGK nhìn diagram trước khi đọc code — diagram rõ ràng nâng điểm tiêu chí kỹ thuật.

**4. AI Logs:** Chứng minh agent hoạt động đúng. Cách dễ nhất: dùng LangSmith (3 env vars, không cần code thêm). Hoặc screenshot terminal output cho thấy agent reasoning steps.

**5. Live URL:** URL truy cập được từ internet. Deploy lên Render (backend), Vercel (frontend). Free tier chấp nhận được. Đảm bảo URL hoạt động ít nhất đến hết ngày Demo Day + 7 ngày. Dùng UptimeRobot chống sleep nếu free tier.

**6. Video Demo:** Quay màn hình 3-5 phút, đi qua main features. Upload YouTube (unlisted OK). Nên có: giới thiệu team, demo main use case, giải thích architecture, demo edge case. Vì sao 100% đội cohort trước thiếu: không ai được giao việc này, và "quay video" nghe như việc của tuần cuối. Mẹo: phân công 1 người chịu trách nhiệm từ tuần 4; video này đồng thời là backup tầng 2 khi demo live gặp sự cố (xem mục 13.4).

**7. Pitch Deck:** Slide thuyết trình cho Demo Day. Thường 10 slides, mỗi slide 1 phút. Xem template chi tiết ở mục 13.8. Vì sao 64% thiếu: đội dồn hết thời gian cho code, để phần "nói về code" lại không có thời gian. Mẹo: draft 10 slide bằng bullet thô ngay tuần 3, chỉnh dần.

**8. Development Journal:** Nhật ký phát triển: quyết định kỹ thuật và lý do, khó khăn gặp phải và cách giải quyết, bài học rút ra. Không cần dài — 2-3 câu mỗi ngày đủ. Đây cũng là nguồn material tốt nhất cho slide "Challenges & Learnings".

**9. Worklog:** Lịch sử phát triển, chứng minh team làm việc đều đặn. Cách dễ nhất: `git log --oneline --since="2026-01-01" > docs/worklog.md`. Hoặc export GitHub contribution graph.

**10. Evaluation Evidence:** Bằng chứng đánh giá chất lượng agent — golden dataset, metrics, benchmark, feedback người dùng. Xem [Chương 10](chapter-10.md) mục 10.5 và 8.6. Với 82% đội cohort trước thiếu deliverable này, đây là cơ hội ghi điểm lớn nhất tính theo effort.

## 13.2 Checklist chi tiết

Dưới đây là checklist từng bước để đảm bảo không bỏ sót deliverables. In ra hoặc copy vào Notion/Trello, check từng mục trước khi nộp.

### Checklist Source Code

- [ ] Repository GitHub public hoặc add BTC làm collaborator
- [ ] Code chạy được sau khi set env vars (README có hướng dẫn)
- [ ] `.gitignore` đúng (không chứa `.env`, `__pycache__`, `.venv`)
- [ ] Không commit secrets (API keys, passwords)
- [ ] Không commit file lớn (models, datasets >10MB)
- [ ] Có `requirements.txt` hoặc `pyproject.toml` với pinned versions
- [ ] Code có type hints
- [ ] Code có docstrings cho functions chính
- [ ] Có ít nhất 1 file test (pytest)

### Checklist README.md

- [ ] Tên dự án và mô tả rõ ràng
- [ ] Screenshot hoặc GIF của ứng dụng
- [ ] Hướng dẫn cài đặt (step-by-step)
- [ ] Hướng dẫn chạy (và chạy với Docker nếu có)
- [ ] Cấu trúc thư mục (tree)
- [ ] Tech stack (bảng hoặc badges)
- [ ] Environment variables cần thiết (liệt kê tên, không ghi giá trị)
- [ ] API documentation (endpoints, request/response format)
- [ ] Team members (tên, vai trò)
- [ ] Link Live URL

### Checklist Architecture Diagram

- [ ] Sơ đồ rõ ràng, dễ đọc
- [ ] Thể hiện đầy đủ components (Frontend, Backend, Agent, DB, External APIs)
- [ ] Có data flow arrows (mũi tên luồng dữ liệu)
- [ ] File format: PNG hoặc SVG (embed trong README)
- [ ] Có mô tả ngắn kèm sơ đồ

### Checklist AI Logs

- [ ] LangSmith project URL (share publicly hoặc screenshot)
- [ ] Hoặc: screenshot terminal logs cho thấy agent reasoning
- [ ] Ít nhất 5-10 trace examples
- [ ] Mỗi trace cho thấy: input, LLM call, retrieval, output

### Checklist Live URL

- [ ] URL trả về HTTP 200 khi truy cập
- [ ] Health check endpoint hoạt động (`/health`)
- [ ] API endpoints chính hoạt động
- [ ] URL được ghi trong README
- [ ] URL hoạt động ổn định (không sleep — dùng UptimeRobot nếu free tier)

### Checklist Video Demo

- [ ] Video 3-5 phút, chất lượng HD
- [ ] Upload YouTube (unlisted OK)
- [ ] Link YouTube ghi trong README hoặc `docs/video-demo.md`
- [ ] Video có: giới thiệu team, demo use case chính, demo edge case
- [ ] Audio rõ ràng, có phụ đề tốt hơn

### Checklist Pitch Deck

- [ ] 10 slides theo template (xem mục 13.8)
- [ ] File PDF (không PowerPoint — tránh font/format issues)
- [ ] Thêm vào `docs/pitch-deck.pdf`
- [ ] Thực hành trình bày trong 10 phút

### Checklist Journal + Worklog

- [ ] Journal: ít nhất 5-7 entries, mỗi entry 2-3 câu
- [ ] Worklog: git log hoặc bảng commit history
- [ ] Cả hai lưu trong `docs/`

### Checklist Evaluation Evidence

- [ ] Bảng test results (pytest output + coverage)
- [ ] Bảng metrics từ golden dataset (pass@k / pass^k, hoặc RAGAS nếu có RAG)
- [ ] Benchmark so sánh (baseline con người hoặc đối thủ)
- [ ] User feedback (ít nhất 3-5 người thật)
- [ ] Code traceability (map test case → feature)

> 💡 **MẸO:** Tạo GitHub Issue hoặc Notion checklist ngay tuần đầu tiên. Check off từng mục khi hoàn thành. Đừng đến tuần cuối mới chạy checklist — lúc đó đã quá muộn để quay video hay viết journal.

## 13.3 Bộ tiêu chí chấm Demo Day — 6 tiêu chí × 5 mức

> 📌 **GHI CHÚ QUAN TRỌNG:** Đây là bộ tiêu chí chính thức chấm Demo Day AI20K (transcribe từ bảng tiêu chí của BTC). **Đối chiếu lại với BTC ở đầu mỗi cohort** — tên tiêu chí và mô tả mức ổn định, nhưng trọng số chính xác từng tiêu chí có thể thay đổi theo cohort; luôn lấy bản BTC phát hành làm chuẩn cuối cùng.

Bộ tiêu chí gồm **6 tiêu chí**, mỗi tiêu chí chấm theo thang **5 mức**:

| Mức điểm | Xếp loại |
|----------|----------|
| 9-10 | Giỏi |
| 7-8 | Khá |
| 5-6 | Trung bình |
| 3-4 | Yếu |
| 1-2 | Kém |

| # | Tiêu chí | Câu hỏi BGK ngầm đặt ra |
|---|----------|--------------------------|
| 1 | Mức độ hoàn thiện của sản phẩm (Demo) | Demo có chạy ổn định không lỗi không? |
| 2 | Kỹ thuật AI / Ứng dụng AI | Đây là kỹ thuật AI thật hay chỉ gọi API? |
| 3 | Đánh giá hiệu quả (Evaluation) | Bạn có số liệu chứng minh agent hiệu quả không? |
| 4 | Giao diện & Trải nghiệm người dùng | Đẹp, tiện dụng, responsive không? |
| 5 | Ý tưởng & Khả năng ứng dụng thực tế | Giải quyết vấn đề thật cho người dùng thật không? |
| 6 | Thuyết trình / Trình bày (Pitch) | Kể chuyện rõ ràng, thuyết phục, trả lời Q&A tốt không? |

Với mỗi tiêu chí, bảng playbook dưới đây trả lời đúng một câu hỏi: **làm gì cụ thể để đạt mức 9-10 (Giỏi), và nộp bằng chứng gì kèm theo.** Đây là north star của toàn bộ guidebook — mọi chương trước đều dẫn về đây.

### Tiêu chí 1: Mức độ hoàn thiện của sản phẩm (Demo)

- **Giỏi (9-10):** demo chạy ổn định không lỗi, các tính năng chính hoạt động đầy đủ, xử lý được edge case.
- **Trung bình (5-6):** chạy được nhưng có lỗi nhỏ, hoặc chỉ phần chính chạy được.
- **Kém (1-2):** demo không chạy được.

| Việc cần làm | Bằng chứng nộp kèm |
|--------------|--------------------|
| Liệt kê 10-15 edge case và mỗi edge case có test tương ứng trong repo (xem [Chương 7](chapter-07.md)) | Thư mục `tests/` với test đặt tên theo edge case |
| Tính năng chưa làm xong thì **ẩn hoặc đánh dấu rõ** — không treo "SOON" trên tính năng cốt lõi (lỗi Beta cohort RA) | Screenshot UI không có dead placeholder |
| Smoke-test demo account sau mỗi deploy trong CI | GitHub Actions log xanh |
| E2E test full user flow quan trọng nhất (Playwright) | `tests/e2e/` trong repo |

> Ghi chú cohort: Gamma regress ngay tại bước nộp bài — một lỗi chặn mới xuất hiện sau khi fix lỗi cũ, vì thiếu E2E regression test. "Hoàn thiện" không phải là "hôm nay chạy được" mà là "có test chứng minh mọi lần deploy đều chạy được".

### Tiêu chí 2: Kỹ thuật AI / Ứng dụng AI

- **Giỏi (9-10):** ứng dụng AI/Agent đúng cách kèm kỹ thuật nâng cao — RAG, multi-agent, guardrails, evaluation.
- **Yếu (3-4):** chỉ gọi API đơn thuần, prompt cơ bản.

| Việc cần làm | Bằng chứng nộp kèm |
|--------------|--------------------|
| Guardrail tối thiểu 2 lớp: prompt + code (Pydantic schema-lock, banned-pattern) — 11/12 đội cohort trước chỉ có 1 lớp prompt | Code guard trong `src/`, có test jailbreak trong `tests/` |
| Có RAG thì đo được chất lượng retrieval + generation (RAGAS, xem [Chương 10](chapter-10.md) mục 10.6) | Bảng RAGAS metrics trong `docs/evaluation.md` |
| Graph có conditional edge thật (hàm routing trả về kết quả khác nhau theo state) | LangSmith trace cho thấy 2 path khác nhau |
| Chống hallucination bằng cơ chế (citation, grounding) chứ không chỉ bằng prompt | Screenshot câu trả lời có citation verify được |

### Tiêu chí 3: Đánh giá hiệu quả (Evaluation)

- **Giỏi (9-10):** có bộ test/data thực tế, số liệu đo lường, so sánh benchmark, feedback người dùng.
- **Yếu (3-4):** không có số liệu.

| Việc cần làm | Bằng chứng nộp kèm |
|--------------|--------------------|
| Golden dataset ≥30 câu on-topic + 15 off-topic từ người dùng thật (chương 10, bài tập 8.5.2) | `eval/datasets/golden.jsonl` |
| Đo pass@k VÀ pass^k, LLM-judge dùng model khác generator | `eval/results/` + bảng metrics |
| Benchmark so baseline con người hoặc đối thủ cạnh tranh | Bảng so sánh 3 cột trong `docs/evaluation.md` |
| Bảng before/after: đo vòng 1 ở tuần 4, sửa, đo lại tuần 6 | 2 cột số liệu cùng dataset |

Đây là tiêu chí mà 82% đội cohort trước không có bằng chứng — playbook chi tiết đầy đủ nhất nằm ở [Chương 10](chapter-10.md) mục 10.5 (bao gồm cả bảng "lên Giỏi" riêng cho tiêu chí này).

### Tiêu chí 4: Giao diện & Trải nghiệm người dùng

- **Giỏi (9-10):** đẹp, tiện dụng, responsive.
- **Kém (1-2):** thô sơ, khó dùng.

| Việc cần làm | Bằng chứng nộp kèm |
|--------------|--------------------|
| Loading states cho mọi LLM call (spinner/skeleton), error message thân thiện (không hiện raw exception) | Screenshot cả 3 trạng thái: loading/success/error |
| Responsive — test trên mobile thật, không chỉ resize browser | Screenshot mobile + desktop |
| Không render reasoning token ra bong bóng chat (lỗi Alpha cohort RA: reasoning render thành tin nhắn user) | Screenshot UI sạch |
| Route `/privacy` thật (không link chết `#`) nếu sản phẩm chạm dữ liệu cá nhân — checklist privacy-by-domain ở [Chương Privacy](chapter-11.md) | Link privacy hoạt động + mô tả xử lý dữ liệu |

### Tiêu chí 5: Ý tưởng & Khả năng ứng dụng thực tế

- **Giỏi (9-10):** giải quyết vấn đề thật cho người dùng thật.
- **Yếu (3-4):** toy problem.

| Việc cần làm | Bằng chứng nộp kèm |
|--------------|--------------------|
| Khảo sát 3 đối thủ trực tiếp trước khi build; nêu được vì sao không dùng giải pháp sẵn có | Bảng competitor trong pitch deck |
| Phỏng vấn ≥5 người dùng thật, thu đúng câu hỏi họ thực sự hỏi (nguồn golden dataset) | File phỏng vấn + thống kê câu hỏi |
| Messaging đồng nhất mọi bề mặt (hero, docs, demo nói cùng một con số) — lỗi Gamma: "~60 min" vs "~35 phút" làm giảm niềm tin BGK | Self-check: 1 con số dùng lại ở mọi nơi |
| USP khai báo rõ và chạy được end-to-end từ UI công khai đến output (xem [Chương 5](chapter-05.md)) | Demo USP ngay trong video demo |

> Ghi chú cohort: sản phẩm bị đánh giá theo khả năng người dùng **chạm được giá trị AI cốt lõi**, không theo số lượng feature. Gamma cohort RA có nội dung rất tốt nhưng user "đi sâu hơn được một đoạn, song vẫn chưa chạm tới giá trị AI cốt lõi".

### Tiêu chí 6: Thuyết trình / Trình bày (Pitch)

- **Giỏi (9-10):** rõ ràng, thuyết phục, demo mượt, trả lời câu hỏi tốt.

| Việc cần làm | Bằng chứng nộp kèm |
|--------------|--------------------|
| Kể chuyện theo AIDA thay vì liệt kê tính năng (xem mục 13.4) | `presentation/demo_script.md` |
| Backup 3 tầng: live → video → screenshot (mục 13.4) | Video YouTube + bộ screenshot annotated |
| Tổng duyệt pitch + demo trước BGK **đúng 1 tuần trước sự kiện** (khuyến nghị chính thức từ BGK) | Feedback BGK từ buổi tổng duyệt đã được fix |
| Tập đủ 3 lần + prep Q&A theo danh sách câu hỏi dễ gặp | Ghi hình lần tập cuối |

### Chiến lược điểm số

Nguyên tắc: **đảm bảo mức Khá (7-8) ở cả 6 tiêu chí trước, rồi đẩy 2-3 tiêu chí lên Giỏi (9-10).** Chọn tiêu chí đẩy Giỏi theo thế mạnh của đội — nhưng lưu ý hai tiêu chí có "quỹ điểm thừa" lớn nhất từ cohort trước là **Đánh giá hiệu quả** (82% đội không có bằng chứng) và **Thuyết trình** (video thiếu 11/11 đội) — tức là effort tương đối vừa phải đã vượt mặt phần lớn các đội.

> 🔑 **ĐIỂM CHÍNH:** Không dồn hết vào 1 tiêu chí mà bỏ 5 tiêu chí còn lại. BGK chấm tổng thể sản phẩm — một đội 7-7-7-7-7-7 đứng trước đội 10-10-4-4-4-4.

## 13.4 Nghệ thuật Demo — kể chuyện thay vì liệt kê tính năng

> Nguồn: nội dung workshop "How to Demo Like a Pro" (Lộc Đặng, VinUni Nhân Tài AI Workshop 2026). Nguyên tắc mở đầu: "Demo thất bại không phải do sản phẩm kém — mà do chưa chuẩn bị."

### Demo Curse là thật

"Mọi thứ có thể hỏng trong demo đều sẽ hỏng." Bản đồ thảm họa demo quen thuộc: Wi-Fi chết giữa chừng, AI model rate limit/timeout đúng lúc chiếu, bug từ deploy sáng hôm đó, presenter run quên flow, OS update sai lúc. Cohort dữ liệu ở trên (video thiếu 11/11) cho thấy hầu như không đội nào có phương án khi thảm họa xảy ra. Cả mục này là về việc loại từng rủi ro một.

### AIDA Storytelling — cấu trúc demo 3-5 phút

Sai lầm phổ biến nhất: demo theo **feature list** — "Tính năng 1 là... Tính năng 2 là... Tính năng 3 là...". Khán giả không nhớ feature; họ nhớ **cảm giác và vấn đề được giải quyết**. Chuyển từ "đây là những gì app làm" sang "đây là câu chuyện của người dùng".

| Bước | Tên | Làm gì | Ví dụ |
|------|-----|--------|-------|
| **A** | Attention | Mở đầu ấn tượng: con số gây sốc, câu hỏi bất ngờ, tình huống thực tế khiến khán giả gật đầu | "Mỗi lần nộp báo cáo nhóm, bạn mất bao nhiêu giờ để gộp file từ 5 người?" |
| **I** | Interest | Vì sao phải quan tâm: pain point của ai? Xảy ra bao nhiêu lần? Chi phí bao nhiêu? | "Khảo sát 200 sinh viên: trung bình 2.3 giờ mỗi lần nộp — mỗi tuần." |
| **D** | Desire | Demo như giải pháp TỰ NHIÊN của câu chuyện — không liệt kê feature | Live demo: "Với app này, cả nhóm edit cùng lúc, submit 1 click — xong trong 5 phút." |
| **A** | Action | Call to action: khán giả trải nghiệm ngay tại chỗ | "Thử ngay tại bit.ly/your-app hoặc quét QR code trên màn hình." |

### 4 framework demo — chọn theo khán giả

| Framework | Phù hợp nhất | Bối cảnh |
|-----------|--------------|----------|
| AIDA | Demo ngắn 3-5 phút | Pitch competition, hackathon, Demo Day AI20K |
| Problem → Solution → Proof | Technical demo | Khi khán giả là developers/engineers |
| Before / After / Bridge | Workflow transformation | Sản phẩm thay thế một quy trình cũ |
| Hero's Journey | Startup pitch dài | Investor demo, user story phức tạp |

Quy tắc: **chọn 1 framework và giữ nguyên** — một câu chuyện mạch lạc tốt hơn 4 framework nửa vời. Với Demo Day AI20K (10 phút, khán giả BGK hỗn hợp kỹ thuật + kinh doanh), AIDA là lựa chọn mặc định.

### Showcase Mode — không bao giờ demo trên dữ liệu thật

Nguyên tắc vàng: **không dùng dữ liệu thật / live input khi demo lần đầu**. Xây dựng Showcase Mode với dummy data được chọn lọc kỹ — trông đẹp, realistic, nhưng không phải data thật, và không chứa PII.

Showcase checklist:

- **Database:** dummy data đã seed? Data trông realistic? Không có PII thật?
- **Account:** demo account đã tạo? Pre-login sẵn? Avatar/profile đẹp?
- **App state:** app ở đúng màn hình cần demo? Không có error messages? Loading đã xong?

Link demo (QR/short link) phải trỏ **thẳng vào trạng thái showcase đã có data** — không yêu cầu signup, không để khán giả tự đánh dấu trước giá trị của bạn.

### Backup 3 tầng — khi live chết vẫn sống

| Tầng | Là gì | Khi nào dùng |
|------|-------|--------------|
| 1. Live demo | Chạy app thật trên showcase mode | Mặc định |
| 2. Video quay sẵn | 1 lần chạy hoàn chỉnh 3-5 phút, upload YouTube, lưu file local | Live chết, mạng chết, rate limit |
| 3. Screenshot step-by-step | Mỗi bước demo 1 screenshot có annotation (mũi tên, highlight) | Cả video và live đều không chạy được |

Video backup (tầng 2) chính là deliverable #6 — một công hai việc: nộp BTC và cứu mạng khi demo sự cố. Screenshot step-by-step (tầng 3) có lợi ích ẩn: quá trình chụp buộc bạn test lại toàn bộ flow thêm một lần. Tool gợi ý: Loom, OBS Studio (free), QuickTime (macOS), Screen Studio; chụp ảnh: CleanShot X, Snagit, Greenshot.

### Demo account riêng — không dùng account cá nhân lên sân khấu

Nên làm:

- Tạo `demo@yourapp.com` — tên rõ ràng
- Pre-login sẵn trước khi lên sân khấu
- Profile đẹp: avatar, display name chuyên nghiệp
- Tắt hết notifications trên máy trình chiếu
- Test OAuth flow ngày hôm trước, ghi credentials ra giấy

Không làm: dùng account cá nhân (lộ email/tên thật), để notification bật trên máy chiếu, có data nhạy cảm hoặc test data xấu, signup live trước mặt khán giả, quên mật khẩu ngay trên sân khấu.

Kèm theo: rút gọn link (bit.ly), đặt QR code ở slide cuối và **để nguyên trong suốt phần Q&A** để khán giả quét bất cứ lúc nào, gắn UTM để biết bao nhiêu người thực sự click sau buổi demo.

### Checklist 1 ngày trước Demo Day

APP:

- [ ] Deploy phiên bản stable (không push code mới sáng hôm sau)
- [ ] Dummy data đã seed lại?
- [ ] Demo account đã tạo, pre-login sẵn?
- [ ] Test full flow 1 lần cuối?
- [ ] Không có console errors?

BACKUP:

- [ ] Video demo đã quay?
- [ ] Screenshots step-by-step?
- [ ] Slide backup sẵn sàng?
- [ ] File video lưu local (không phụ thuộc mạng)?
- [ ] Link rút gọn đã test?

### Presenter mindset: 3 lần tập + Q&A prep

- **Luyện tập 3 lần:** chạy thử flow đầy đủ ít nhất 3 lần — trước gương, trước bạn cùng đội, rồi mới lên sân khấu.
- **Chuẩn bị Q&A có sẵn:** "Nếu scale lên 1000 users thì sao?" / "Tại sao chọn tech này thay vì cái kia?" / "Roadmap tiếp theo?" / "Làm sao xử lý hallucination?" — có câu trả lời soạn sẵn, phân công ai trả lời câu nào.
- **Khi sự cố xảy ra:** nói thẳng với khán giả → switch sang backup → tiếp tục. Đừng hoảng loạn, đừng im lặng, đừng xin lỗi nhiều lần.
- **Phân bổ thời gian:** khoảng 70% thời gian cho story + value, 30% cho technical details và Q&A. Demo là kể câu chuyện — không phải chạy phần mềm.

## 13.5 Lộ trình 6 tuần đến Demo Day

Deliverables không phải việc của tuần cuối — mọi mục ở trên đều có mốc cụ thể trong timeline 6 tuần. Khuyến nghị từ BGK cohort trước: **tổng duyệt pitch + demo trước BGK ít nhất 1 tuần trước sự kiện** (tuần 5), kèm mời BGK góp ý giữa kỳ để còn thời gian sửa.

```mermaid
timeline
    title 6 tuần đến Demo Day
    Tuần 1 : Clone template, deploy /health lên cloud : Mở checklist 10 deliverables (Notion/GitHub Issues) : Viết README bản đầu
    Tuần 2 : Nộp proposal (problem, user, USP) : Khảo sát 3 đối thủ + phỏng vấn 5 user thật : Bắt đầu thu golden dataset
    Tuần 3 : Build tính năng chính, CI/CD xanh : Draft 10 slide pitch deck bản thô : Journal mỗi ngày 2-3 câu
    Tuần 4 : Midway demo nội bộ theo AIDA : Đo eval vòng 1 (baseline "before") : Phân công người quay video demo
    Tuần 5 : Tổng duyệt trước BGK (đúng 1 tuần) : Quay video backup + screenshot step-by-step : Chỉnh pitch deck theo feedback
    Tuần 6 : Demo Day — seed showcase mode : Pre-login demo account, tắt notifications : Tập lần 3 + Q&A prep
```

Ba mốc không thể trễ: **proposal tuần 2** (trễ thì build sai thứ), **midway demo tuần 4** (không có thì không phát hiện demo sự cố kịp sửa), **tổng duyệt tuần 5** (BGK khuyến nghị 1 tuần buffer — tổng duyệt sát ngày thì không còn thời gian fix).

## 13.6 Những lỗi phổ biến cần tránh

Kinh nghiệm thực tiễn cho thấy những lỗi sau lặp đi lặp lại ở nhiều đội. Hiểu và tránh là cách nhanh nhất cải thiện điểm số.

### Top 5 lỗi phổ biến nhất

**Lỗi #1: Không có CI/CD**

Hầu hết các đội không thiết lập CI/CD pipeline. Không có CI nghĩa là code không được test tự động, không được lint tự động — và cũng không có smoke-test demo account sau mỗi deploy.

```yaml
# SAI: Không có .github/workflows/
# (thư mục không tồn tại)

# ĐÚNG: .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v
```

**Lỗi #2: Không có test**

Đa số đội không có test tự động, coverage = 0%. BTC không thể verify code hoạt động đúng, và chính đội cũng không thể tự phát hiện lỗi — cohort trước, mọi CRITICAL/HIGH đều do QA bên ngoài phát hiện, không đội nào tự bắt được lỗi của mình.

```python
# SAI: Không có thư mục tests/
# (hoặc tests/ rỗng)

# ĐÚNG: tests/test_api.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_health(client):
    response = await client.get("/health")
    assert response.status_code == 200
```

**Lỗi #3: Bare except và silent fallback**

Bắt exception với `except:` hoặc `except Exception` mà không log. Cohort trước có đội viết `except Exception: return default` — AI chạy regression giữa chừng mà không ai biết.

```python
# SAI: Bare except
try:
    result = llm.invoke(prompt)
except:  # Bắt mọi thứ, che giấu lỗi
    pass

# ĐÚNG: Bắt cụ thể + log
import logging
logger = logging.getLogger(__name__)

try:
    result = llm.invoke(prompt)
except openai.APIError as e:
    logger.error(f"LLM API error: {e}")
    raise HTTPException(status_code=503, detail="AI service unavailable")
except openai.RateLimitError:
    logger.warning("Rate limit hit, retrying...")
    # Retry logic
except ValidationError as e:
    logger.error(f"Validation error: {e}")
    raise HTTPException(status_code=422, detail=str(e))
```

**Lỗi #4: Hardcoded secrets**

Nhiều đội commit API key trực tiếp vào source code trên GitHub. Key có thể bị dùng trái phép, tốn tiền.

```python
# SAI: Hardcoded API key
openai_client = OpenAI(api_key="sk-proj-abc123...")
DATABASE_URL = "postgresql://admin:password123@localhost/db"

# ĐÚNG: Dùng environment variables
import os
from dotenv import load_dotenv

load_dotenv()
openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///local.db")
```

```text
# .gitignore (luôn có dòng này)
.env
```

**Lỗi #5: Thiếu Evaluation Evidence**

82% đội cohort trước không có bằng chứng đánh giá hiệu quả. Đây là deliverable bị bỏ qua nhiều nhất nhưng là cơ hội ghi điểm lớn nhất — làm theo [Chương 10](chapter-10.md) mục 10.5, xong trong 1-2 ngày.

## 13.7 Tips ghi điểm từ kinh nghiệm thực tiễn

Kinh nghiệm từ các đội đạt kết quả cao cho thấy những điểm chung tạo nên khác biệt.

### Điểm chung của top teams

**1. Đủ 10 deliverables.** Đội đạt điểm cao nộp đủ hoặc gần đủ (9-10/10). Deliverables hoàn chỉnh = tín hiệu chuyên nghiệp.

**2. Code có cấu trúc rõ ràng.** Tổ chức theo module: `app/api/`, `app/agent/`, `app/core/`, `app/models/`. Không dump tất cả code vào 1-2 file, mỗi module có vai trò rõ ràng.

```text
# Cấu trúc tốt (ví dụ)
app/
├── __init__.py
├── main.py              # FastAPI app
├── api/
│   ├── health.py        # Health endpoints
│   └── chat.py          # Chat endpoints
├── agent/
│   ├── graph.py         # LangGraph graph
│   ├── nodes.py         # Agent nodes
│   ├── state.py         # State definition
│   └── tools.py         # Agent tools
├── core/
│   ├── config.py        # Settings
│   └── logging_config.py
└── services/
    └── vector_store.py  # Vector store service

# Cấu trúc kém (ví dụ)
app.py                   # Tất cả trong 1 file
agent.py                 # Tất cả agent logic
```

**3. README chuyên nghiệp.** README là thứ BTC đọc đầu tiên — screenshot, architecture diagram, install guide, API docs, team info. README tốt nâng ấn tượng ở mọi tiêu chí.

**4. Có tests.** Top teams có ít nhất 5-10 test cases cho API endpoints và agent nodes, kể cả test edge case.

**5. Docker + deployment ổn định.** Dockerfile, Live URL hoạt động, health check.

### Tips cụ thể

**Tip 1: README "vàng"** — README là deliverable ROI cao nhất. 30 phút viết README tốt đáng giá hơn 3 tiếng thêm feature.

**Tip 2: Deploy sớm** — Deploy tuần 1 dù chỉ có `/health`. Nhiều đội deploy ngày cuối và gặp lỗi không kịp fix.

**Tip 3: Screenshot mọi thứ** — App chạy, API docs, test output, LangSmith traces, CI/CD green checks. Bằng chứng hình ảnh mạnh hơn text.

**Tip 4: Git history đều đặn** — Commit hàng ngày, message rõ ràng. 50 commits trong 4 tuần tốt hơn 3 commits ngày cuối.

```bash
# Tốt: commit message rõ ràng
git commit -m "feat: add RAG retrieval node with ChromaDB"
git commit -m "fix: handle empty query in chat endpoint"
git commit -m "test: add integration tests for chat API"

# Kém: commit message chung chung
git commit -m "update"
git commit -m "fix"
git commit -m "wip"
```

**Tip 5: Nộp Evaluation Evidence** — 82% đội thiếu. Chạy pytest + golden dataset, chụp kết quả, viết bảng metrics. Xong trong 1-2 ngày theo chương 10.

**Tip 6: Quay video demo tuần 5, không phải đêm trước** — 11/11 đội cohort trước không có video. Video vừa là deliverable #6, vừa là backup tầng 2 khi demo live gặp sự cố.

## 13.8 Pitch Deck — Slide thuyết trình

Pitch Deck là bài thuyết trình Demo Day — thường 10 phút cho 10 slides. 64% đội cohort trước thiếu deliverable này. Slide tốt + thuyết trình tốt nâng điểm thuyết phục ở mọi tiêu chí.

### Cấu trúc 10 slides

**Slide 1: Title (Tiêu đề)**
- Tên dự án
- Tagline (1 câu mô tả)
- Tên team + logo
- Ngày Demo Day

**Slide 2: Problem (Vấn đề)**
- Mô tả pain point cụ thể
- Ai đang gặp vấn đề? (target user)
- Tần suất/mức độ nghiêm trọng
- Số liệu nếu có (ví dụ: "70% sinh viên không biết sử dụng AI")

**Slide 3: Solution (Giải pháp)**
- Giải pháp của bạn giải quyết vấn đề như thế nào
- Khác biệt với các giải pháp hiện có
- Demo screenshot hoặc mockup

**Slide 4: Product Demo (Sản phẩm)**
- Screenshot hoặc GIF demo thực tế
- Highlight main features
- User flow chính

**Slide 5: Architecture (Kiến trúc)**
- Architecture diagram (đơn giản, dễ hiểu)
- Giải thích tech stack choices
- Tại sao chọn LangGraph? Tại sao chọn vector store này?

**Slide 6: AI/LLM Approach (Cách tiếp cận AI)**
- RAG pipeline, Agent design, Prompt strategy
- LangGraph graph diagram
- Evaluation metrics (golden dataset pass@k, RAGAS)

**Slide 7: Technical Highlights (Điểm nổi bật kỹ thuật)**
- CI/CD pipeline
- Test coverage
- Performance metrics
- Guardrail 2 lớp (code + prompt)

**Slide 8: Demo Video (Video demo)**
- Embed video hoặc QR code link YouTube
- 2-3 phút demo main use case

**Slide 9: Challenges & Learnings (Thách thức & Bài học)**
- Khó khăn lớn nhất và cách giải quyết
- Bài học kỹ thuật
- Nếu làm lại, bạn sẽ thay đổi gì?

**Slide 10: Team & Next Steps (Team & Bước tiếp theo)**
- Team members + vai trò
- Roadmap tiếp theo
- Cảm ơn + Q&A + QR code trải nghiệm ngay

### Tips cho slide và thuyết trình

**Slide design:**
- Mỗi slide chỉ 1 idea chính
- Font size tối thiểu 24pt (BGK ngồi xa)
- Hình ảnh > text (1 hình = 1000 từ)
- Dark background + light text (projector tốt hơn)
- Không quá 30 từ mỗi slide

**Thuyết trình:**
- Thực hành ít nhất 3 lần trước Demo Day (mục 13.4)
- Time rehearsal: 10 slides × 1 phút = 10 phút
- Chỉ 1 người nói chính, không ai đọc slide
- Demo live luôn có backup 3 tầng (mục 13.4)
- 70% thời gian cho story + value, 30% cho technical + Q&A

> 💡 **MẸO:** BGK sẽ hỏi về technical decisions. Chuẩn bị câu trả lời cho: "Tại sao chọn LangGraph thay vì CrewAI/AutoGen?", "Làm sao giảm hallucination?", "Cost per request là bao nhiêu?", "Làm sao scale khi có 1000 users đồng thời?"

## Bài tập cuối chương

**Bài tập 9.1 (output: `presentation/demo_script.md`) — Script demo 3 phút theo AIDA.** Viết script từng câu cho demo 3 phút của đội bạn, chia 4 nhánh AIDA:

- **Attention (15 giây):** 1 câu hỏi hoặc con số mở đầu khiến BGK gật đầu. Không được bắt đầu bằng "Xin chào, chúng tôi là đội...".
- **Interest (30 giây):** pain point của ai, xảy ra bao nhiêu lần, chi phí bao nhiêu — dùng số liệu từ phỏng vấn user thật của bạn (chương 5), không bịa.
- **Desire (2 phút):** kịch bản click từng bước trên Showcase Mode — mỗi dòng script ghi rõ [CLICK làm gì] → [Màn hình hiện gì] → [Nói câu gì]. Không liệt kê tính năng; mọi click phải phục vụ câu chuyện.
- **Action (15 giây):** link rút gọn + QR code, mời BGK trải nghiệm ngay.

Quy tắc chấm chéo: cho đội bạn đọc script khi không nhìn màn hình — nếu họ hiểu được câu chuyện chỉ qua lời nói, script đạt. Script này đồng thời là kịch bản quay video demo (deliverable #6).

## Exit-test chương (tự kiểm — trả lời được mới được sang chương sau)

1. Ba deliverables bị thiếu nhiều nhất ở cohort trước là gì (kèm tỷ lệ), và ba mục đó đều thuộc nhóm "dễ làm hay khó làm"? Kế hoạch của bạn chốt chúng ở tuần nào trong timeline 6 tuần?
2. Trong 6 tiêu chí chấm Demo Day, đội bạn chọn đẩy tiêu chí nào lên mức Giỏi 9-10? Bằng chứng nộp kèm cho tiêu chí đó là file gì trong repo, và file đó được tạo ở tuần nào trong timeline 6 tuần?
3. Backup 3 tầng khi demo live gặp sự cố gồm những tầng nào? Tầng 2 kiêm luôn deliverable số mấy trong bảng 10 deliverables? (Gợi ý: xem mục 13.4 và mục 13.1.)
4. Vì sao BGK khuyến nghị tổng duyệt trước 1 tuần thay vì 2 ngày trước Demo Day? Điều gì xảy ra với đội Gamma cohort trước khi sửa xong mà không có thời gian regression test?

## Tóm tắt

Trong chương này, chúng ta đã tìm hiểu mọi thứ cần biết để nộp bài Demo Day thành công:

- **10 deliverables kèm số liệu thật** — Video Demo thiếu 11/11 đội, Evaluation Evidence thiếu 82%, Pitch Deck thiếu 64%: ba deliverable này là lợi thế cạnh tranh lớn nhất
- **Checklist chi tiết** cho từng deliverable — không bỏ sót gì
- **Bộ tiêu chí chấm 6 tiêu chí × 5 mức** (bộ tiêu chí chính thức — đối chiếu BTC mỗi cohort) — kèm playbook "lên Giỏi" với việc cụ thể + bằng chứng nộp kèm cho từng tiêu chí
- **Nghệ thuật Demo** — AIDA storytelling thay feature-list, 4 framework theo khán giả, Showcase Mode, backup 3 tầng, demo account riêng, checklist 1 ngày trước, 3 lần tập + Q&A prep
- **Timeline 6 tuần** — proposal tuần 2, midway demo tuần 4, tổng duyệt trước BGK tuần 5
- **Top 5 lỗi phổ biến** — Không CI/CD, không test, bare except, hardcoded secrets, thiếu Evaluation Evidence
- **Pitch Deck 10 slides** — template hoàn chỉnh cho Demo Day

Cuối cùng, hãy nhớ: Demo Day không chỉ là thi — nó là cơ hội thể hiện kỹ năng engineering và teamwork. BGK đánh giá tổng thể sản phẩm, không chỉ code. Deliverables đầy đủ + demo kể chuyện hay + backup sẵn sàng = chiến thắng.

## Checklist cuối cùng trước khi nộp

- [ ] 10/10 deliverables đã hoàn thành?
- [ ] README có screenshot, install guide, API docs?
- [ ] Live URL hoạt động (test trên browser khác + incognito)?
- [ ] Tests chạy pass (pytest green)?
- [ ] Không có hardcoded secrets trong code?
- [ ] Không có bare except, không silent fallback?
- [ ] Docker build thành công?
- [ ] CI/CD pipeline xanh (GitHub Actions green)?
- [ ] Git history đều đặn (không phải 5 commits ngày cuối)?
- [ ] Pitch Deck đã thực hành thuyết trình 3+ lần?
- [ ] Video demo đã quay (backup tầng 2)?
- [ ] Showcase Mode đã seed dummy data, demo account pre-login?
- [ ] Đã tổng duyệt trước BGK đủ 1 tuần?
