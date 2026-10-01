import React from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import TitleSlide from './slides/TitleSlide';
import SectionSlide from './slides/SectionSlide';
import ComparisonSlide from './slides/ComparisonSlide';
import TriadSlide from './slides/TriadSlide';
import MetricSlide from './slides/MetricSlide';
import EfficiencyChartSlide from './slides/EfficiencyChartSlide';
import InteractivePollSlide from './slides/InteractivePollSlide';
import ArchitectureSlide from './slides/ArchitectureSlide';
import MottoSlide from './slides/MottoSlide';
import MathSlide from './slides/MathSlide';

export default function SlideDeck({ slideData }) {
  const renderSlideContent = () => {
    if (slideData.problem || slideData.solution || slideData.type === 'math_problem') {
      return <MathSlide slideData={slideData} />;
    }
    switch (slideData.type) {
      case 'title':
        return <TitleSlide slideData={slideData} />;
      case 'section':
        return <SectionSlide slideData={slideData} />;
      case 'comparison':
        return <ComparisonSlide slideData={slideData} />;
      case 'triad':
        return <TriadSlide slideData={slideData} />;
      case 'metric':
        return <MetricSlide slideData={slideData} />;
      case 'chart_efficiency':
      case 'chart_case_study':
        return <EfficiencyChartSlide slideData={slideData} />;
      case 'poll':
        return <InteractivePollSlide slideData={slideData} />;
      case 'architecture':
        return <ArchitectureSlide slideData={slideData} />;
      case 'motto':
      default:
        return <MottoSlide slideData={slideData} />;
    }
  };

  return (
    <div className="w-full h-full relative overflow-hidden bg-gradient-to-br from-[#0B132B] via-[#0F172A] to-[#090D16] flex flex-col justify-center">
      <AnimatePresence mode="wait">
        <motion.div
          key={slideData.num}
          initial={{ opacity: 0, scale: 0.98 }}
          animate={{ opacity: 1, scale: 1 }}
          exit={{ opacity: 0, scale: 1.02 }}
          transition={{ duration: 0.25, ease: 'easeOut' }}
          className="w-full h-full max-w-[98vw] 2xl:max-w-[1880px] mx-auto flex flex-col justify-center px-1 md:px-3 py-1"
        >
          {renderSlideContent()}
        </motion.div>
      </AnimatePresence>
    </div>
  );
}
