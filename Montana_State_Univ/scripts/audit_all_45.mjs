import { MONTANA_ALL_SLIDES } from '../../src/data/montanaSlidesData.js';
import fs from 'fs';

function checkUnit(unitNum, startLec, endLec) {
  let issues = [];
  for (let lec = startLec; lec <= endLec; lec++) {
    const slides = MONTANA_ALL_SLIDES[lec];
    for (const s of slides) {
      const prob = (s.problem || '').toLowerCase();
      const title = (s.title || '').toLowerCase();
      const script = (s.script || '').toLowerCase();
      
      // Let's check if the slide has a specific exercise/equation that is completely missing in the script
      // Or if the script starts with an entirely different problem
    }
  }
}

// Check Lectures 1 to 45 specifically looking for equations in problem vs script
let auditLog = '';
for (let lec = 1; lec <= 45; lec++) {
  const slides = MONTANA_ALL_SLIDES[lec];
  for (const s of slides) {
    // Look at first 200 chars of script
    const head = s.script ? s.script.slice(0, 250).replace(/\n/g, ' ') : '';
    auditLog += `L${lec} S${s.num} | Title: ${s.title}\n   Problem: ${(s.problem || '').slice(0, 100).replace(/\n/g, ' ')}\n   Script: ${head}\n\n`;
  }
}

fs.writeFileSync('Montana_State_Univ/scripts/all_45_lectures_audit.txt', auditLog, 'utf-8');
console.log('Saved all_45_lectures_audit.txt');
