import { MONTANA_ALL_SLIDES } from '../../src/data/montanaSlidesData.js';
import fs from 'fs';

let issues = [];

for (let lec = 1; lec <= 45; lec++) {
  const slides = MONTANA_ALL_SLIDES[lec];
  if (!slides) continue;
  
  for (const s of slides) {
    if (s.num === 1) continue; // Skip intro slide
    if (s.title.includes('Recap') || s.title.includes('Summary') || s.title.includes('Congratulations')) continue;
    
    const title = s.title;
    const prob = s.problem || '';
    const sol = s.solution || '';
    const script = s.script || '';
    
    // Check if script mentions the core title or problem
    // Let's inspect L41, L42, L43, L44, L45
    // Also inspect L31-L40
    // Also inspect L1-L30
    
    // Test heuristic: extract first equation from problem, e.g. "x^2 + 6x = 0"
    const m = prob.match(/\$\$([^$]+)\$\$/);
    if (m) {
      const eq = m[1].replace(/\s+/g, '').replace(/\\quad/g, '').replace(/\\text\{[^}]+\}/g, '');
      const scriptClean = script.replace(/\s+/g, '');
      
      // If the equation has at least 4 characters and isn't found in script:
      if (eq.length >= 5 && !scriptClean.includes(eq.slice(0, 5))) {
        issues.push({
          lec,
          slide: s.num,
          title,
          expectedInScript: eq.slice(0, 15),
          scriptHead: script.slice(0, 120).replace(/\n/g, ' ')
        });
      }
    }
  }
}

console.log(`Potential issues found: ${issues.length}`);
for (const iss of issues) {
  console.log(`L${iss.lec} S${iss.slide}: [${iss.title}]`);
  console.log(`   Expected pattern: ${iss.expectedInScript}`);
  console.log(`   Script actual: ${iss.scriptHead}\n`);
}
