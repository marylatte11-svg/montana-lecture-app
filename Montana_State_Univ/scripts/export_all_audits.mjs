import { MONTANA_ALL_SLIDES, MONTANA_LECTURES } from '../../src/data/montanaSlidesData.js';
import fs from 'fs';

const report = [];

for (const lecId of Object.keys(MONTANA_ALL_SLIDES)) {
  const slides = MONTANA_ALL_SLIDES[lecId];
  for (const s of slides) {
    // Extract title, problem formula
    const title = s.title || '';
    const prob = s.problem || '';
    const script = s.script || '';
    
    // Check if script matches the problem
    report.push({
      lec: parseInt(lecId),
      slide: s.num,
      title: title,
      problemShort: prob.slice(0, 150).replace(/\n/g, ' '),
      scriptShort: script.slice(0, 200).replace(/\n/g, ' ')
    });
  }
}

fs.writeFileSync('Montana_State_Univ/scripts/full_slide_script_audit.json', JSON.stringify(report, null, 2));
console.log(`Audited ${report.length} total slides. Written to full_slide_script_audit.json`);
