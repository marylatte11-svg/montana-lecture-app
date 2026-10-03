import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const baseDir = path.resolve(__dirname, '../..');

const lectureId = parseInt(process.argv[2] || '1', 10);
const montanaPath = path.join(baseDir, 'src/data/montanaSlidesData.js');

const { MONTANA_ALL_SLIDES } = await import(`file://${montanaPath.replace(/\\/g, '/')}`);
const slides = MONTANA_ALL_SLIDES[lectureId] || [];

const outPath = path.join(__dirname, `lecture_${lectureId}_slides.json`);
fs.writeFileSync(outPath, JSON.stringify(slides, null, 2), 'utf-8');
console.log(`Exported ${slides.length} slides for Lecture ${lectureId} to ${outPath}`);
