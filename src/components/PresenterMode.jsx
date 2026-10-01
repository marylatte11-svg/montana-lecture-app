import React, { useState, useEffect } from 'react';
import { renderInlineMathAndBold } from './slides/MathRenderer';
import { 
  X, 
  Play, 
  Pause, 
  RotateCcw, 
  ChevronLeft, 
  ChevronRight, 
  BookOpen, 
  Clock, 
  Volume2,
  VolumeX,
  Globe,
  Type,
  CheckCircle2,
  Lightbulb,
  Sparkles
} from 'lucide-react';

/**
 * Converts mathematical formulas, LaTeX markup, and markdown in spoken script
 * into clean, natural spoken English for the TTS engine.
 * Prevents TTS from pronouncing raw symbols like "dollar sign x dollar sign".
 */
export function convertMathToSpokenEnglish(text) {
  if (!text) return '';

  let spoken = text;

  // 1. Currency: \$1,500 or $1500 -> "1,500 dollars"
  spoken = spoken.replace(/\\?\$(\d[\d,]*(?:\.\d+)?)/g, '$1 dollars');

  // 2. Common LaTeX math symbols & fractions
  spoken = spoken
    .replace(/\\(?:d?frac)\{([^}]+)\}\{([^}]+)\}/g, '$1 over $2')
    .replace(/\\sqrt\{([^}]+)\}/g, 'the square root of $1')
    .replace(/\\sqrt\[(\d+)\]\{([^}]+)\}/g, 'the $1th root of $2')
    .replace(/\\cdot/g, ' times ')
    .replace(/\\times/g, ' times ')
    .replace(/\\div/g, ' divided by ')
    .replace(/\\pm/g, ' plus or minus ')
    .replace(/\\neq/g, ' is not equal to ')
    .replace(/\\approx/g, ' is approximately ')
    .replace(/\\leq?/g, ' is less than or equal to ')
    .replace(/\\geq?/g, ' is greater than or equal to ')
    .replace(/\\mathbb\{R\}/g, 'the real numbers')
    .replace(/\\mathbb\{Z\}/g, 'the integers')
    .replace(/\\mathbb\{Q\}/g, 'the rational numbers')
    .replace(/\\mathbb\{N\}/g, 'the natural numbers')
    .replace(/\\pi/g, 'pi')
    .replace(/\\circ/g, ' degrees ')
    .replace(/\\text\{([^}]+)\}/g, ' $1 ')
    .replace(/\\quad/g, ' ')
    .replace(/\\;/g, ' ')
    .replace(/\\\\/g, '. ');

  // 3. Absolute value: |-8| -> "the absolute value of -8"
  spoken = spoken.replace(/\|([^|]+)\|/g, 'the absolute value of $1');

  // 4. Exponents: x^2 -> x squared, x^3 -> x cubed, x^n -> x to the n
  spoken = spoken
    .replace(/([a-zA-Z0-9\(\)]+)\^2\b/g, '$1 squared')
    .replace(/([a-zA-Z0-9\(\)]+)\^3\b/g, '$1 cubed')
    .replace(/([a-zA-Z0-9\(\)]+)\^{?([a-zA-Z0-9\+\-]+)}?/g, '$1 to the $2');

  // 5. Clean remaining inline math markers ($...$) -> just content without dollar signs
  spoken = spoken.replace(/\$([^$]+)\$/g, ' $1 ');

  // 6. Clean markdown formatting (**bold**, *italic*)
  spoken = spoken
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/\*([^*]+)\*/g, '$1');

  // 7. Clean residual backslashes or braces
  spoken = spoken
    .replace(/\\[a-zA-Z]+/g, ' ')
    .replace(/[{}\\]/g, ' ');

  // 8. Normalise spaces and clean repeated punctuation
  spoken = spoken.replace(/\s+/g, ' ').trim();

  return spoken;
}


