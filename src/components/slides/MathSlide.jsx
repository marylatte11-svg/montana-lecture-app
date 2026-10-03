import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { CheckCircle2, AlertTriangle, MessageSquare, Lightbulb, Sparkles, GraduationCap, Compass, HelpCircle, BookOpen } from 'lucide-react';
import MathRenderer from './MathRenderer';
import CoordinateGrid from './CoordinateGrid';

export default function MathSlide({ slideData }) {
  const [activeTab, setActiveTab] = useState('solution'); // 'solution' or 'script'

  const {
    num = 1,
    title = '',
    subtitle = '',
    detail = '',
    slideTypeLabel = 'Problem Breakdown',
    problem = '',
    solution = '',
    pitfall = '',
    script = '',
    graph = null,
    coordinate = null,
    problemGraph = null,
    graphPosition = 'solution'
  } = slideData || {};

  const activeGraph = graph || coordinate;

  const searchParams = typeof window !== 'undefined' ? new URLSearchParams(window.location.search) : null;
  const activeTurnParam = searchParams ? searchParams.get('activeTurn') : null;
  const activeTurn = activeTurnParam !== null ? parseInt(activeTurnParam, 10) : null;

  const isConceptSlide = !solution || slideTypeLabel.toLowerCase().includes('concept') || slideTypeLabel.toLowerCase().includes('definition');
  const problemCardLabel = isConceptSlide ? 'Concept Focus & Definitions' : 'Problem Statement';
  const isWorkbookMatch = (subtitle && subtitle.toLowerCase().includes('workbook')) || (slideTypeLabel && slideTypeLabel.toLowerCase().includes('workbook'));

  return (
    <div className="w-full h-full max-w-full flex flex-col justify-between p-4 md:p-6 lg:p-8 text-slate-100">
      {/* Top Banner / University Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-amber-500/25 pb-4 mb-4">
        <div>
          <div className="flex items-center gap-2.5 mb-1.5 flex-wrap">
            <span className="px-3 py-1 rounded-full text-xs font-bold tracking-wide uppercase bg-blue-600/30 text-blue-200 border border-blue-500/40 flex items-center gap-1.5 shadow-sm">
              <GraduationCap className="w-4 h-4 text-amber-400" />
              Gallatin College MSU
            </span>
            {isWorkbookMatch && (
              <span className="px-3 py-1 rounded-full text-xs font-bold tracking-wide bg-emerald-500/20 text-emerald-300 border border-emerald-500/35 flex items-center gap-1.5 shadow-sm">
                <BookOpen className="w-3.5 h-3.5 text-emerald-400" />
                M090 Workbook Match
              </span>
            )}
            <span className="px-3 py-1 rounded-full text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/30">
              {slideTypeLabel}
            </span>
            <span className="text-xs text-slate-400 font-mono px-2 py-0.5 rounded bg-slate-900 border border-slate-800">
              Slide {num}
            </span>
          </div>
          <h2 className="text-2xl md:text-3xl lg:text-4xl font-black tracking-tight text-white flex items-center gap-3">
            <MathRenderer content={title} inline={true} />
          </h2>
          <div className="text-sm md:text-base text-slate-300 font-medium mt-1">
            <MathRenderer content={subtitle || detail} inline={true} />
          </div>
        </div>

        {/* View Switcher Tabs */}
        <div className="flex items-center gap-2 bg-slate-900/90 p-1.5 rounded-xl border border-slate-700/60 shadow-inner self-start md:self-auto shrink-0">
          <button
            onClick={() => setActiveTab('solution')}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg text-xs md:text-sm font-bold transition ${
              activeTab === 'solution'
                ? 'bg-blue-600 text-white shadow-lg shadow-blue-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
            }`}
          >
            <CheckCircle2 className="w-4 h-4 text-amber-300" />
            {solution ? 'AI Solution & Steps' : 'Concept Overview'}
          </button>
          <button
            onClick={() => setActiveTab('script')}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg text-xs md:text-sm font-bold transition ${
              activeTab === 'script'
                ? 'bg-amber-600 text-white shadow-lg shadow-amber-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
            }`}
          >
            <MessageSquare className="w-4 h-4 text-white" />
            Prof. Park & TA Sora Dialogue
          </button>
        </div>
      </div>

      {/* Main Content Area: Responsive Spacious Grid */}
      <div className="flex-1 overflow-y-auto pr-1 flex flex-col">
        {activeTab === 'solution' && (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch flex-1 min-h-[500px]">
            {/* Left Card: Problem Statement / Concept (6 cols) */}
            <div className="lg:col-span-6 flex flex-col gap-4 h-full justify-between">
              {/* Problem / Concept Card */}
              {problem && (
                <div className="bg-gradient-to-br from-slate-900/95 via-slate-900/90 to-blue-950/40 rounded-2xl p-6 lg:p-7 border border-blue-500/35 shadow-2xl relative overflow-hidden flex-1 flex flex-col justify-between">
                  <div className="absolute top-0 right-0 w-32 h-32 bg-blue-500/10 rounded-full blur-2xl pointer-events-none" />
                  <div>
                    <div className="flex items-center justify-between gap-2 border-b border-blue-500/20 pb-3 mb-4">
                      <div className="flex items-center gap-2 text-xs lg:text-sm font-extrabold uppercase tracking-wider text-blue-300">
                        {isConceptSlide ? (
                          <Compass className="w-4 h-4 text-amber-400" />
                        ) : (
                          <Sparkles className="w-4 h-4 text-blue-400" />
                        )}
                        {problemCardLabel}
                      </div>
                      <span className="text-[10px] lg:text-xs uppercase font-bold tracking-widest px-2.5 py-0.5 rounded bg-blue-950/80 text-blue-300 border border-blue-500/30">
                        {isWorkbookMatch ? 'Official Workbook Problem' : 'Core Concept'}
                      </span>
                    </div>
                    <div className="text-base md:text-lg text-slate-100 font-medium leading-relaxed">
                      <MathRenderer content={problem} />
                    </div>
                    {(problemGraph || (activeGraph && (graphPosition === 'problem' || graphPosition === 'both'))) && (
                      <div className="mt-4 flex justify-center w-full">
                        <CoordinateGrid {...(problemGraph || activeGraph)} />
                      </div>
                    )}
                  </div>
                </div>
              )}

              {/* Sora's Pitfall Alert / Pro-Tip Card */}
              {pitfall ? (
                <div className="bg-gradient-to-br from-amber-950/60 via-slate-900/90 to-rose-950/40 rounded-2xl p-5 border border-amber-500/40 shadow-xl shrink-0">
                  <div className="flex items-center gap-2 text-xs lg:text-sm font-bold uppercase tracking-wider text-amber-300 mb-2 border-b border-amber-500/20 pb-2">
                    <AlertTriangle className="w-4 h-4 text-amber-400" />
                    Sora's Pitfall Alert & Pro-Tip
                  </div>
                  <div className="text-sm md:text-base text-amber-100/95 leading-relaxed bg-black/30 p-4 rounded-xl border border-amber-500/25">
                    <MathRenderer content={pitfall} />
                  </div>
                </div>
              ) : (
                <div className="bg-slate-900/70 rounded-2xl p-4 border border-slate-700/60 flex items-start gap-3 shadow-md shrink-0">
                  <Lightbulb className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
                  <div className="text-xs md:text-sm text-slate-300 leading-relaxed">
                    <span className="font-bold text-amber-300">Sora's Pro-Tip:</span> Write every step on paper. Never skip protective parentheses when substituting negative numbers!
                  </div>
                </div>
              )}
            </div>

            {/* Right Card: AI Step-by-Step Solution OR Concept Dialogue Highlights (6 cols) */}
            <div className="lg:col-span-6 flex flex-col h-full">
              <div className="bg-gradient-to-br from-slate-900/95 via-slate-900/90 to-cyan-950/30 rounded-2xl p-6 lg:p-7 border border-cyan-500/35 shadow-2xl flex flex-col flex-1 h-full justify-between">
                <div className="flex items-center justify-between mb-4 border-b border-slate-800 pb-3">
                  <div className="flex items-center gap-2 text-xs lg:text-sm font-extrabold uppercase tracking-wider text-cyan-300">
                    <CheckCircle2 className="w-4 h-4 text-cyan-400" />
                    {solution ? 'AI Step-by-Step Solution & Graph' : 'Key Conceptual Takeaway & Dialogue'}
                  </div>
                  <span className="text-[10px] lg:text-xs font-mono px-2.5 py-0.5 rounded bg-cyan-950/80 text-cyan-300 border border-cyan-500/30 font-semibold">
                    KaTeX Formatted
                  </span>
                </div>
                
                <div className="text-base text-slate-100 leading-relaxed flex-1 overflow-y-auto pr-1 space-y-4">
                  {activeGraph && graphPosition !== 'problem' && (
                    <div className="mb-4 flex justify-center w-full">
                      <CoordinateGrid {...activeGraph} />
                    </div>
                  )}
                  {solution ? (
                    <div className="bg-slate-950/80 p-5 rounded-xl border border-white/5 shadow-inner">
                      <MathRenderer content={solution} />
                    </div>
                  ) : script ? (
                    <div className="space-y-2.5">
                      <div className="text-xs font-semibold text-slate-400 uppercase tracking-wider flex items-center gap-1.5 mb-1.5">
                        <MessageSquare className="w-3.5 h-3.5 text-amber-400" />
                        Instructor Dialogue Highlights:
                      </div>
                      {script.split(/\n\n+|\n(?=\[(?:Prof|TA)|(?:Prof\.|TA\s)[\w\s]+:)/).map((para, pIdx) => {
                        const trimmed = para.trim();
                        if (!trimmed) return null;
                        const isProf = trimmed.startsWith('[Prof. Park]') || trimmed.startsWith('Prof. Park:');
                        const isSora = trimmed.startsWith('[TA Sora]') || trimmed.startsWith('TA Sora:');
                        const cleanText = trimmed.replace(/^(\[(Prof\.\s*Park|TA\s*Sora)\]|(Prof\.\s*Park|TA\s*Sora):)\s*/i, '');
                        const isActive = activeTurn !== null && activeTurn === pIdx;
                        const isDimmed = activeTurn !== null && activeTurn !== pIdx;

                        return (
                          <div
                            key={pIdx}
                            id={`dialogue-turn-${pIdx}`}
                            className={`p-2.5 px-3 rounded-xl border text-xs md:text-sm leading-snug transition-all duration-300 ${
                              isActive
                                ? isProf
                                  ? 'bg-blue-900/90 border-blue-400 text-white shadow-xl shadow-blue-500/50 scale-[1.02] ring-2 ring-blue-400'
                                  : 'bg-amber-900/90 border-amber-400 text-white shadow-xl shadow-amber-500/50 scale-[1.02] ring-2 ring-amber-400'
                                : isDimmed
                                ? 'opacity-35 border-slate-800/80 bg-slate-900/30 text-slate-400 scale-[0.99]'
                                : isProf
                                ? 'bg-blue-950/40 border-blue-500/30 text-blue-50 shadow-sm'
                                : isSora
                                ? 'bg-amber-950/30 border-amber-500/30 text-amber-50 shadow-sm'
                                : 'bg-slate-800/50 border-slate-700 text-slate-200'
                            }`}
                          >
                            <div className="flex items-center gap-2 mb-1">
                              <span
                                className={`text-[10px] font-extrabold uppercase px-2 py-0.5 rounded ${
                                  isProf
                                    ? 'bg-blue-500/30 text-blue-300 border border-blue-400/40'
                                    : 'bg-amber-500/30 text-amber-300 border border-amber-400/40'
                                }`}
                              >
                                {isProf ? 'Prof. Eunju Park' : 'TA Sora'}
                              </span>
                            </div>
                            <MathRenderer content={cleanText} inline={true} />
                          </div>
                        );
                      })}
                    </div>
                  ) : (
                    <div className="text-slate-400 italic text-sm">
                      Core conceptual rule slide. Click 'Prof. Park & TA Sora Dialogue' above for full breakdown.
                    </div>
                  )}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Tab 2: Full Broadcast Dialogue */}
        {activeTab === 'script' && (
          <div className="bg-slate-900/90 rounded-2xl p-6 md:p-8 border border-amber-500/30 shadow-2xl max-w-5xl mx-auto space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-4">
              <div className="flex items-center gap-2.5 text-base font-bold text-amber-300">
                <MessageSquare className="w-5 h-5 text-amber-400" />
                Prof. Eunju Park & TA Sora — Micro-Turns Dialogue
              </div>
              <div className="flex items-center gap-2">
                <span className="text-xs px-2.5 py-1 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30 font-bold">
                  Prof. Eunju Park
                </span>
                <span className="text-xs px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 font-bold">
                  TA Sora
                </span>
              </div>
            </div>

            <div className="space-y-4 text-base md:text-lg leading-relaxed">
              {script ? (
                script.split(/\n\n+|\n(?=\[(?:Prof|TA)|(?:Prof\.|TA\s)[\w\s]+:)/).map((paragraph, idx) => {
                  const trimmed = paragraph.trim();
                  if (!trimmed) return null;

                  const isProf = trimmed.startsWith('[Prof. Park]') || trimmed.startsWith('Prof. Park:');
                  const isSora = trimmed.startsWith('[TA Sora]') || trimmed.startsWith('TA Sora:');
                  const cleanText = trimmed.replace(/^(\[(Prof\.\s*Park|TA\s*Sora)\]|(Prof\.\s*Park|TA\s*Sora):)\s*/i, '');
                  const speaker = isProf ? 'Prof. Eunju Park' : isSora ? 'TA Sora' : 'Instructor';

                  return (
                    <motion.div
                      key={idx}
                      initial={{ opacity: 0, y: 4 }}
                      animate={{ opacity: 1, y: 0 }}
                      className={`p-4 rounded-xl border flex items-start gap-4 shadow-md ${
                        isProf
                          ? 'bg-blue-950/30 border-blue-500/35 text-blue-50'
                          : isSora
                          ? 'bg-amber-950/25 border-amber-500/35 text-amber-50'
                          : 'bg-slate-800/40 border-slate-700 text-slate-200'
                      }`}
                    >
                      <div
                        className={`text-[11px] font-black uppercase px-2.5 py-1 rounded shrink-0 mt-0.5 shadow-sm ${
                          isProf
                            ? 'bg-blue-500/30 text-blue-300 border border-blue-400/40'
                            : isSora
                            ? 'bg-amber-500/30 text-amber-300 border border-amber-400/40'
                            : 'bg-slate-700 text-slate-300'
                        }`}
                      >
                        {speaker}
                      </div>
                      <div className="flex-1 text-sm md:text-base leading-relaxed">
                        <MathRenderer content={cleanText} />
                      </div>
                    </motion.div>
                  );
                })
              ) : (
                <div className="text-slate-400 italic">No dialogue script available for this slide.</div>
              )}
            </div>
          </div>
        )}
      </div>

      {/* Bottom Footer */}
      <div className="border-t border-slate-800/80 pt-3 flex items-center justify-between text-xs md:text-sm text-slate-400">
        <div className="flex items-center gap-2">
          <span className="inline-block w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse shadow-sm shadow-amber-400/50" />
          <span className="font-semibold text-slate-300">Montana State University • Gallatin College • M090 Introductory Algebra</span>
        </div>
        <div className="font-mono text-xs text-amber-400/90 font-medium">
          Prof. Eunju Park & TA Sora • One Problem One Slide
        </div>
      </div>
    </div>
  );
}
