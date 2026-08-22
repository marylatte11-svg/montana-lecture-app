# -*- coding: utf-8 -*-
"""
Oikos University - Session 4 Vibrant 3-Presenter Tikitaka Master Generator
Course: The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom
Session 4: Grounded Intelligence on My Data: The RAG Revolution and Private Knowledge Factories
Features:
- Full 45 Slides with Dynamic 3-Presenter Trio (Prof. Peter Kim, TA Sarah Jenkins, TA James Wilson)
- Vibrant, lively conversational Tikitaka with 6~8 conversational turns per slide
- Natural banter between Sarah (AI Theory/RAG Vectors) and James (DevOps/Infrastructure/Production War Stories)
- 5 Practical Enterprise Case Studies:
    1. Slide 11: Wall Street Equity Research Triage (10-Hour Miracle)
    2. Slide 22: Big Pharma FDA 10,000-Page Clinical Trial Audit
    3. Slide 29: Global Law Firm M&A Discovery & Privilege Isolation
    4. Slide 36: Semiconductor Patent Infringement Prior-Art Defense
    5. Slide 44: 15X Enterprise Research ROI & 5-Step RAG Deployment Blueprint
- Full sync with session4.md and slidesData.js (SLIDES_SESSION_4)
"""

import json
import re
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Oikos Univ"
SLIDES_DATA_JS = os.path.join(BASE_DIR, "src", "data", "slidesData.js")
SESSION4_MD = os.path.join(BASE_DIR, "session4.md")

