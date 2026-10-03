# 🎥 Recordly Autonomous Motion Video Generator Guide

[Recordly (GitHub: webadderallorg/Recordly)](https://github.com/webadderallorg/Recordly)의 핵심 연출 엔진(Screen Studio 스타일)을 기반으로, 강의 화면과 scripts 대본을 결합하여 **초고화질 1080p 모션 비디오**를 100% 전자동으로 생성하는 파이프라인 가이드입니다.

---

## ✨ 도입된 Recordly 핵심 연출 요소

1. **Auto-Zoom & Pan (지능형 오토 줌 & 카메라 트래킹)**
   - 대본(`scripts`)에서 설명하는 핵심 영역(왼쪽 카드, 오른쪽 솔루션, 수식, 그래프 등)을 분석하여 부드럽게 줌인(1.3x) 및 패닝합니다.
   - 슬라이드 전환 및 아웃트로 시 전체 화면(1.0x)으로 우아하게 줌아웃됩니다.

2. **Smooth Cursor & Ripple Effects (스튜디오 마우스 커서)**
   - 베지에 가감속 곡선을 그리며 설명 중인 UI 요소로 부드럽게 이동합니다.
   - 포커스 지점에 도달하면 미세한 파문(Ripple pulse) 클릭 효과가 발생하여 시선을 집중시킵니다.

3. **Studio Canvas & 3D Window Frame**
   - 1920x1080 전체 화면에 은은한 앰비언트 글로우 배경(Dark Slate & Aurora)을 제공합니다.
   - 슬라이드 창은 macOS 스타일 3색 트래픽 라이트, 부드러운 둥근 모서리(Border-radius), 깊이감 있는 3D 드롭 섀도우로 마감됩니다.

4. **Presenter Avatar Bubble (발화자 오버레이)**
   - 우측 하단 플로팅 글래스 버블에 현재 말하는 인물(Prof. Peter Kim, TA Sarah Jenkins, TA James Wilson)의 아바타와 이름 배지가 표시됩니다.
   - 발화 중에는 실시간 오디오 펄스 링(Pulsing soundwave ring)이 작동하여 생동감을 더합니다.

5. **Glassmorphic Floating Subtitles (글래스모피즘 자막)**
   - 발화자 이름 태그와 함께 또렷한 폰트로 대본 문장이 하단 중앙에 실시간 싱크되어 표시됩니다.

---

## 🚀 사용법 (Usage)

### 1. 단일 슬라이드 모션 비디오 생성
```bash
# Oikos Session 1의 Slide 8 영상 생성 (기본값)
python scripts/recordly_engine/render_recordly_video.py --session 1 --slide 8

# Oikos Session 1의 Slide 10 영상 생성
python scripts/recordly_engine/render_recordly_video.py --session 1 --slide 10
```

### 2. 선택한 슬라이드 복수 생성
```bash
# Slide 1, 8, 10번 영상 순차 생성
python scripts/recordly_engine/render_recordly_video.py --session 1 --slides 1,8,10
```

### 3. 세션 전체 일괄 생성
```bash
# Session 1의 모든 슬라이드 전체 자동 렌더링
python scripts/recordly_engine/render_recordly_video.py --session 1 --all
```

### 4. Montana State University M090 강의 슬라이드 생성
```bash
# Montana Lecture 1의 Slide 3 영상 생성
python scripts/recordly_engine/render_recordly_video.py --type montana --session 1 --slide 3
```

---

## 📁 산출물 디렉토리 (`c:\Oikos Univ\recordly_videos\`)
- 🎬 `Recordly_Session1_Slide_XX.mp4`: 1080p 25fps H.264 + AAC 고화질 Recordly 모션 비디오
- 🎵 `audio_segments/`: 발화자별 및 턴별 합성된 MP3 오디오 트랙
- 📸 `slide_images/`: 1920x1080 고해상도 슬라이드 캡처 원본
