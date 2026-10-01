import React from 'react';
import { 
  ChevronLeft, 
  ChevronRight, 
  Grid, 
  Monitor, 
  Maximize, 
  Printer,
  Sparkles,
  BookOpen,
  GraduationCap
} from 'lucide-react';
import { MONTANA_LECTURES } from '../data/montanaSlidesData';

export default function Header({ 
  currentSlide, 
  totalSlides, 
  onPrev, 
  onNext, 
  onTogglePresenter, 
  isPresenterOpen,
  onToggleOverview,
  onToggleCurriculum,
  onExportPDF,
  selectedSession,
  onSelectSession
}) {
  const toggleFullScreen = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => console.log(err));
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  };

  return (
    <header className="no-print h-16 bg-[#00173D]/95 backdrop-blur-md border-b border-amber-500/25 px-4 flex items-center justify-between z-30 sticky top-0 shadow-lg">
      {/* Brand & Logo: Montana State University Bobcats */}
      <div className="flex items-center gap-3">
        <div className="w-9 h-9 rounded-lg bg-gradient-to-br from-amber-400 via-amber-500 to-blue-800 flex items-center justify-center shadow-lg shadow-amber-500/20 border border-amber-400/30">
          <GraduationCap className="w-5 h-5 text-white" />
        </div>
        <div>
          <div className="flex items-center gap-2">
            <span className="font-extrabold text-white tracking-wide text-xs md:text-sm">
              MONTANA STATE UNIVERSITY
            </span>
            <span className="text-[10px] px-2 py-0.5 rounded font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40">
              GALLATIN COLLEGE • M090
            </span>
          </div>
          <div className="flex items-center gap-2 mt-0.5">
            <span className="inline-flex items-center gap-1 px-1.5 py-0.2 rounded bg-blue-500/25 text-blue-200 text-[10px] font-bold border border-blue-400/30">
              <span className="w-1.5 h-1.5 rounded-full bg-blue-400"></span>
              Prof. Eunju Park
            </span>
            <span className="inline-flex items-center gap-1 px-1.5 py-0.2 rounded bg-amber-500/25 text-amber-200 text-[10px] font-bold border border-amber-400/30">
              <span className="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
              TA Sora
            </span>
          </div>
        </div>
      </div>

      {/* Lecture Selector & Progress */}
      <div className="hidden md:flex items-center gap-4">
        <select 
          value={selectedSession} 
          onChange={(e) => onSelectSession(Number(e.target.value))}
          className="bg-slate-900/90 border border-amber-500/30 text-xs text-white rounded-lg px-3 py-1.5 focus:outline-none focus:border-amber-400 transition"
        >
          {MONTANA_LECTURES.map(s => (
            <option key={s.id} value={s.id} disabled={!s.active}>
              {s.title}
            </option>
          ))}
        </select>

        {/* Counter Badge */}
        <div className="px-3 py-1 rounded-full bg-slate-900/80 border border-amber-500/30 text-xs font-semibold text-amber-300 flex items-center gap-1.5">
          <span>Slide</span>
          <span className="text-white font-bold">{currentSlide}</span>
          <span className="text-slate-500">/</span>
          <span className="text-slate-400">{totalSlides}</span>
        </div>
      </div>

      {/* Action Controls */}
      <div className="flex items-center gap-2">
        {/* Navigation Buttons */}
        <button 
          onClick={onPrev} 
          disabled={currentSlide === 1}
          className="p-2 rounded-lg bg-slate-800/80 hover:bg-cyan-500/20 text-white disabled:opacity-30 disabled:hover:bg-slate-800 transition border border-slate-700"
          title="Previous Slide (Left Arrow)"
        >
          <ChevronLeft className="w-4 h-4" />
        </button>

        <button 
          onClick={onNext} 
          disabled={currentSlide === totalSlides}
          className="p-2 rounded-lg bg-slate-800/80 hover:bg-cyan-500/20 text-white disabled:opacity-30 disabled:hover:bg-slate-800 transition border border-slate-700"
          title="Next Slide (Right Arrow)"
        >
          <ChevronRight className="w-4 h-4" />
        </button>

        <div className="h-5 w-px bg-slate-800 mx-1" />

        {/* Master Curriculum & Table of Contents Button */}
        <button 
          onClick={onToggleCurriculum}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-cyan-500/20 hover:bg-cyan-500/30 text-cyan-300 border border-cyan-500/40 text-xs font-bold transition shadow-md"
          title="Course Syllabus & Master Table of Contents [S]"
        >
          <BookOpen className="w-3.5 h-3.5 text-cyan-400" />
          <span className="hidden sm:inline">Course Syllabus</span>
          <span className="sm:hidden">Syllabus</span>
        </button>

        {/* Grid Overview */}
        <button 
          onClick={onToggleOverview}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-white border border-slate-700 transition"
          title="View All Slides [M]"
        >
          <Grid className="w-3.5 h-3.5 text-cyan-400" />
          <span className="hidden sm:inline">Overview</span>
        </button>

        {/* Export PDF Button */}
        <button 
          onClick={onExportPDF}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-bold transition shadow-md"
          title="Export All 40 Slides to PDF (No Scripts)"
        >
          <Printer className="w-3.5 h-3.5 text-amber-400" />
          <span>Export PDF</span>
        </button>

        {/* Presenter Teleprompter Mode Toggle */}
        <button 
          onClick={onTogglePresenter}
          className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold border transition ${
            isPresenterOpen 
              ? "bg-cyan-500 text-slate-950 border-cyan-400 shadow-lg shadow-cyan-500/30" 
              : "bg-slate-800 hover:bg-cyan-500/20 text-cyan-400 border-cyan-500/30"
          }`}
          title="Toggle Presenter Teleprompter View [P]"
        >
          <Monitor className="w-3.5 h-3.5" />
          <span>Presenter Mode [P]</span>
        </button>

        {/* Fullscreen Toggle */}
        <button 
          onClick={toggleFullScreen}
          className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition border border-slate-700"
          title="Toggle Fullscreen [F]"
        >
          <Maximize className="w-4 h-4" />
        </button>
      </div>
    </header>
  );
}
