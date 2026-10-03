import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const baseDir = path.resolve(__dirname, '..');

const montanaPath = path.join(baseDir, 'src/data/montanaSlidesData.js');
const { MONTANA_ALL_SLIDES, MONTANA_LECTURES } = await import(`file://${montanaPath.replace(/\\/g, '/')}`);

console.log(`Loaded MONTANA_LECTURES: ${MONTANA_LECTURES.length} lectures.`);

let totalSlides = 0;
const candidates = [];

for (let l = 1; l <= 45; l++) {
  const slides = MONTANA_ALL_SLIDES[l] || [];
  totalSlides += slides.length;

  slides.forEach((s) => {
    const prob = s.problem || '';
    // Check if problem starts with $$ and has \text{ and math formula without 2-line separation
    if (prob.startsWith('$$') && prob.includes('\\text{') && !prob.includes('\n\n$$')) {
      // Check if there is formula outside \text{} or inside
      candidates.push({
        lecture: l,
        slide: s.num,
        title: s.title,
        problem: prob
      });
    } else if (prob.startsWith('$$') && prob.length > 80 && !prob.includes('\n\n$$') && prob.includes('\\quad')) {
      candidates.push({
        lecture: l,
        slide: s.num,
        title: s.title,
        problem: prob
      });
    }
  });
}

console.log(`Total Slides across all 45 lectures: ${totalSlides}`);
console.log(`Slides with single-line text+math in problem: ${candidates.length}`);

candidates.forEach((c) => {
  console.log(`L${String(c.lecture).padStart(2, '0')} S${String(c.slide).padStart(2, '0')}: [${c.title}] -> ${c.problem.slice(0, 80)}...`);
});
