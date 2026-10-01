import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import SlideDeck from './components/SlideDeck';
import PresenterMode from './components/PresenterMode';
import SlideOverviewModal from './components/SlideOverviewModal';
import PrintSlidesView from './components/PrintSlidesView';
import { MONTANA_ALL_SLIDES, SLIDES_MONTANA_L01 } from './data/montanaSlidesData';
import { Keyboard } from 'lucide-react';

export default function App() {
  const getInitialSession = () => {
    if (typeof window !== 'undefined') {
      const params = new URLSearchParams(window.location.search);
      const s = parseInt(params.get('lecture') || params.get('l') || params.get('session') || params.get('s'), 10);
      if (s >= 1 && s <= 50) return s;
    }
    return 1;
  };

  const getInitialSlideIndex = () => {
    if (typeof window !== 'undefined') {
      const params = new URLSearchParams(window.location.search);
      const slide = parseInt(params.get('slide') || params.get('p'), 10);
      if (slide >= 1 && slide <= 100) return slide - 1;
    }
    return 0;
  };

  const [selectedSession, setSelectedSession] = useState(getInitialSession);
  const [currentSlideIndex, setCurrentSlideIndex] = useState(getInitialSlideIndex);
  const [isPresenterOpen, setIsPresenterOpen] = useState(false);
  const [isOverviewOpen, setIsOverviewOpen] = useState(false);
  const [showShortcutHint, setShowShortcutHint] = useState(true);
  const [isPrinting, setIsPrinting] = useState(false);

  const currentSlides = MONTANA_ALL_SLIDES[selectedSession] || SLIDES_MONTANA_L01;
  const totalSlides = currentSlides.length;
  const currentSlideData = currentSlides[currentSlideIndex] || currentSlides[0];
  const nextSlideData = currentSlideIndex < totalSlides - 1 ? currentSlides[currentSlideIndex + 1] : null;

  const handleSelectSession = (sessionId) => {
    setSelectedSession(sessionId);
    setCurrentSlideIndex(0);
  };

  // BroadcastChannel for Dual-Monitor Multi-Window Sync
  useEffect(() => {
    const channel = new BroadcastChannel('msu_slide_sync');
    channel.onmessage = (event) => {
      if (typeof event.data?.slideIndex === 'number') {
        setCurrentSlideIndex(event.data.slideIndex);
      }
    };
    return () => channel.close();
  }, []);

  const broadcastSlideChange = (newIndex) => {
    setCurrentSlideIndex(newIndex);
    try {
      const channel = new BroadcastChannel('msu_slide_sync');
      channel.postMessage({ slideIndex: newIndex });
      channel.close();
    } catch (e) {
      console.log('BroadcastChannel error:', e);
    }
  };

  const handlePrev = () => {
    if (currentSlideIndex > 0) {
      broadcastSlideChange(currentSlideIndex - 1);
    }
  };

  const handleNext = () => {
    if (currentSlideIndex < totalSlides - 1) {
      broadcastSlideChange(currentSlideIndex + 1);
    }
  };

  const handleSelectSlide = (slideNum) => {
    broadcastSlideChange(slideNum - 1);
    setIsOverviewOpen(false);
  };

  const handleExportPDF = () => {
    setIsPrinting(true);
    setTimeout(() => {
      window.print();
      setIsPrinting(false);
    }, 500);
  };

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') {
        return;
      }
      if (e.key === 'ArrowRight' || e.key === 'Space') {
        e.preventDefault();
        handleNext();
      } else if (e.key === 'ArrowLeft') {
        e.preventDefault();
        handlePrev();
      } else if (e.key === 'p' || e.key === 'P') {
        e.preventDefault();
        setIsPresenterOpen(prev => !prev);
      } else if (e.key === 'm' || e.key === 'M' || e.key === 'o' || e.key === 'O') {
        e.preventDefault();
        setIsOverviewOpen(prev => !prev);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [currentSlideIndex, totalSlides]);

  useEffect(() => {
    const timer = setTimeout(() => setShowShortcutHint(false), 8000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="w-screen h-screen flex flex-col bg-[#00122e] text-white overflow-hidden font-sans select-text">
      {/* Printable View */}
      {isPrinting && <PrintSlidesView slides={currentSlides} />}

      {/* Montana State University Header Bar */}
      <Header
        currentSlide={currentSlideIndex + 1}
        totalSlides={totalSlides}
        onPrev={handlePrev}
        onNext={handleNext}
        onTogglePresenter={() => setIsPresenterOpen(prev => !prev)}
        isPresenterOpen={isPresenterOpen}
        onToggleOverview={() => setIsOverviewOpen(prev => !prev)}
        onExportPDF={handleExportPDF}
        selectedSession={selectedSession}
        onSelectSession={handleSelectSession}
      />

      {/* Main Slide Presentation Area */}
      <main className="no-print flex-1 relative overflow-hidden bg-gradient-to-br from-[#00173D] via-[#021027] to-[#010814]">
        <SlideDeck slideData={currentSlideData} />

        {/* Presenter Teleprompter Sidebar Mode */}
        {isPresenterOpen && (
          <PresenterMode
            slideData={currentSlideData}
            nextSlideData={nextSlideData}
            currentSlide={currentSlideIndex + 1}
            totalSlides={totalSlides}
            onPrev={handlePrev}
            onNext={handleNext}
            onClose={() => setIsPresenterOpen(false)}
          />
        )}
      </main>

      {/* Keyboard Shortcut Hint Toast - 100% English */}
      {showShortcutHint && (
        <div className="no-print fixed bottom-4 left-4 bg-slate-900/90 border border-amber-500/30 text-xs text-slate-300 px-3 py-2 rounded-xl backdrop-blur-md shadow-lg flex items-center gap-2 z-20">
          <Keyboard className="w-4 h-4 text-amber-400" />
          <span>Use <b>← →</b> for slides | <b>P</b> for Presenter | <b>M</b> for Overview | <b>Export PDF</b> to save</span>
          <button 
            onClick={() => setShowShortcutHint(false)}
            className="text-slate-500 hover:text-white ml-1 font-bold"
          >
            ×
          </button>
        </div>
      )}

      {/* Grid Overview Modal */}
      {isOverviewOpen && (
        <SlideOverviewModal
          slides={currentSlides}
          currentSlide={currentSlideIndex + 1}
          onSelectSlide={handleSelectSlide}
          onClose={() => setIsOverviewOpen(false)}
        />
      )}
    </div>
  );
}