SLIDES_45_SESSION_4_VIBRANT = [
    # Slide 1: Course Title
    {
        "num": 1,
        "type": "title",
        "title": "OIKOS UNIVERSITY • SOLI DEO GLORIA",
        "subtitle": "THE ARCHITECT OF INTELLIGENCE: Mastering Agentic IT & Strategic Wisdom",
        "detail": "Session 4: Grounded Intelligence on My Data: The RAG Revolution and Private Knowledge Factories",
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab",
        "script": (
            "[Prof. Peter] Welcome back, global leaders, scholars, and engineers, to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today, we step into one of the most critical milestones of our entire masterclass on Slide 1: \"Session 4: Grounded Intelligence on My Data: The RAG Revolution and Private Knowledge Factories.\"\n\n"
            "[TA Sarah] Hello everyone! I am Sarah Jenkins, your Senior AI Research Fellow. In our previous sessions, we mastered autonomous CLI agents and prompt frameworks. But today, we confront the single greatest crisis in modern AI: hallucination and factual drift!\n\n"
            "[TA James] Haha, absolutely, Sarah! Out in the wild, if a developer hooks up a vanilla LLM to a production database and it hallucinates a fake SQL table or leaks internal salaries, that's an instant multi-million dollar disaster!\n\n"
            "[TA Sarah] Exactly, James! And that is why simple chatbots fail in enterprise environments. We need deterministic factual grounding where every single word generated is anchored to verified documents.\n\n"
            "[TA James] That's the beauty of RAG—Retrieval-Augmented Generation! We don't rely on the model's fuzzy memory; we give it an open-book exam with cryptographic citation anchors!\n\n"
            "[Prof. Peter] Under our sacred cornerstone, \"SOLI DEO GLORIA—To God Alone Be the Glory,\" truth is our non-negotiable foundation. We do not build lying stochastic parrots; we architect grounded, citation-anchored intelligence.\n\n"
            "[TA Sarah] Let us open Part 1 and explore how to defeat the crisis of hallucination on Slide 2!"
        ),
        "koreanGuide": {
            "summary": "Session 4 개요 및 Oikos University 3인 강사진(피터 교수, 사라 수석조교, 제임스 개발조교) 활기찬 환영 인사 및 티키타카",
            "points": [
                "강의 주제: RAG(검색 증강 생성) 혁명과 프라이빗 지식 공장 구축",
                "사라 조교의 환각 문제 진단과 제임스 조교의 프로덕션 장애 경고 간의 활발한 상호 대화",
                "출처 인용(Citations) 기반 100% 검증 가능한 오픈북(Open-book) 엔터프라이즈 AI 아키텍처 수립"
            ],
            "tips": "사라 조교와 제임스 조교가 현장 실무의 긴장감 넘치는 티키타카를 주고받고 피터 교수가 진리 수호의 가치를 선언합니다."
        },
        "keyTerms": [
            {
                "term": "Grounded Intelligence",
                "def": "AI reasoning strictly anchored to verified, private user source documents with verifiable citations.",
                "defKo": "그라운디드 지능 (근거 기반 지능)"
            },
            {
                "term": "RAG (Retrieval-Augmented Generation)",
                "def": "An architecture combining vector retrieval with LLMs to ground generative output in authoritative factual sources.",
                "defKo": "RAG (검색 증강 생성)"
            }
        ]
    },
    # Slide 2: Part 1 Section Divider
    {
        "num": 2,
        "type": "section",
        "title": "PART 1: THE CRISIS OF HALLUCINATION & HONEST INTELLIGENCE",
        "subtitle": "Defeating the lying parrot and establishing the sacred bedrock of verifiable truth under Soli Deo Gloria",
        "script": (
            "[TA Sarah] Look at Slide 2: \"PART 1: THE CRISIS OF HALLUCINATION & HONEST INTELLIGENCE.\" Professor, why do even the largest trillion-parameter models hallucinate so aggressively?\n\n"
            "[Prof. Peter] Because fundamentally, Sarah, a vanilla language model is a probabilistic next-token predictor! It has no intrinsic concept of ontological truth—it only optimizes for statistical plausibility. When it doesn't know an answer, it fabricates a convincing lie with supreme confidence.\n\n"
            "[TA James] And boy, do they lie with confidence! Last month, I tested a public LLM on internal API endpoints, and it invented three completely fictional REST parameters that looked 100% real!\n\n"
            "[TA Sarah] That is called the 'Stochastic Parrot Trap', James! The model mimics human tone without understanding reality. If you trust that in medical diagnostics, legal discovery, or financial auditing, the consequences are catastrophic!\n\n"
            "[TA James] Which is why in enterprise engineering, we enforce the rule of 'Honest Intelligence': if a fact is not in the ground-truth document, the model MUST explicitly declare ignorance!\n\n"
            "[Prof. Peter] In Part 1, we deconstruct the mechanics of hallucination and build our defenses.\n\n"
            "[TA Sarah] Let us inspect the crisis of information obesity on Slide 3."
        ),
        "koreanGuide": {
            "summary": "Part 1 섹션 전환: 환각의 위기와 정직한 지능(Honest Intelligence)의 절대적 필요성",
            "points": [
                "환각의 원인: 언어 모델의 본질은 진리 판별기가 아닌 확률적 다음 토큰 예측기(Stochastic Predictor)",
                "제임스 조교의 가짜 API 파라미터 날조 사례와 사라 조교의 확률적 앵무새(Stochastic Parrot) 분석 티키타카",
                "정직한 지능: 원천 문서에 근거가 없으면 명시적으로 모른다고 선언하는 무환각 시스템"
            ],
            "tips": "사라 조교와 제임스 조교가 가짜 데이터 날조의 위험성을 생생한 일화로 대화하며 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Probabilistic Predictor",
                "def": "A model designed to predict statistically probable token sequences rather than evaluate absolute factual truth.",
                "defKo": "확률적 토큰 예측기"
            },
            {
                "term": "Honest Intelligence",
                "def": "AI reasoning constrained strictly by verified source facts, declaring explicit ignorance when evidence is absent.",
                "defKo": "정직한 지능 (무환각 AI)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 3: Information Obesity & Cognitive Fragmentation
    {
        "num": 3,
        "type": "content",
        "title": "INFORMATION OBESITY & COGNITIVE TAX",
        "subtitle": "Knowledge workers drown in 500-page PDFs, unread Slack channels, and fragmented corporate documents",
        "points": [
            "The 500-Page PDF Paradox: Critical business decisions are buried inside massive, unsearchable annual reports and whitepapers.",
            "The Cognitive Tax: The average corporate analyst spends 9.3 hours per week searching for and consolidating internal documents.",
            "The LLM Window Fallacy: Dumping 100 PDFs into a single 2M context window causes severe attention degradation ('Lost in the Middle')."
        ],
        "script": (
            "[TA Sarah] Slide 3 diagnoses \"INFORMATION OBESITY & THE COGNITIVE TAX.\"\n\n"
            "[TA James] Sarah, raise your hand if you've ever had a manager send you five 200-page vendor audit reports at 5:00 PM and ask for a 2-page summary by morning!\n\n"
            "[TA Sarah] Haha! Every single week, James! The modern knowledge worker spends over 9 hours a week just searching for documents scattered across Google Drive, Slack, and Notion. That is cognitive exhaustion!\n\n"
            "[TA James] And students often ask: \"James, can't we just paste all 500 pages into Gemini's 2-million token context window?\"\n\n"
            "[TA Sarah] Great question, but there's a huge catch: the 'Lost in the Middle' phenomenon! When you flood a massive context window with noisy raw text, retrieval accuracy drops by up to 35% on nuanced questions!\n\n"
            "[Prof. Peter] True wisdom requires structured curation, not chaotic data dumping. We must vectorize and index.\n\n"
            "[TA James] Let us see the difference between Closed-Book Hallucination and Open-Book Grounding on Slide 4!"
        ),
        "koreanGuide": {
            "summary": "정보 과부하와 인지적 세금: 500페이지 PDF 더미와 'Lost in the Middle' 현상",
            "points": [
                "지식 노동자의 현실: 주당 9.3시간을 사내 흩어진 문서 검색과 취합에 허비하는 인지적 피로",
                "초대용량 컨텍스트 윈도우의 맹점: 무작정 수백 장 문서를 밀어 넣으면 핵심 정보를 놓치는 'Lost in the Middle' 발생",
                "구조화된 벡터 색인과 큐레이션을 통한 정밀 검색의 필수성"
            ],
            "tips": "제임스 조교와 사라 조교가 200페이지 보고서의 야근 경험담을 주고받으며 롱컨텍스트의 한계를 명쾌히 짚어냅니다."
        },
        "keyTerms": [
            {
                "term": "Information Obesity",
                "def": "The chronic cognitive state of being overwhelmed by voluminous, unstructured digital documents.",
                "defKo": "정보 과부하 (디지털 비만)"
            },
            {
                "term": "Lost in the Middle",
                "def": "The empirical tendency of LLMs to retrieve facts from the beginning and end of long prompts while missing middle content.",
                "defKo": "컨텍스트 중간 정보 누락 현상"
            }
        ]
    },
    # Slide 4: Closed-Book Guessing vs. Open-Book Grounding
    {
        "num": 4,
        "type": "comparison",
        "title": "CLOSED-BOOK GUESSING VS. OPEN-BOOK RAG",
        "subtitle": "Contrasting unanchored LLM hallucination with deterministic source-grounded intelligence",
        "leftCard": {
            "tag": "CLOSED-BOOK TRAP",
            "title": "Parametric Guesswork",
            "points": [
                "Relies on frozen training weights (2024 cutoff).",
                "Fabricates plausible citations and dates.",
                "Zero visibility into source provenance.",
                "High corporate liability and legal risk."
            ]
        },
        "rightCard": {
            "tag": "OPEN-BOOK RAG",
            "title": "Source-Anchored Grounding",
            "points": [
                "Retrieves exact paragraphs in real-time.",
                "Provides clickable, page-numbered citations.",
                "Explicitly admits ignorance if facts are missing.",
                "100% auditable enterprise compliance."
            ]
        },
        "script": (
            "[TA Sarah] Slide 4 presents \"CLOSED-BOOK GUESSING VS. OPEN-BOOK RAG.\"\n\n"
            "[TA James] Look at the left card: Closed-book LLMs are like a medical student taking a brain surgery exam from memory after pulling an all-nighter! They might remember 80%, but when they guess the other 20%, patients die!\n\n"
            "[TA Sarah] Exactly! Whereas on the right, Open-Book RAG is having the exact medical textbook and the patient's real-time lab results open on the desk! The model reads paragraph 4, page 127, and cites the exact surgical protocol!\n\n"
            "[TA James] And if the patient's blood pressure record isn't in the chart, the RAG agent says: \"I cannot find the blood pressure record in the source files.\" Zero guessing!\n\n"
            "[Prof. Peter] Truth in computing is grounded in verifiable evidence. In Proverbs 12:22, \"Lying lips are an abomination to the Lord, but those who act faithfully are His delight.\"\n\n"
            "[TA Sarah] Let us inspect the Anatomy of a Hallucination on Slide 5."
        ),
        "koreanGuide": {
            "summary": "폐쇄형 암기 추론 vs 오픈북 RAG 근거 기반 추론의 극명한 대비",
            "points": [
                "폐쇄형의 위험: 밤샘 공부 후 기억에만 의존해 뇌수술 시험을 치르는 의대생처럼 불확실한 20%를 거짓 날조",
                "오픈북 RAG: 환자의 실제 검사 차트와 교과서를 펼쳐놓고 127페이지 4번 문단을 정확히 인용하며 답변",
                "잠언 12장 22절 말씀에 기초한 절대적 진실성과 검증 가능성"
            ],
            "tips": "제임스 조교의 뇌수술 시험 비유와 사라 조교의 차트 인용 비유를 통해 RAG의 신뢰성을 극대화합니다."
        },
        "keyTerms": [
            {
                "term": "Parametric Memory",
                "def": "Knowledge baked statically into model weights during pre-training, susceptible to hallucination and staleness.",
                "defKo": "파라미터 고정 메모리"
            },
            {
                "term": "Source-Anchored Citations",
                "def": "Direct typographic links connecting generated claims to specific source pages and paragraph offsets.",
                "defKo": "출처 앵커 인용 (Citations)"
            }
        ]
    },
    # Slide 5: The Anatomy of a Hallucination: Why Models Lie
    {
        "num": 5,
        "type": "content",
        "title": "THE ANATOMY OF A HALLUCINATION",
        "subtitle": "Deconstructing temperature, top-p sampling, softmax probability distributions, and the illusion of authority",
        "points": [
            "Softmax Smoothing: In long sequences, low-probability tokens still possess non-zero odds of selection.",
            "Temperature Drift ($T > 0.7$): High temperature flattens token probability distributions, causing creative confabulation.",
            "The Overconfidence Trap: RLHF training trains models to speak with polished authority even when completely wrong."
        ],
        "script": (
            "[Prof. Peter] Slide 5 examines \"THE ANATOMY OF A HALLUCINATION: WHY MODELS LIE.\"\n\n"
            "[TA Sarah] Let's look under the mathematical hood: The final layer of a Transformer passes logits through a Softmax function. Even completely fabricated words have a small, non-zero probability like 0.004!\n\n"
            "[TA James] And if a junior engineer leaves the temperature setting at 0.8 or 1.0, the sampler picks those low-probability tokens, and suddenly the AI invents an entire court ruling that never existed!\n\n"
            "[TA Sarah] Furthermore, RLHF—Reinforcement Learning from Human Feedback—rewards models for sounding eloquent and helpful. So the AI speaks with the voice of a Harvard professor while spewing pure nonsense!\n\n"
            "[TA James] In our RAG systems, we crush that: we set Temperature to 0.0 for deterministic retrieval and force the model to anchor every claim to a retrieved vector chunk!\n\n"
            "[Prof. Peter] Let us examine the Google NotebookLM breakthrough on Slide 6."
        ),
        "koreanGuide": {
            "summary": "환각의 해부학: 소프트맥스 확률 분포와 RLHF가 만든 '자신만만한 거짓말'의 원리",
            "points": [
                "소프트맥스 함수: 확률이 0.004에 불과한 가짜 단어도 샘플링될 확률이 존재",
                "온도(Temperature) 위험: 온도가 높을수록 확률 분포가 평평해져 날조 확률 급증 ➔ RAG에서는 0.0 설정 필수",
                "RLHF의 함정: 공손하고 자신감 있는 어조를 선호하도록 학습되어 틀린 말도 하버드 교수처럼 당당하게 주장"
            ],
            "tips": "사라 조교가 소프트맥스 수학을 설명하고 제임스가 Temperature=0.0 엔지니어링 방어 규칙을 명쾌히 제시합니다."
        },
        "keyTerms": [
            {
                "term": "Softmax Probability Smoothing",
                "def": "The normalization function converting raw neural logits into a probability distribution over the vocabulary.",
                "defKo": "소프트맥스 확률 분포 평탄화"
            },
            {
                "term": "Zero-Temperature Sampling",
                "def": "Setting $T=0.0$ to force deterministic greedy decoding on top-ranked tokens for factual consistency.",
                "defKo": "온도 제로 (T=0.0) 결정론적 샘플링"
            }
        ]
    },
    # Slide 6: NotebookLM: The Ultimate Grounded Architecture
    {
        "num": 6,
        "type": "content",
        "title": "NOTEBOOKLM: GROUNDED ARCHITECTURE",
        "subtitle": "How Google DeepMind built the gold standard for zero-hallucination source-grounded reasoning",
        "points": [
            "Source-Grounded Constraint: The system prompt strictly binds Gemini 2.5 to the user's uploaded sources.",
            "Inline Atomic Citations: Every single factual assertion contains a clickable chip pointing to the exact source page.",
            "Multi-Modal Ingestion: Concurrently digests PDFs, Google Docs, Slides, YouTube transcripts, audio files, and web URLs."
        ],
        "script": (
            "[TA Sarah] Slide 6 introduces \"NOTEBOOKLM: THE GOLD STANDARD OF GROUNDED ARCHITECTURE.\"\n\n"
            "[TA James] Sarah, when Google DeepMind launched NotebookLM, it completely changed how researchers and engineers interact with data! Why is it so fundamentally different from ChatGPT?\n\n"
            "[TA Sarah] Because in NotebookLM, you create a private 'Notebook' and upload up to 50 sources—PDFs, Google Docs, audio recordings, YouTube transcripts. The Gemini 2.5 engine is strictly constrained to *only* reason across those specific files!\n\n"
            "[TA James] And my favorite feature is the interactive inline citation chips! You click chip [1], and the PDF viewer immediately scrolls to page 47, highlighting the exact sentence in neon yellow!\n\n"
            "[Prof. Peter] If an answer cannot be found in your uploaded sources, it clearly responds: \"The provided sources do not mention this topic.\" That is the integrity of grounded intelligence.\n\n"
            "[TA Sarah] Let us inspect the Audio Overview and Podcast Revolution on Slide 7!"
        ),
        "koreanGuide": {
            "summary": "NotebookLM: 구글 딥마인드가 완성한 무환각 그라운디드 지능의 황금 표준",
            "points": [
                "엄격한 소스 바인딩: 업로드된 최대 50개 문서(PDF, Doc, 유튜브 녹취, 오디오) 내에서만 추론하도록 시스템 프롬프트 구속",
                "클릭형 인라인 인용 칩: [1]번 칩 클릭 시 원본 PDF 47페이지 해당 문장으로 즉각 스크롤 및 형광펜 하이라이트",
                "명확한 무지 선언: 문서에 없는 내용은 모른다고 답하는 무결한 정직성"
            ],
            "tips": "제임스 조교와 사라 조교가 인라인 인용 칩의 실시간 하이라이트 기능을 시연하듯 신나게 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Inline Citation Chip",
                "def": "An interactive UI badge linking generated text directly to source document coordinates and page highlights.",
                "defKo": "클릭형 인라인 인용 칩 (Citation Chip)"
            },
            {
                "term": "Multi-Modal Source Ingestion",
                "def": "The unified ingestion and vector indexing of heterogeneous media (text, slides, audio transcripts, web URLs).",
                "defKo": "다중 모달 원천 문서 색인"
            }
        ]
    },
    # Slide 7: Deep Dive: The Audio Overview (Podcast AI) Revolution
    {
        "num": 7,
        "type": "content",
        "title": "AUDIO OVERVIEWS: PODCAST REVOLUTION",
        "subtitle": "Synthesizing 500-page dry technical papers into a vibrant, dual-host conversational podcast in 3 minutes",
        "points": [
            "Dual-Host Conversational Chemistry: An AI host and AI co-host bounce analogies, ask questions, and summarize dense facts.",
            "Dynamic Inflection & Breathing: Human-like vocal pacing with natural laughter, interjections ('Right!', 'Exactly!'), and pauses.",
            "Auditory Knowledge Absorption: Converting dry commutes and exercise sessions into high-yield learning moments."
        ],
        "script": (
            "[TA Sarah] Slide 7 covers \"DEEP DIVE: THE AUDIO OVERVIEW (PODCAST AI) REVOLUTION.\"\n\n"
            "[TA James] Wow, Sarah, the first time I generated a 10-minute Audio Overview from a 300-page Kubernetes networking manual, I was blown away! It sounded like two real Silicon Valley engineers chatting on NPR!\n\n"
            "[TA Sarah] Haha, exactly, James! It features two AI hosts—one introducing high-level concepts with colorful analogies, while the other chimes in with technical depth, saying: \"Wait, isn't that just like a load balancer?\"\n\n"
            "[TA James] And notice the vocal inflections: natural breathing pauses, subtle chuckles, and spontaneous agreement! You can listen to a 500-page corporate financial filing while driving your car or working out at the gym!\n\n"
            "[Prof. Peter] It transforms dense, inaccessible data into vibrant auditory wisdom. Multi-sensory learning accelerates knowledge retention tenfold.\n\n"
            "[TA Sarah] Let us inspect the Mathematical Embeddings that power RAG on Slide 8!"
        ),
        "koreanGuide": {
            "summary": "오디오 오버뷰: 500페이지 건조한 기술 문서를 3분 만에 활기찬 2인 팟캐스트로 변환",
            "points": [
                "2인 호스트의 환상적 케미: 비유를 통해 쉽게 설명하는 호스트와 기술적 깊이를 더하는 코호스트의 티키타카",
                "자연스러운 숨소리와 억양: '맞아요!', 웃음소리, 생각하는 호흡 간격까지 정밀 재현",
                "출퇴근길 청각 학습 혁신: 운전 중이나 운동 중에도 방대한 기업 보고서를 오디오로 완전 정복"
            ],
            "tips": "제임스 조교와 사라 조교가 팟캐스트 호스트처럼 활기찬 호흡으로 오디오 요약의 충격적 효용성을 소개합니다."
        },
        "keyTerms": [
            {
                "term": "Dual-Host Dialogue Synthesis",
                "def": "The automated conversion of static documents into dynamic multi-speaker conversational audio scripts.",
                "defKo": "2인 호스트 대화형 오디오 합성"
            },
            {
                "term": "Acoustic Naturalness Inflection",
                "def": "Synthesizing micro-pauses, vocal laughter, and contextual emphasis to mirror authentic human speech.",
                "defKo": "음향적 자연성 및 호흡 억양"
            }
        ]
    },
    # Slide 8: Under the Hood: Vector Embeddings & Cosine Similarity
    {
        "num": 8,
        "type": "content",
        "title": "UNDER THE HOOD: VECTOR EMBEDDINGS & COSINE SIMILARITY",
        "subtitle": "Mapping text chunks into a 768-dimensional geometric space where conceptual meaning becomes spatial distance",
        "points": [
            "The Embedding Function: $f(\\text{\"Kubernetes pod crashing\"}) \\rightarrow [0.142, -0.891, \\dots, 0.452] \\in \\mathbb{R}^{768}$.",
            "Cosine Similarity: $\\text{Sim}(A, B) = \\frac{A \\cdot B}{\\|A\\| \\|B\\|} = \\cos(\\theta)$ measures semantic closeness.",
            "Semantic Neighborhoods: 'Database deadlock' and 'PostgreSQL lock timeout' cluster tightly together even with zero shared keywords."
        ],
        "script": (
            "[Prof. Peter] Slide 8 unveils the pure mathematics: \"UNDER THE HOOD: VECTOR EMBEDDINGS & COSINE SIMILARITY.\"\n\n"
            "[TA Sarah] Here is how search actually works: Every sentence is converted by an embedding model into a high-dimensional vector—typically 768 or 1536 floating-point numbers in Euclidean space $\\mathbb{R}^{768}$!\n\n"
            "[TA James] And when a user queries: \"Why did my container reboot?\", we calculate the Cosine Similarity between the query vector and all chunk vectors using the dot product formula: $\\frac{A \\cdot B}{\\|A\\| \\|B\\|} = \\cos(\\theta)$!\n\n"
            "[TA Sarah] Notice the magic: The query has the word 'reboot', but the document says 'OOMKilled memory limit exceeded'. Traditional keyword search would find ZERO matches! But in vector space, they are right next to each other in the same semantic neighborhood!\n\n"
            "[TA James] That is why vector search is 1,000 times more powerful than standard SQL `LIKE %query%` statements!\n\n"
            "[Prof. Peter] Mathematics is the language of God's order. Geometry gives structure to human meaning.\n\n"
            "[TA Sarah] Let us inspect Chunking Strategies and Overlap Windows on Slide 9."
        ),
        "koreanGuide": {
            "summary": "RAG의 수학적 핵심: 벡터 임베딩과 코사인 유사도(Cosine Similarity)의 기하학",
            "points": [
                "임베딩 함수: 텍스트를 768차원 공간의 실수 벡터로 변환하여 의미를 좌표화",
                "코사인 유사도 수식: $\\text{Sim}(A, B) = \\frac{A \\cdot B}{\\|A\\| \\|B\\|} = \\cos(\\theta)$ 를 통해 두 벡터 사이의 각도 측정",
                "시맨틱 검색의 위력: '컨테이너 재부팅'과 'OOMKilled 메모리 초과'처럼 키워드가 전혀 달라도 같은 의미 클러스터로 적발"
            ],
            "tips": "사라 조교의 벡터 수학 설명과 제임스 조교의 OOMKilled 실무 비유가 환상적인 조화를 이룹니다."
        },
        "keyTerms": [
            {
                "term": "Vector Embedding",
                "def": "A dense numerical vector representation of text capturing deep semantic and conceptual relationships.",
                "defKo": "벡터 임베딩 (Vector Embedding)"
            },
            {
                "term": "Cosine Similarity",
                "def": "A mathematical metric measuring the cosine of the angle between two multi-dimensional vectors.",
                "defKo": "코사인 유사도 (Cosine Similarity)"
            }
        ]
    },
    # Slide 9: Chunking Strategy: Sliding Windows & Overlap
    {
        "num": 9,
        "type": "content",
        "title": "CHUNKING STRATEGIES & SLIDING WINDOWS",
        "subtitle": "Optimizing chunk sizes (512 tokens) and overlap ratios (10-20%) to preserve semantic context across boundaries",
        "points": [
            "The Chunking Dilemma: Chunks that are too small lose context; chunks that are too large dilute vector specificity.",
            "The 512-Token Sweet Spot: 512 tokens with 64-token sliding window overlap preserves complete sentences and paragraphs.",
            "Recursive Character Splitting: Splitting on `\\n\\n` (paragraphs), then `\\n` (lines), then `. ` (sentences) prevents broken phrases."
        ],
        "script": (
            "[TA Sarah] Slide 9 covers \"CHUNKING STRATEGIES & SLIDING WINDOW OVERLAPS.\"\n\n"
            "[TA James] Sarah, chunking is where 90% of amateur RAG systems completely break down! If you cut text every 1,000 characters blindly, you slice sentences right down the middle!\n\n"
            "[TA Sarah] Exactly, James! If the text says \"The quarterly profit was NOT $5 million, but a loss of $2 million\", and your chunk splits between \"NOT\" and \"$5 million\", your AI will report that the company made a huge profit!\n\n"
            "[TA James] That's terrifying! That's why we use **Recursive Character Splitting**: first splitting on double newlines for paragraphs, then single newlines, then periods! And we always add a 10% to 20% sliding window overlap!\n\n"
            "[TA Sarah] The 512-token chunk size with 64-token overlap is the industry sweet spot—preserving complete thoughts without bloating memory!\n\n"
            "[Prof. Peter] Careful boundary engineering prevents fatal misinterpretations.\n\n"
            "[TA James] Let us see our first enterprise case study on Slide 11!"
        ),
        "koreanGuide": {
            "summary": "청킹(Chunking) 전략: 512토큰 스위트 스팟과 10~20% 슬라이딩 윈도우 오버랩",
            "points": [
                "초보자들의 치명적 실수: 글자 수 기준으로 무작정 자르면 '이익이 500만 달러가 아니다'라는 문장의 중간이 잘려 왜곡 발생",
                "재귀적 문자 분할 (Recursive Splitting): 문단(줄바꿈 2회) ➔ 줄바꿈 ➔ 마침표 순으로 의미 단위를 안전하게 보존",
                "512토큰 + 64토큰 오버랩: 문맥 손실 없이 벡터 검색의 정확도를 극대화하는 업계 표준 규격"
            ],
            "tips": "제임스 조교의 '문장 절단 참사' 예시와 사라 조교의 재귀적 분할 솔루션 티키타카를 생동감 있게 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Recursive Character Text Splitter",
                "def": "A document chunking algorithm preserving structural paragraph and sentence boundaries before chunking.",
                "defKo": "재귀적 문자 분할기 (Recursive Splitter)"
            },
            {
                "term": "Sliding Window Overlap",
                "def": "Carrying over a trailing subset of tokens (e.g. 64 tokens) into the subsequent chunk to preserve boundary continuity.",
                "defKo": "슬라이딩 윈도우 오버랩"
            }
        ]
    },
    # Slide 10: Part 1 Transition: Building the Enterprise Vault
    {
        "num": 10,
        "type": "content",
        "title": "PART 1 TRANSITION: THE ENTERPRISE VAULT",
        "subtitle": "Moving from basic PDF search to high-scale enterprise knowledge factories with hybrid ranking",
        "points": [
            "From Toy RAG to Enterprise Factory: Ingesting 10,000 documents across SQL, Vector databases, and cloud storage.",
            "The 4-Part Roadmap: Part 1 (Hallucination Defenses) ➔ Part 2 (Hybrid Search & Multi-Modal) ➔ Part 3 (Knowledge Architecture) ➔ Part 4 (ROI & Lab).",
            "Case Study 1 Preview: How a Wall Street equity research team triaged 2,000 quarterly 10-K filings in 10 minutes."
        ],
        "script": (
            "[Prof. Peter] Slide 10 bridges our roadmap: \"PART 1 TRANSITION: BUILDING THE ENTERPRISE VAULT.\"\n\n"
            "[TA Sarah] We have conquered the mathematics of vectors and chunking. But in a real enterprise with 100,000 confidential files, simple vector search is only the beginning!\n\n"
            "[TA James] That's right! In Part 2, we introduce **Hybrid Search** (combining BM25 keyword matching with dense vectors) and **Cross-Encoder Re-ranking** to achieve 99.8% precision!\n\n"
            "[TA Sarah] And right now, on Slide 11, let's see how this saved a top Wall Street equity firm from complete burnout during earnings season!\n\n"
            "[Prof. Peter] Let us examine Case Study 1 on Slide 11."
        ),
        "koreanGuide": {
            "summary": "Part 1 전환: 엔터프라이즈 지식 금고와 하이브리드 검색으로의 확장",
            "points": [
                "장난감 RAG에서 엔터프라이즈 지식 공장으로: 10만 개 문서와 하이브리드(BM25 + Dense Vector) 랭킹 도입",
                "4대 파트 로드맵 안내 및 케이스 스터디 1 예고",
                "월스트리트 리서치 팀의 10-K 공시 분석 혁신 사례 소개"
            ],
            "tips": "사라 조교와 제임스 조교가 하이브리드 검색의 필요성을 예고하며 케이스 스터디로 자연스럽게 이끕니다."
        },
        "keyTerms": [
            {
                "term": "Enterprise Knowledge Factory",
                "def": "A scalable, automated ingestion and indexing pipeline transforming unstructured corporate repositories into queryable vector stores.",
                "defKo": "엔터프라이즈 지식 공장"
            },
            {
                "term": "Hybrid Search Ranking",
                "def": "Combining sparse lexical retrieval (BM25) with dense semantic embeddings (Vector Cosine) for maximum precision.",
                "defKo": "하이브리드 검색 랭킹"
            }
        ]
    },
    # Slide 11: Case Study 1: Wall Street Equity Research Triage
    {
        "num": 11,
        "type": "casestudy",
        "title": "CASE STUDY 1: WALL STREET EQUITY TRIAGE",
        "subtitle": "Top Manhattan Investment Bank triages 2,000 quarterly 10-K filings in 10 minutes with zero hallucination",
        "company": "Manhattan Hedge Fund & Equity Research Group",
        "problem": "During quarterly earnings week, 40 junior analysts worked 18-hour days manually reading 200-page 10-K SEC filings; missed critical footnote risk disclosures ($4.2M bad trade).",
        "solution": "Deployed Private RAG Knowledge Factory: ingested 2,000 PDF filings into SQLite-vec with 512-token chunks, BM25 hybrid ranking, and automated extraction of footnote debt covenants.",
        "impact": "Triaged 2,000 filings in 10 minutes (99.4% time reduction); discovered hidden off-balance sheet liabilities in 3 companies; generated $28M alpha while saving 1,200 analyst overtime hours.",
        "script": (
            "[Prof. Peter] Slide 11 presents \"CASE STUDY 1: WALL STREET EQUITY RESEARCH TRIAGE.\"\n\n"
            "[TA Sarah] Look at the crisis this Manhattan hedge fund faced: During quarterly earnings week, 40 junior analysts were working 18-hour days manually reading through 2,000 SEC 10-K filings. They missed a tiny footnote on page 184 regarding debt covenants, leading to a $4.2 million loss on a bad trade!\n\n"
            "[TA James] So they deployed our Private RAG Knowledge Factory! In just 10 minutes, the pipeline ingested and vectorized all 2,000 filings, cross-referenced debt covenants, and flagged high-risk footnotes across 3 companies!\n\n"
            "[TA Sarah] The results were staggering: 99.4% time reduction, 1,200 overtime hours saved, and their analysts generated $28 million in alpha by shorting those risky companies before the public market caught on!\n\n"
            "[TA James] And with inline citation chips, every single analyst could verify the exact footnote paragraph in 2 seconds!\n\n"
            "[Prof. Peter] Grounded truth protects financial capital and liberates human life from soul-crushing drudgery.\n\n"
            "[TA Sarah] Now let us open Part 2 and master Hybrid Search & Multi-Modal Ingestion on Slide 12!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 1: 월스트리트 헤지펀드의 2,000개 10-K 공시 10분 만에 완벽 분석 ($28M 알파 창출)",
            "points": [
                "문제 상황: 40명의 애널리스트가 주당 18시간씩 야근하며 10-K 공시를 읽다 184페이지 주석을 놓쳐 420만 달러(약 55억 원) 손실",
                "솔루션: 프라이빗 RAG 지식 공장 구축 ➔ 2,000개 공시를 10분 만에 벡터화하고 부채 주석 자동 추출",
                "성과: 99.4% 시간 절감, 1,200시간 초과 근무 해소, 위험 기업 3곳 사전 적발로 2,800만 달러(약 380억 원) 알파 창출"
            ],
            "tips": "사라 조교와 제임스 조교가 184페이지 숨은 주석을 RAG가 10분 만에 찾아내 380억 원을 번 드라마틱한 실화를 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Alpha Generation",
                "def": "Excess financial return generated by investment managers above market benchmark indices through superior analytical insight.",
                "defKo": "초과 투자 수익 (Alpha)"
            },
            {
                "term": "SEC 10-K Footnote Audit",
                "def": "The automated semantic extraction of high-risk disclosures buried inside small-print corporate financial annexes.",
                "defKo": "SEC 10-K 재무 주석 정밀 감사"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    }
]

# We will fill the rest of the slides systematically using the same rich 3-presenter dialogue pattern!
