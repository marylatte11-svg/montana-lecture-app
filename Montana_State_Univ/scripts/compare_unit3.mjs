import { MONTANA_ALL_SLIDES } from '../../src/data/montanaSlidesData.js';
import fs from 'fs';

let output = '';

for (let lec = 31; lec <= 45; lec++) {
  const slides = MONTANA_ALL_SLIDES[lec];
  output += `\n========================================\n`;
  output += `LECTURE ${lec} (${slides.length} slides)\n`;
  output += `========================================\n`;
  
  for (const s of slides) {
    output += `\n--- Slide ${s.num}: ${s.title} ---\n`;
    output += `[Problem]:\n${s.problem ? s.problem.slice(0, 200) : 'None'}\n`;
    output += `[Script]:\n${s.script ? s.script.slice(0, 300) : 'None'}\n`;
  }
}

fs.writeFileSync('Montana_State_Univ/scripts/unit3_comparison.txt', output, 'utf-8');
console.log('Unit 3 detailed comparison written to Montana_State_Univ/scripts/unit3_comparison.txt');
