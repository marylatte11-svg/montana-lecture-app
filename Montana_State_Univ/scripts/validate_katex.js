import katex from 'katex';
import { MONTANA_ALL_SLIDES } from '../../src/data/montanaSlidesData.js';

let totalErrors = 0;

function checkMath(str, slideNum, field) {
  if (!str || typeof str !== 'string') return;

  // Check display math $$...$$
  const displayRegex = /\$\$([\s\S]*?)\$\$/g;
  let m;
  while ((m = displayRegex.exec(str)) !== null) {
    const math = m[1].trim();
    try {
      katex.renderToString(math, { displayMode: true, throwOnError: true });
    } catch (e) {
      totalErrors++;
      console.log(`[Slide ${slideNum}] Display Error in ${field}: ${e.message}`);
      console.log(`Snippet: ${math.substring(0, 120)}...\n`);
    }
  }

  // Check inline math $...$
  const inlineRegex = /\$([^\$]+?)\$/g;
  while ((m = inlineRegex.exec(str)) !== null) {
    const math = m[1].trim();
    try {
      katex.renderToString(math, { displayMode: false, throwOnError: true });
    } catch (e) {
      totalErrors++;
      console.log(`[Slide ${slideNum}] Inline Error in ${field}: ${e.message}`);
      console.log(`Snippet: ${math}\n`);
    }
  }
}

for (const [lectureId, slides] of Object.entries(MONTANA_ALL_SLIDES || {})) {
  for (const slide of slides) {
    checkMath(slide.title, slide.num, `L${lectureId} title`);
    checkMath(slide.problem, slide.num, `L${lectureId} problem`);
    checkMath(slide.solution, slide.num, `L${lectureId} solution`);
    checkMath(slide.pitfall, slide.num, `L${lectureId} pitfall`);
  }
}

console.log(`Validation complete. Total KaTeX errors found: ${totalErrors}`);
