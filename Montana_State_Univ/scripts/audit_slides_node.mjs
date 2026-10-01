import { MONTANA_ALL_SLIDES, MONTANA_LECTURES } from '../../src/data/montanaSlidesData.js';

console.log(`Total lectures in MONTANA_ALL_SLIDES: ${Object.keys(MONTANA_ALL_SLIDES).length}`);

for (const lecId of Object.keys(MONTANA_ALL_SLIDES)) {
  const slides = MONTANA_ALL_SLIDES[lecId];
  console.log(`\n=== Lecture ${lecId} (${slides.length} slides) ===`);
  for (const s of slides) {
    const scriptStart = s.script ? s.script.slice(0, 100).replace(/\n/g, ' ') : 'NO SCRIPT';
    console.log(`  S${s.num}: [Title: ${s.title}] -> [Script: ${scriptStart}...]`);
  }
  if (parseInt(lecId) >= 5 && parseInt(lecId) <= 40) {
    // only show sampling if too many
  }
}
