# 🏔️ MONTANA STATE UNIVERSITY — GALLATIN COLLEGE
# M090 INTRODUCTORY ALGEBRA: MASTER CURRICULUM BLUEPRINT & SYSTEM ARCHITECTURE
> **Document:** `design_montana.md`  
> **Institution:** Gallatin College, Montana State University (Bozeman, MT)  
> **Department:** Developmental Mathematics  
> **Course:** M090 Introductory Algebra (Fall / Spring 15-Week Semester)  
> **Course Lead:** Prof. Eunju Park (Lead Faculty)  
> **Instructional Partner:** TA Sora (Senior Teaching Assistant & Student Advocate)  
> **Structure:** 15 Weeks • 3 Sessions/Week = **45 Master Lectures** (20–25 Minutes per Lecture)  
> **Pedagogical Strategy:** "One Problem = One Slide" • Authentic 2-Presenter High-Frequency Tiki-Taka (8~14 Turns/Slide) • AI Step-by-Step LaTeX Solutions  
> **Core Textbook:** *M090 Introductory Algebra: Student Workbook (Notes Packet)*  
> **Curriculum Status:** **100% COMPLETE (361 Slides, 107,294 Words, 825.3 Minutes, 0 KaTeX Errors)**  
> **Comprehensive Progress Report:** [COMPREHENSIVE_PROGRESS_REPORT.md](file:///c:/Oikos%20Univ/Montana_State_Univ/COMPREHENSIVE_PROGRESS_REPORT.md)

---

## 0. 📖 TEXTBOOK SUPREMACY PRINCIPLE (교재 최우선주의 — 제1원칙)

> **"내용이 아무리 좋아도, 미리 배포되고 학생들이 공부하고 있는 교재 우선입니다. 교재의 문항들은 교수들이 심혈을 기울여 수업하기 위해 만든 소중한 핵심 자료입니다. 그 교재를 가지고 공부하는 학생들이, 교재에서 본 바로 그 문제의 해설을 온라인에서 보아야 합니다."**

```mermaid
flowchart LR
    WB["📘 M090 Full Student Workbook<br/>(학생들이 소지하고 공부하는 교재)"] -->|"1:1 직결"| SL["🖥️ 온라인 슬라이드 & 풀이<br/>(One Problem = One Slide)"]
    SL --> P1["📌 정확한 Workbook Section & Page 표기 (Workbook p. 4)"]
    SL --> P2["🎯 교재 원문 문항 그대로 100% 반영 (Board Work #1~#14, Ex 1~5)"]
    SL --> P3["💡 AI 기반 엄밀한 KaTeX 단계별 해설 & Sora의 Pro-Tip"]
    SL --> P4["🎙️ Prof. Park & TA Sora 2인 대화로 교재 문항 풀이 코칭"]
```

### 0.1. 교재 연계 3대 준수 수칙
1. **임의 문항 배제 & 교재 원본 1:1 매칭:**
   - 교재 외의 임의 창작 문제나 모호한 요약 카드로 대체하지 않으며, 학생 워크북(`M090 Full Student Workbook.pdf`)에 인쇄된 번호와 수식을 원형 그대로 화면에 제시합니다.
2. **명확한 단원·페이지·문항 번호 표기:**
   - 모든 슬라이드 배지 및 소제목에 `Section X.X [Board Work / Example] #N (Workbook p. Y)`을 반드시 명시하여, 학생이 종이 책과 화면을 번갈아 볼 때 1초 만에 일치하는 문제를 찾을 수 있게 합니다.
3. **완전한 순차 풀이(No Skipping):**
   - 워크북 한 페이지에 수록된 문항(예: Section 1.0 p.4의 14개 문제)은 한 문제도 빠짐없이 차례대로 완벽하게 강의 슬라이드로 커버합니다. (L01: #1~#7 ➔ L02: #8~#14)

---

## 1. 🎯 COURSE MISSION & DEVELOPMENTAL MATH PHILOSOPHY

```mermaid
flowchart TD
    A["GALLATIN COLLEGE MSU • DEVELOPMENTAL MATHEMATICS"] --> B["수학 불안감(Math Anxiety) 해소 & 자기 효능감 구축"]
    A --> C["One Problem = One Slide (시각적 과부하 방지)"]
    A --> D["교수-조교 2인 팟캐스트 티키타카 (공감과 질문 중심)"]
    A --> E["AI 기반 LaTeX 단계별 시각적 풀이 (명확한 수식 전개)"]

    B --> F["미국 대학생 눈높이에 맞춘 일상/몬태나 로컬 예시 (Bozeman, Skiing, Elevation)"]
    C --> G["슬라이드당 1개 문항 집중 ➔ 인지 부하 최소화"]
    D --> H["학생들이 자주 틀리는 부호 실수, 괄호 누락, 분수 공포 집중 공략"]
    E --> I["수식 한 줄 한 줄의 논리적 이유(Why)를 직관적으로 제시"]
```

### 1.1. 발달수학(Developmental Mathematics)의 본질과 사명
- **대상의 특수성:** M090 Introductory Algebra 수강생은 고등학교 이후 수학과 단절되었거나, 수학적 트라우마 및 불안감(Math Anxiety)을 겪는 미국 대학 신입생들입니다.
- **교육 철학:** 단순한 기계적 암기가 아니라 **"왜(Why) 이 공식이 성립하는가"**에 대한 직관적 이해와, 실생활 속 문제 해결 도구로서의 대수학을 경험하게 합니다.
- **심리적 안전지대 형성:** "틀려도 괜찮다. 어디서 부호가 바뀌었는지 조교 Sora와 함께 찾아보자!"라는 친근하고 지지적인 학습 환경을 구축합니다.

---

## 2. 🎙️ 2-PRESENTER TIKI-TAKA PEDAGOGICAL SPECIFICATIONS (교수 & 조교 페르소나 및 대화 규약)

```mermaid
graph LR
    P["👩‍🏫 Prof. Eunju Park<br/>(50대 후반 여성 교수 / 원리·구조·차분한 톤)"] <--> S["👩‍🎓 TA Sora<br/>(20대 중반 여성 조교 / 톡톡 튀는 발랄한 톤·공감)"]
    N["🎙️ Male Narrator<br/>(영어 스크립트 전체 낭독 / 신뢰감 있는 남성 음성)"]
```

### 2.1. 강사진 및 내레이터 페르소나 사양

| 역할 / 화자 | 인물 설정 및 연령대 | 주요 대화 기여 포인트 | 음성 합성 규격 (TTS 엔진) |
| :--- | :--- | :--- | :--- |
| **👩‍🏫 Prof. Eunju Park** (교수) | • **50대 후반 여성 (Female, Late 50s)**<br/>• Gallatin College 발달수학 전담 교수<br/>• 온화하고 지적이며 깊은 격려의 리더십<br/>• 수학적 구조와 논리적 연계 강조 | • 도발적/흥미로운 오프닝 질문 던지기<br/>• 수식의 숨겨진 원리와 대수적 패턴 설명<br/>• 학생들의 오개념을 짚어주고 원리적 해결책 제시<br/>• 보즈먼(Bozeman) 현지 실생활 예시 연결 | `en-US-JennyNeural` / 성숙하고 차분한 여성 톤<br/>(Pitch: 0.82, Rate: 0.85, 품격 있는 50대 여성 교수) |
| **👩‍🎓 TA Sora** (수석 조교) | • **20대 중반 여성 (Female, Mid 20s)**<br/>• 친근하고 열정적인 학생들의 든든한 멘토<br/>• 톡톡 튀는 발랄함과 밝고 에너지 넘치는 진행자<br/>• 학생들이 흔히 하는 실수를 귀신같이 짚어냄 | • "교수님! 학생들이 여기서 부호(- * - = +)를 제일 많이 실수하잖아요!"<br/>• "Sora's Pro-Tip: 괄호를 먼저 치고 대입하세요!"<br/>• 학생 입장에서 헷갈리는 부분 즉각 질문<br/>• 문제 풀이 후 성공적인 'Aha!' 모먼트 리액션 | `en-US-AriaNeural` / 톡톡 튀고 상큼발랄한 톤<br/>(Pitch: 1.38, Rate: 1.05, 에너지 넘치는 20대 중반 여성) |
| **🎙️ Male Narrator** (전체 낭독) | • **남성 내레이터 (Male Narrator)**<br/>• English Script 전체 통독 전담<br/>• 명료하고 안정된 발음과 신뢰감 있는 보이스 | • 슬라이드 대본 전체를 완결성 있게 완독<br/>• ESL 학생을 위한 명확한 딕션과 호흡 제공<br/>• 통독 청취 모드 지원 | `en-US-GuyNeural` / 신뢰감 있는 남성 톤<br/>(Pitch: 0.95, Rate: 0.92, 명료한 남성 낭독) |

### 2.2. 슬라이드당 6~9턴 고밀도 티키타카 원칙 (Micro-Turns)
1. **일방적 독백 금지:** 교수 혼자 3줄 이상 설명하면 조교 Sora가 즉시 브레이크를 걸고 질문하거나 학생 팁을 보충합니다.
2. **리얼한 리액션 및 감탄사 사용:**
   - *"Wait, Professor Park! Before you simplify, look at that negative sign outside the parenthesis!"*
   - *"Haha, exactly Sora! That minus sign distributes to EVERY single term inside!"*
   - *"Oh wow, that makes so much sense now! Let's write out the steps together!"*
3. **몬태나 현지 생활 밀착형 비유 (Montana Context):**
   - 보즈먼(Bozeman)의 해발고도와 끓는점($212^\circ\text{F} \to 201^\circ\text{F}$ at the 'M' trail)
   - 브리저 보울(Bridger Bowl) / 빅스카이(Big Sky) 스키 패스 비용 모델링
   - 몬태나 겨울철 기온 변화(음수 덧셈/뺄셈)
   - 중고차 딜러 커미션 계산 등 실제 워크북 문항 반영

---

## 3. 📐 "ONE PROBLEM = ONE SLIDE" STRATEGY & LATEX AI ARCHITECTURE

```mermaid
graph TD
    A["Slide Display"] --> B["Problem Box (원문 문항 & 난이도 태그)"]
    A --> C["AI Step-by-Step Solution (엄격한 LaTeX 수식 표기)"]
    A --> D["Sora's Pro-Tip & Common Pitfall (함정 주의 배너)"]
    A --> E["Prof. Park & TA Sora Audio Script (6~9턴 대본)"]
    A --> F["Korean Guide & Math Terminology (교수자/튜터용)"]
```

### 3.1. 원 페이지 원 메시지 (One Page One Message) 원칙
- **1개 슬라이드 = 오직 1개의 수학 문제(또는 핵심 정의 1개):**
  - 문제 문항이 복합 문항(예: Ex 2: A, B, C, D)인 경우, **A, B, C, D 각각을 독립된 슬라이드로 분리**합니다.
  - 슬라이드 안에 여러 문제가 혼재되어 학생이 길을 잃지 않도록 완벽히 격리합니다.
- **시각적 계층 구조:**
  - 상단: 단원 / 섹션 / 문항 번호 (`Unit 1 • Section 1.1 • Example 2A`)
  - 중앙 좌측: 문항 제시 (Clean LaTeX Typography)
  - 중앙 우측: 단계별 AI 해설 (Step 1 $\to$ Step 2 $\to$ Final Answer)
  - 하단: `Sora's Pitfall Alert` (자주 저지르는 오답 유형 경고)

### 3.2. 엄격한 LaTeX 수식 표준화
- 모든 수식, 변수, 분수, 지수, 제곱근, 부등식, 좌표는 반드시 표준 LaTeX 문법(`$...$` 및 `$$...$$`)으로 렌더링합니다.
- 가독성을 위해 복잡한 분수는 `\dfrac{numerator}{denominator}`, 괄호는 `\left( ... \right)`를 사용합니다.
- 단계별 풀이 과정은 `\begin{aligned} ... \end{aligned}` 환경을 활용하여 등호($=$) 위치를 수직 정렬합니다.

---

## 4. 📅 45-LECTURE MASTER SEMESTER BLUEPRINT (15주 × 3회 = 45강 마스터 플랜)

- **총 강의 수:** 45강 (강의당 20~25분 분량, 각 강의당 10~15개 슬라이드)
- **Unit 1 (Weeks 1~5, 15 Lectures):** Foundations, Arithmetic Review, Polynomials, Linear Equations & Inequalities
- **Unit 2 (Weeks 6~10, 15 Lectures):** Cartesian Graphing, Linear Equations in Two Variables, Slope, Line Equations, Functions & Applications
- **Unit 3 (Weeks 11~15, 15 Lectures):** Quadratic Functions, Vertex, Solving via Square Root / GCF / Trinomial Factoring / Quadratic Formula, Graphing Parabolas

```mermaid
gantt
    title M090 15-Week / 45-Lecture Semester Schedule
    dateFormat  YYYY-MM-DD
    section Unit 1: Foundations & Linear Equations
    Week 1 (L01-L03) Arithmetic Review & Expressions :done, u1w1, 2026-09-01, 7d
    Week 2 (L04-L06) Exponents & Polynomials         :done, u1w2, after u1w1, 7d
    Week 3 (L07-L09) Multiplying & Rational Frac     :done, u1w3, after u1w2, 7d
    Week 4 (L10-L12) Solving Linear Equations        :done, u1w4, after u1w3, 7d
    Week 5 (L13-L15) Formulas, Inequalities & Exam 1 :done, u1w5, after u1w4, 7d
    section Unit 2: Graphing, Lines & Functions
    Week 6 (L16-L18) Intro to Graphing & Domain/Range:active, u2w1, after u1w5, 7d
    Week 7 (L19-L21) Slope-Intercept & Intercepts    :active, u2w2, after u2w1, 7d
    Week 8 (L22-L24) Slope & Point-Slope Form        :active, u2w3, after u2w2, 7d
    Week 9 (L25-L27) Writing Equations & Functions   :active, u2w4, after u2w3, 7d
    Week 10 (L28-L30) Function Notation & Modeling   :active, u2w5, after u2w4, 7d
    section Unit 3: Quadratic Functions & Equations
    Week 11 (L31-L33) Intro to Quadratics & Vertex   :crit, u3w1, after u2w5, 7d
    Week 12 (L34-L36) Square Root Property & GCF     :crit, u3w2, after u3w1, 7d
    Week 13 (L37-L39) Factoring Trinomials (Parts 1&2):crit, u3w3, after u3w2, 7d
    Week 14 (L40-L42) Quadratic Formula & Strategies :crit, u3w4, after u3w3, 7d
    Week 15 (L43-L45) Full Graphing & Final Mastery  :crit, u3w5, after u3w4, 7d
```

---

## 5. 📂 PROJECT DIRECTORY & ASSET PIPELINE

```
c:\Oikos Univ\Montana_State_Univ\
│
├── M090 Full Student Workbook.pdf      # 원본 워크북 교재 (93페이지 전량)
├── design_montana.md                   # [본 문서] 마스터 기획 및 시스템 설계 청사진
├── SYLLABUS_M090.md                    # 15주 45강 전체 상세 실라버스
├── CURRICULUM_45_LECTURES.md           # 45개 강의별 문항 매핑 및 슬라이드 배분표
│
├── lectures/                           # 45개 강의별 마크다운 대본 (LaTeX + 티키타카)
│   ├── lecture01.md                    # L01: Language of Algebra & PEMDAS
│   ├── lecture02.md                    # L02: Fraction Arithmetic & Signed Numbers
│   ├── ...                             # (L03 ~ L44)
│   └── lecture45.md                    # L45: Final Comprehensive Review & Wrap-up
│
├── scripts/                            # 데이터 처리 및 자동화 스크립트
│   ├── extract_workbook_problems.py    # 워크북 PDF에서 문항 및 LaTeX 수식 자동 파싱
│   ├── generate_lecture_markdown.py    # 파싱된 문항 기반 45강 티키타카 마크다운 생성
│   └── export_slides_data.py           # 웹 앱(React)용 slidesData.js 생성기
│
└── src_montana/ (또는 Web App 연동)     # 웹 인터랙티브 슬라이드 뷰어 컴포넌트
    ├── components/
    │   ├── MathSlide.jsx               # KaTeX 지원 단일 문항 슬라이드 뷰어
    │   ├── FormulaCard.jsx             # 공식 요약 카드
    │   └── TikiTakaDialogue.jsx        # 박은주 교수 & 소라 조교 대화 오디오 뷰어
    └── data/
        ├── montanaCurriculum.js        # 45강 커리큘럼 메타데이터
        └── montanaSlidesData.js        # 45강 전체 슬라이드 및 수식 데이터베이스
```

---

## 6. 💡 SUCCESS METRICS & PEDAGOGICAL IMPACT
1. **Pass Rate & Confidence:** 수학에 자신이 없던 발달수학 학생들의 시험 통과율 85% 이상 달성.
2. **Zero Confusion on Notation:** LaTeX 기반의 깔끔한 렌더링으로 칠판 필기 오독률 0% 달성.
3. **High Engagement Micro-Lectures:** 20~25분 단위 마이크로 러닝으로 학생 완강률 90% 이상 유지.
4. **Emotional Reassurance:** 조교 Sora의 질문과 박은주 교수의 자상한 해설을 통해 학습 스트레스 최소화.

---

## 7. 🚀 PRODUCTION DEPLOYMENT & PRESENTER SYNCHRONIZATION AUDIT REPORT (2026-10-02 완료)

### 7.1. 프로덕션 배포 현황
* **GitHub Repository:** [`https://github.com/marylatte11-svg/montana-lecture-app.git`](https://github.com/marylatte11-svg/montana-lecture-app.git) (`main` 브랜치)
* **Vercel Production Live URL:** [`https://montana-lecture-app.vercel.app/`](https://montana-lecture-app.vercel.app/)
* **최신 배포 커밋:**
  * `d1db895` — `fix(presenter): synchronize spoken teleprompter dialogue with exact workbook slide equations across all Unit 3 lectures`
  * `a27b65c` — `chore(audit): add all lecture slide audit tools and reports`
* **빌드 퍼포먼스:** Vite v8.2.0 프로덕션 번들 정상 컴파일 (1.10초 소요, 0 KaTeX Errors)

```mermaid
flowchart LR
    DEV["💻 Local Source<br/>(montanaSlidesData.js)"] -->|"git push main"| GH["🐙 GitHub Repo<br/>(marylatte11-svg)"]
    GH -->|"Auto Webhook"| VERCEL["⚡ Vercel Deployment<br/>(Edge Network)"]
    VERCEL --> LIVE["🌐 Live Production Site<br/>(montana-lecture-app.vercel.app)"]
```

---

### 7.2. 프리젠터 모드(Presenter Mode) UI 및 TTS 음성 엔진 고도화
1. **100% 영문 글로벌 UI 전환:**
   * 한국어 강의 가이드 탭 및 혼용 라벨 완전 제거.
   * `Pronounce Selection`, `Full Read-Aloud (Male Voice)`, `Key Vocabulary & Definitions` 등 100% 직관적인 영어 UI 구성.
2. **LaTeX 수식 구어체(Spoken English) 자동 변환 엔진 (`convertMathToSpokenEnglish`):**
   * 웹 브라우저 음성 합성(TTS)이 `$x$`, `$y$`, `$g(x)$`의 달러 기호를 "dollar sign x"로 읽지 않도록 필터링.
   * `$x^2$` ➔ *"x squared"*, `$\pm$` ➔ *"plus or minus"*, `$\sqrt{k}$` ➔ *"square root of k"* 등으로 자연스럽게 읽는 음성 전처리 적용.
3. **역할별 맞춤형 보컬 페르소나 (Vocal Personas):**
   * **👩‍🏫 Prof. Eunju Park (50대 여성 교수):** Pitch `0.82`, Rate `0.85` — 신뢰감 있고 차분하며 깊이 있는 아카데믹 톤.
   * **👩‍🎓 TA Sora (20대 중반 여성 조교):** Pitch `1.38`, Rate `1.05` — 톡톡 튀고 발랄하며 에너지 넘치는 리액션과 학생 꿀팁(Pro-Tip) 제시.
   * **🎙️ Full Read-Aloud (남성 내레이터):** Pitch `0.95`, Rate `0.92` — 명료하고 안정된 낭독 음성.

---

### 7.3. 45개 강의(361개 슬라이드) 전수 감사 및 슬라이드-대본 100% 동기화

#### 🔍 발견되었던 문제점 (Root Cause)
Unit 3의 슬라이드 문제들을 몬태나 주립대 Gallatin College 워크북의 최신 문제로 개정하는 과정에서, **슬라이드 화면은 개정 문제를 표시하고 있었으나 프리젠터 대본(Script)은 이전 템플릿의 다른 문제를 설명하는 불일치가 34개 슬라이드에서 발견됨.**
* *대표 사례:* **Lecture 43 Slide 2**에서 슬라이드는 $g(x) = x^2 + 6x$ (공통인수 인수분해)인데 대본은 $x^2 - 36 = 0$을 설명하고 있었음.

#### 🛠️ 수정 완료 내역 (34개 슬라이드 전수 교체)

| 단원/강의 | 수정 슬라이드 | 슬라이드 실제 수식 및 내용 | 수정된 프리젠터 텔레프롬프트 대화 |
|---|---|---|---|
| **L43 (Sec 3.6)** | **Slide 2** | $g(x) = x^2 + 6x$ | **GCF $x(x+6)=0$, 절편 $(0,0), (-6,0)$, 꼭짓점 $(-3,-9)$ 풀이 100% 동기화** |
| | **Slide 3** | $h(x) = -2x^2 + 5x + 6$ | 근의 공식 $x = \frac{-5 \pm \sqrt{73}}{-4}$, 꼭짓점 $(1.25, 9.13)$ 대화로 수정 |
| | **Slide 4** | $f(x) = 4x^2 - 28$ | 제곱근 성질 $x^2 = 7 \implies x = \pm\sqrt{7}$, 꼭짓점 $(0, -28)$ 대화로 수정 |
| | **Slide 5** | $f(x) = x^2 - 15x + 50$ | 인수분해 $(x-5)(x-10)=0$, 절편 $5, 10$, 꼭짓점 $(7.5, -6.25)$ 대화로 수정 |
| | **Slide 6** | $f(x) = -2(x-15)^2 + 50$ | 꼭짓점 $(15, 50)$, $x$-절편 $10, 20$, $y$-절편 $-400$ 대화로 수정 |
| **L41 (Sec 3.5)** | **Slide 3~7** | $x^2-5x-7$, $13x-x^2+1$, $-x^2-5x+7$, $2x^2-3x-1$, $3x^2-5x+7$ | 워크북 수식 및 근의 공식 전개, 함수값 평가에 정확히 일치하도록 교체 |
| **L44 (Sec 3.7)** | **Slide 2, 4, 5, 6, 7, 8** | $x^2+6x+5$, $2x^2-8x$, $-\frac{1}{2}(x+1)^2+8$, $f(-7)/g(-7)$, $f(x+5)$, $f(x)=g(x)$ | 5점 그래프법 및 합성/연립방정식 풀이로 전면 동기화 |
| **L31, L32, L33** | L31(S5, S6), L32(S2, S3), L33(S1~S6) | $f(x) = -2-3x+\frac{x^2}{3}$, $x^2-6x+5$, $g(x) = -x^2+2x+7$, $h(x) = 3(x-2)^2-4$ | 내림차순 정리, 절편과 대칭축, 대입 평가($g(a), g(x-6), h(k+1)$) 일치 |
| **L35, L36, L38, L40, L42, L45** | L35(S5, S6), L36(S5, S6), L38(S3), L40(S5), L42(S4), L45(S2) | $f(x) = -x^2-4x-5$, $x^2-36$, $3x^2-27$, $x^2+7x+12$, $2x^2+12x-10=0$, $x^2+2x+5$ | 판별식 음수($\Delta < 0$, 실근 없음), 계수 $a \neq 1$ 나눗셈 등 수학적 일치 |

---

### 7.4. 검증 결과 (Verification Proof)
* **실시간 브라우저 서브에이전트 검증:**
  * Lecture 43 Slide 2를 직접 방문하여 캡처 검증 완료 (`slide2_teleprompter_verified_1790885468528.png`).
  * 문제 화면($g(x) = x^2+6x$)과 텔레프롬프트 대화(TA Sora & Prof. Eunju Park의 $x(x+6)=0$ 풀이)가 완벽하게 일치함을 시각적으로 최종 확인.
* **프로덕션 가동 확인:**
  * Vercel 라이브 사이트 HTTP 요청 검증 결과 최신 번들 파일이 배포되어 사용자에게 정상 서비스 중임을 확인.

---

## 8. 🎬 RECORDLY MOTION VIDEO ENGINE & 2026-10-03 MASTER REVISIONS (최신 개편 완료)
> **종합 보고서 원문:** [MASTER_REVISION_SUMMARY_20261003.md](file:///c:/Oikos%20Univ/Montana_State_Univ/MASTER_REVISION_SUMMARY_20261003.md)  
> **비디오 연출 보고서:** [RECORDLY_VIDEO_ENGINE_REVISION_REPORT.md](file:///c:/Oikos%20Univ/Montana_State_Univ/RECORDLY_VIDEO_ENGINE_REVISION_REPORT.md)  
> **슬라이드-대본 조화원칙:** [SLIDE_SCRIPT_HARMONY_PRINCIPLES.md](file:///c:/Oikos%20Univ/Montana_State_Univ/SLIDE_SCRIPT_HARMONY_PRINCIPLES.md)

### 8.1. 4대 핵심 아키텍처 개선
1. **문제 문항 카드 2줄 분리 배치 (가로 스크롤 및 잘림 완벽 해결):**
   - 1행(문제 설명 텍스트) + 2행(독립 디스플레이 수식 `$$\mathbf{...}$$`) 분리로 가로 폭 초과 및 청록색 스크롤바 생성 문제를 근본적으로 해결.
2. **슬라이드-대본-음성 3위 1체 정합성 복원:**
   - Slide 2 번분수 오류($\frac{3/4}{5/8} \to \mathbf{\frac{5/8}{3/4} = \frac{5}{6}}$) 교정.
   - Slide 3, 4, 6 및 후속 슬라이드 대본을 워크북 원문($16-\frac{3}{4}+9=\frac{97}{4}$, $\frac{(16)(3)}{(9)(4)}=\frac{4}{3}$, $24\div4\cdot2=12$)으로 전수 동기화.
3. **수식 기호 무결성 복원:**
   - 근호(`√`) 및 복부호(`±`)가 자막 정규식에서 탈락되어 `$16=4$` 등으로 왜곡되던 현상을 원천 방지하는 특수 기호 보호 레이어 구축.
4. **조교 Sora 20대 보컬 페르소나 복원:**
   - `en-US-AriaNeural` (Pitch `+2Hz`, Rate `+4%`) 적용으로 상큼하고 발랄한 20대 대학생 멘토 보이스 확립.

### 8.2. 고화질 1080p 60fps 마스터 비디오 완성 현황
* **Lecture 01:** [MSU_M090_Lecture01_Full_Master.mp4](file:///c:/Oikos%20Univ/Montana_State_Univ/recordly_videos/Lecture01/MSU_M090_Lecture01_Full_Master.mp4) (10개 슬라이드 전편, 11분 3초, 83.21 MB)
* **Lecture 02:** [MSU_M090_Lecture02_Full_Master.mp4](file:///c:/Oikos%20Univ/Montana_State_Univ/recordly_videos/Lecture02/MSU_M090_Lecture02_Full_Master.mp4) (10개 슬라이드 전편, 13분 56초, 109.82 MB)
* **Lecture 36:** [MSU_M090_Lecture36_Full_Master.mp4](file:///c:/Oikos%20Univ/Montana_State_Univ/recordly_videos/Lecture36/MSU_M090_Lecture36_Full_Master.mp4) (8개 슬라이드 전편, 14분 59초, 96.28 MB)