export default function PresenterMode({ 
  slideData, 
  nextSlideData,
  currentSlide, 
  totalSlides, 
  onPrev, 
  onNext, 
  onClose 
}) {
  // Timer State
  const [seconds, setSeconds] = useState(0);
  const [isActive, setIsActive] = useState(true);
  const [activeTab, setActiveTab] = useState('script'); // 'script' | 'korean' | 'terms'
  const [fontSize, setFontSize] = useState('text-base'); // 'text-sm' | 'text-base' | 'text-lg' | 'text-xl'
  const [speakingText, setSpeakingText] = useState(null);

  useEffect(() => {
    let interval = null;
    if (isActive) {
      interval = setInterval(() => {
        setSeconds(s => s + 1);
      }, 1000);
    } else if (!isActive && seconds !== 0) {
      clearInterval(interval);
    }
    return () => clearInterval(interval);
  }, [isActive, seconds]);

  // Cancel TTS when switching slides or closing
  useEffect(() => {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      setSpeakingText(null);
    }
  }, [currentSlide, onClose]);

  const formatTime = (totalSeconds) => {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const handleResetTimer = () => {
    setSeconds(0);
    setIsActive(false);
  };

  const [voices, setVoices] = useState([]);

  // Load available voices
  useEffect(() => {
    if (!('speechSynthesis' in window)) return;
    const updateVoices = () => {
      const v = window.speechSynthesis.getVoices();
      if (v && v.length > 0) setVoices(v);
    };
    updateVoices();
    window.speechSynthesis.onvoiceschanged = updateVoices;
    return () => {
      window.speechSynthesis.onvoiceschanged = null;
    };
  }, []);

  // Text-To-Speech Role Helper
  // - 'narrator': Male Voice (entire script read-through)
  // - 'park': Late 50s Female (Prof. Eunju Park: mature, calm, authoritative, lower pitch)
  // - 'sora': Mid 20s Female (TA Sora: lively, bouncy, youthful, upbeat, higher pitch)
  const getVoiceForRole = (role) => {
    if (!voices.length) return null;
    const englishVoices = voices.filter(v => v.lang.startsWith('en'));
    const pool = englishVoices.length > 0 ? englishVoices : voices;

    const maleVoices = pool.filter(v => /david|guy|george|mark|christopher|eric|male/i.test(v.name));
    const femaleVoices = pool.filter(v => !/david|guy|george|mark|christopher|eric|male/i.test(v.name));

    if (role === 'narrator') {
      return maleVoices[0] || pool[0];
    } else if (role === 'park') {
      // 50s professor: deep, mature, calm tone (Zira, Susan, Hazel, Catherine, or 1st female)
      const matureVoice = femaleVoices.find(v => /zira|susan|hazel|catherine|linda/i.test(v.name));
      return matureVoice || femaleVoices[0] || pool[0];
    } else if (role === 'sora') {
      // Mid-20s TA: bubbly, energetic, youthful tone (Aria, Ava, Jenny, Samantha, Victoria)
      const youngVoice = femaleVoices.find(v => /aria|ava|jenny|samantha|victoria|stephanie|karen/i.test(v.name));
      if (youngVoice) return youngVoice;
      
      // If no explicit match, pick a DIFFERENT female voice from Prof. Park if available
      if (femaleVoices.length > 1) {
        return femaleVoices[femaleVoices.length - 1];
      }
      return femaleVoices[0] || pool[0];
    }
    return pool[0];
  };

  const speakText = (textToSpeak, role = 'narrator') => {
    if (!('speechSynthesis' in window)) return;

    if (speakingText === textToSpeak) {
      window.speechSynthesis.cancel();
      setSpeakingText(null);
      return;
    }

    window.speechSynthesis.cancel();
    // Convert math expressions and LaTeX syntax into natural spoken English
    const naturalSpokenText = convertMathToSpokenEnglish(textToSpeak);
    const utterance = new SpeechSynthesisUtterance(naturalSpokenText);
    utterance.lang = 'en-US';

    const selectedVoice = getVoiceForRole(role);
    if (selectedVoice) {
      utterance.voice = selectedVoice;
    }

    // Role-specific prosody tuning:
    if (role === 'narrator') {
      utterance.pitch = 0.95; // Steady, composed male narrator
      utterance.rate = 0.92;
    } else if (role === 'park') {
      utterance.pitch = 0.82; // Mature, dignified 50s professor (calm, deep, authoritative)
      utterance.rate = 0.85;  // Deliberate, clear, academic pacing
    } else if (role === 'sora') {
      utterance.pitch = 1.38; // Bouncy, bubbly mid-20s TA (톡톡 튀는 상큼하고 밝은 톤!)
      utterance.rate = 1.05;  // Upbeat, enthusiastic, energetic rhythm
    } else {
      utterance.pitch = 1.0;
      utterance.rate = 0.90;
    }
    
    utterance.onend = () => setSpeakingText(null);
    utterance.onerror = () => setSpeakingText(null);

    setSpeakingText(textToSpeak);
    window.speechSynthesis.speak(utterance);
  };

  // Speak currently highlighted/selected text (using clear male narrator voice)
  const speakSelection = () => {
    const selectedText = window.getSelection()?.toString().trim();
    if (selectedText) {
      speakText(selectedText, 'narrator');
    }
  };

  const cycleFontSize = () => {
    if (fontSize === 'text-sm') setFontSize('text-base');
    else if (fontSize === 'text-base') setFontSize('text-lg');
    else if (fontSize === 'text-lg') setFontSize('text-xl');
    else setFontSize('text-sm');
  };

  return (
    <div className="fixed inset-y-0 right-0 w-full md:w-[540px] bg-slate-950/95 border-l border-cyan-500/30 backdrop-blur-2xl shadow-2xl z-50 flex flex-col justify-between overflow-hidden font-sans select-text">
      {/* Presenter Teleprompter Header */}
      <div className="p-3.5 bg-slate-900/90 border-b border-slate-800 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-ping" />
          <h2 className="text-xs font-bold text-cyan-300 tracking-wider uppercase select-none">
            PRESENTER TELEPROMPTER
          </h2>
        </div>
        
        {/* Timer Control & Pacing Target */}
        <div className="flex items-center gap-2 select-none">
          <div className="flex items-center gap-1.5 bg-slate-800/90 px-3 py-1 rounded-full border border-slate-700">
            <Clock className="w-3.5 h-3.5 text-cyan-400" />
            <span className="font-mono text-xs font-bold text-amber-300">{formatTime(seconds)}</span>
            <span className="text-[10px] text-slate-400 font-mono">/ 60:00</span>
            <button 
              onClick={() => setIsActive(!isActive)}
              className="text-slate-400 hover:text-white transition ml-1"
              title={isActive ? "Pause Timer" : "Start Timer"}
            >
              {isActive ? <Pause className="w-3 h-3" /> : <Play className="w-3 h-3" />}
            </button>
            <button 
              onClick={handleResetTimer}
              className="text-slate-400 hover:text-white transition"
              title="Reset Timer"
            >
              <RotateCcw className="w-3 h-3" />
            </button>
          </div>

          <button 
            onClick={onClose}
            className="p-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white transition"
            title="Close Teleprompter"
          >
            <X className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Slide Index & Control Header */}
      <div className="px-4 py-2.5 bg-slate-900/60 border-b border-slate-800/80 flex items-center justify-between select-none">
        <div className="flex items-center gap-2 truncate">
          <span className="px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-mono font-bold text-[11px] border border-cyan-500/30">
            {currentSlide} / {totalSlides}
          </span>
          <h3 className="text-xs font-bold text-white truncate max-w-[260px]">
            {slideData?.title}
          </h3>
        </div>

        {/* Font Controls & Pronunciation Button */}
        <div className="flex items-center gap-1.5">
          <button
            onClick={speakSelection}
            className="px-2 py-1 rounded bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 border border-indigo-500/40 text-[11px] font-medium flex items-center gap-1 transition"
            title="Highlight any text with mouse and click here to hear pronunciation"
          >
            <Volume2 className="w-3 h-3" />
            <span>선택 발음 듣기</span>
          </button>

          <button
            onClick={cycleFontSize}
            className="p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-cyan-300 transition text-xs font-mono font-bold flex items-center gap-1"
            title="Change Text Size"
          >
            <Type className="w-3.5 h-3.5" />
            <span className="text-[10px] uppercase">{fontSize.replace('text-', '')}</span>
          </button>

          <div className="h-4 w-px bg-slate-800" />

          <button 
            onClick={onPrev} 
            disabled={currentSlide === 1}
            className="p-1 rounded bg-slate-800 hover:bg-cyan-500/20 text-white disabled:opacity-30 transition"
          >
            <ChevronLeft className="w-4 h-4" />
          </button>
          <button 
            onClick={onNext} 
            disabled={currentSlide === totalSlides}
            className="p-1 rounded bg-slate-800 hover:bg-cyan-500/20 text-white disabled:opacity-30 transition"
          >
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* View Mode Selector Tabs */}
      <div className="grid grid-cols-3 gap-1 p-2 bg-slate-900 border-b border-slate-800/90 text-xs font-bold select-none">
        <button
          onClick={() => setActiveTab('script')}
          className={`py-2 px-2 rounded-lg flex items-center justify-center gap-1.5 transition ${
            activeTab === 'script' 
              ? 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 shadow-sm' 
              : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
          }`}
        >
          <Volume2 className="w-3.5 h-3.5" />
          <span>English Script</span>
        </button>

        <button
          onClick={() => setActiveTab('korean')}
          className={`py-2 px-2 rounded-lg flex items-center justify-center gap-1.5 transition ${
            activeTab === 'korean' 
              ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40 shadow-sm' 
              : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
          }`}
        >
          <Globe className="w-3.5 h-3.5" />
          <span>한국어 강의가이드</span>
        </button>

        <button
          onClick={() => setActiveTab('terms')}
          className={`py-2 px-2 rounded-lg flex items-center justify-center gap-1.5 transition ${
            activeTab === 'terms' 
              ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 shadow-sm' 
              : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
          }`}
        >
          <BookOpen className="w-3.5 h-3.5" />
          <span>Key Vocabulary</span>
        </button>
      </div>

      {/* Teleprompter Main Content Area */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4 select-text">
        
        {/* TAB 1: EASY ENGLISH SPOKEN SCRIPT */}
        {activeTab === 'script' && (
          <div className="space-y-3">
            <div className="flex items-center justify-between text-xs text-cyan-400 font-medium pb-1 border-b border-cyan-500/20 select-none">
              <span className="flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5" />
                Spoken Teleprompter Script (ESL Easy English)
              </span>
              <div className="flex items-center gap-2">
                {slideData?.script && (
                  <button
                    onClick={() => {
                      const cleanFull = slideData.script
                        .replace(/\[(?:Prof\.\s*Park|TA\s*Sora|Prof\.\s*Peter(?:\s*Kim)?|TA\s*Sarah|TA\s*James)\]:?/gi, '')
                        .trim();
                      speakText(cleanFull, 'narrator');
                    }}
                    className="px-2.5 py-1 rounded bg-cyan-500/20 hover:bg-cyan-500/30 text-cyan-300 border border-cyan-500/40 text-[10px] font-bold flex items-center gap-1.5 transition"
                    title="전체 대본을 차분한 남성 내레이터 목소리로 완독합니다"
                  >
                    {speakingText ? <VolumeX className="w-3 h-3 text-amber-400" /> : <Volume2 className="w-3 h-3 text-cyan-300" />}
                    <span>{speakingText ? '정지' : '🎙️ 전체 낭독 (남성 목소리)'}</span>
                  </button>
                )}
                <span className="text-[10px] text-slate-400 bg-slate-900 px-2 py-0.5 rounded border border-slate-800">
                  🎯 ~1:30 min
                </span>
              </div>
            </div>

            <div className="space-y-3">
              {slideData?.script ? (
                slideData.script.split(/\n\n+|\n(?=\[(?:Prof|TA)|(?:Prof\.|TA\s)[\w\s]+:)/).map((paragraph, idx) => {
                  const trimmed = paragraph.trim();
                  if (!trimmed) return null;

                  const isPark = trimmed.startsWith('[Prof. Park]') || trimmed.startsWith('Prof. Park:');
                  const isSora = trimmed.startsWith('[TA Sora]') || trimmed.startsWith('TA Sora:');
                  const isPeter = trimmed.startsWith('[Prof. Peter]') || trimmed.startsWith('[Prof. Peter Kim]');
                  const isSarah = trimmed.startsWith('[TA Sarah]') || trimmed.startsWith('[Sarah (TA)]') || trimmed.startsWith('[Prof. Sarah]');
                  const isJames = trimmed.startsWith('[TA James]') || trimmed.startsWith('[James (TA)]') || trimmed.startsWith('[James]');
                  
                  const cleanText = trimmed.replace(/^(\[(Prof\.\s*Park|TA\s*Sora|Prof\.\s*Peter(\s*Kim)?|TA\s*Sarah|Sarah\s*\(TA\)|Prof\.\s*Sarah|TA\s*James|James\s*\(TA\)|James)\]|(Prof\.\s*Park|TA\s*Sora):)\s*/i, '');
                  const currentRole = isPark ? 'park' : isSora ? 'sora' : (isPeter || isJames) ? 'narrator' : isSarah ? 'sora' : 'narrator';
                  
                  return (
                    <div 
                      key={idx} 
                      className={`group relative p-3.5 rounded-xl border transition ${
                        isPark || isPeter
                          ? 'bg-blue-950/40 border-blue-500/40 text-blue-50 shadow-sm shadow-blue-950/50' 
                          : isSora
                            ? 'bg-amber-950/40 border-amber-500/40 text-amber-50 shadow-sm shadow-amber-950/50'
                          : isSarah 
                            ? 'bg-purple-950/40 border-purple-500/40 text-purple-50 shadow-sm shadow-purple-950/50' 
                            : isJames
                              ? 'bg-emerald-950/40 border-emerald-500/40 text-emerald-50 shadow-sm shadow-emerald-950/50'
                              : 'bg-slate-900/90 border-cyan-500/30 text-cyan-50'
                      }`}
                    >
                      {/* Speaker Badge */}
                      <div className="flex items-center justify-between mb-2">
                        {isPark && (
                          <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/40" title="50대 후반 여성 주임교수 • 차분하고 깊이 있는 학구적 톤">
                            <span className="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></span>
                            👩‍🏫 Prof. Eunju Park (50대 여성 교수 • 차분한 톤)
                          </span>
                        )}
                        {isSora && (
                          <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40" title="20대 중반 여성 수석조교 • 상큼하고 톡톡 튀는 발랄한 톤">
                            <span className="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
                            👩‍🎓 TA Sora (20대 조교 • 톡톡 튀는 톤)
                          </span>
                        )}
                        {isPeter && (
                          <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/40">
                            <span className="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></span>
                            👨‍🏫 Prof. Peter Kim (Lead Professor)
                          </span>
                        )}
                        {isSarah && (
                          <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/40">
                            <span className="w-2 h-2 rounded-full bg-purple-400 animate-pulse"></span>
                            👩‍💻 TA Sarah Jenkins (Senior TA & Architect)
                          </span>
                        )}
                        {isJames && (
                          <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                            👨‍💻 TA James Wilson (DevOps & Infrastructure TA)
                          </span>
                        )}
                        {!isPark && !isSora && !isPeter && !isSarah && !isJames && (
                          <span className="text-[11px] font-bold text-cyan-300">🎙️ Spoken Script</span>
                        )}

                        <button
                          onClick={() => speakText(cleanText || paragraph, currentRole)}
                          className="opacity-60 group-hover:opacity-100 p-1 text-slate-300 hover:text-white transition rounded bg-slate-800/80 hover:bg-slate-700 flex items-center gap-1 text-[10px]"
                          title={`${isPark ? '박교수 (50대 차분한 여성)' : isSora ? 'Sora 조교 (20대 톡톡 튀는 여성)' : '남성 내레이터'} 음성으로 듣기`}
                        >
                          <Volume2 className="w-3.5 h-3.5" />
                          <span className="hidden group-hover:inline text-[9px] text-slate-300">
                            {isPark ? '50대 차분한 톤' : isSora ? '20대 톡톡 튀는 톤' : '남성'}
                          </span>
                        </button>
                      </div>

                      <p className={`${fontSize} leading-relaxed font-normal text-slate-100 selection:bg-cyan-500 selection:text-slate-950`}>
                        {renderInlineMathAndBold(cleanText || paragraph, `pres-script-${idx}`)}
                      </p>
                    </div>
                  );
                })
              ) : (
                <div className="p-4 rounded-xl bg-slate-900/90 border border-cyan-500/30 text-slate-400 italic">
                  No spoken script provided for this slide.
                </div>
              )}
            </div>
          </div>
        )}

        {/* TAB 2: KOREAN LECTURE & DELIVERY GUIDE */}
        {activeTab === 'korean' && (
          <div className="space-y-4 cursor-text">
            <div className="flex items-center justify-between text-xs text-amber-400 font-medium pb-1 border-b border-amber-500/20 select-none">
              <span className="flex items-center gap-1.5">
                <Globe className="w-3.5 h-3.5" />
                한국어 강의 해설 및 내용 전달 가이드
              </span>
              <span className="text-[10px] text-amber-300/80 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/30">
                강의자 전용 팁
              </span>
            </div>

            {slideData?.koreanGuide ? (
              <div className="space-y-3">
                {/* Core Summary Box */}
                <div className="p-3.5 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-100 space-y-1.5">
                  <div className="flex items-center gap-1.5 text-amber-300 text-xs font-bold uppercase select-none">
                    <CheckCircle2 className="w-3.5 h-3.5" />
                    <span>슬라이드 핵심 요지 (Core Summary)</span>
                  </div>
                  <p className="text-sm font-medium leading-relaxed text-amber-200 selection:bg-amber-500 selection:text-slate-950">
                    {slideData.koreanGuide.summary}
                  </p>
                </div>

                {/* Main Explanation Points */}
                <div className="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
                  <span className="text-xs font-bold text-cyan-300 block uppercase tracking-wider select-none">
                    📌 본문 설명 및 전달 포인트
                  </span>
                  <ul className="space-y-2">
                    {slideData.koreanGuide.points.map((point, idx) => (
                      <li key={idx} className="text-xs text-slate-200 leading-relaxed flex items-start gap-2 selection:bg-cyan-500 selection:text-slate-950">
                        <span className="w-1.5 h-1.5 rounded-full bg-cyan-400 mt-1.5 shrink-0" />
                        <span>{point}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* Delivery & Q&A Tip */}
                <div className="p-3.5 rounded-xl bg-indigo500/10 border border-indigo-500/30 text-indigo-100 space-y-1">
                  <div className="flex items-center gap-1.5 text-indigo-300 text-xs font-bold uppercase select-none">
                    <Lightbulb className="w-3.5 h-3.5" />
                    <span>강의 전달 & 학생 소통 팁</span>
                  </div>
                  <p className="text-xs text-indigo-200 leading-relaxed selection:bg-indigo-500 selection:text-slate-950">
                    {slideData.koreanGuide.tips}
                  </p>
                </div>
              </div>
            ) : (
              <p className="text-slate-400 italic text-xs">한국어 가이드 정보가 준비 중입니다.</p>
            )}
          </div>
        )}

        {/* TAB 3: KEY VOCABULARY & DEFINITIONS */}
        {activeTab === 'terms' && (
          <div className="space-y-3 cursor-text">
            <div className="flex items-center justify-between text-xs text-emerald-400 font-medium pb-1 border-b border-emerald-500/20 select-none">
              <span className="flex items-center gap-1.5">
                <BookOpen className="w-3.5 h-3.5" />
                Key Terms & Korean Meanings (어휘 정리)
              </span>
            </div>

            {slideData?.keyTerms && slideData.keyTerms.length > 0 ? (
              <div className="grid gap-2.5">
                {slideData.keyTerms.map((kt, idx) => (
                  <div key={idx} className="p-3 rounded-xl bg-slate-900/90 border border-emerald-500/30 space-y-1 relative group">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <span className="font-bold text-emerald-300 text-xs selection:bg-emerald-500 selection:text-slate-950">{kt.term}</span>
                        <button
                          onClick={() => speakText(kt.term)}
                          className="p-0.5 text-emerald-400 hover:text-white transition rounded"
                          title={`Listen to pronunciation of '${kt.term}'`}
                        >
                          <Volume2 className="w-3.5 h-3.5" />
                        </button>
                      </div>

                      {kt.defKo && (
                        <span className="text-[11px] font-medium text-amber-300 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20 select-none">
                          {kt.defKo}
                        </span>
                      )}
                    </div>
                    <p className="text-slate-300 text-xs leading-relaxed selection:bg-emerald-500 selection:text-slate-950">{kt.def}</p>
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-slate-400 italic text-xs">등록된 어휘가 없습니다.</p>
            )}
          </div>
        )}

        {/* Next Slide Preview */}
        {nextSlideData && (
          <div className="pt-3 border-t border-slate-800/80 space-y-1.5 select-none">
            <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">
              NEXT SLIDE ({nextSlideData.num} / {totalSlides})
            </span>
            <div className="p-2.5 rounded-lg bg-slate-900/40 border border-slate-800 opacity-70">
              <p className="text-xs font-bold text-slate-300 truncate">{nextSlideData.title}</p>
              <p className="text-[11px] text-slate-400 truncate mt-0.5">{nextSlideData.subtitle}</p>
            </div>
          </div>
        )}
      </div>

      {/* Footer Navigation Bar */}
      <div className="p-3 bg-slate-900 border-t border-slate-800 flex items-center justify-between select-none">
        <button 
          onClick={onPrev}
          disabled={currentSlide === 1}
          className="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-white text-xs font-medium disabled:opacity-30 transition flex items-center gap-1"
        >
          <ChevronLeft className="w-4 h-4" />
          <span>Previous</span>
        </button>

        <div className="text-center">
          <span className="text-xs font-mono font-bold text-cyan-400 block">
            Slide {currentSlide} of {totalSlides}
          </span>
          <span className="text-[10px] text-slate-400">
            60-Min Full Session
          </span>
        </div>

        <button 
          onClick={onNext}
          disabled={currentSlide === totalSlides}
          className="px-4 py-2 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 text-xs font-bold disabled:opacity-30 transition flex items-center gap-1 shadow-lg shadow-cyan-500/20"
        >
          <span>Next</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}
