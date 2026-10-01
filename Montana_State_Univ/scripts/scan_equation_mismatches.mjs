import { MONTANA_ALL_SLIDES } from '../../src/data/montanaSlidesData.js';

const allMismatches = [];

for (let lec = 1; lec <= 45; lec++) {
  const slides = MONTANA_ALL_SLIDES[lec];
  if (!slides) continue;
  
  for (const s of slides) {
    // Only check problem slides (num >= 2 usually, or non-intro)
    if (s.slideTypeLabel && s.slideTypeLabel.includes('Intro')) continue;
    if (s.title && (s.title.includes('Recap') || s.title.includes('Summary') || s.title.includes('Formula Card') || s.title.includes('Congratulations'))) continue;
    
    const prob = s.problem || '';
    const script = s.script || '';
    const title = s.title || '';
    
    // Check key math identifiers
    // Look for equations in problem
    // Regex for quadratic/linear equations: e.g. "g(x) = ...", "x^2 + ...", or "Problem N"
    // Let's check if the specific function name or equation in problem is mentioned in script
    const funcMatch = prob.match(/([fghpqr]\(x\)\s*=\s*[^$\n\\]+)/);
    if (funcMatch) {
      const eq = funcMatch[1].replace(/\s+/g, '');
      const scriptClean = script.replace(/\s+/g, '');
      // Check if equation core appears in script
      // e.g. "x^2+6x"
      const coreParts = eq.split('=');
      const rhs = coreParts[1] ? coreParts[1].replace(/\\/g, '') : '';
      if (rhs.length >= 4 && !scriptClean.includes(rhs)) {
        allMismatches.push({
          lec,
          slide: s.num,
          title: s.title,
          problemEq: funcMatch[1],
          scriptSnippet: script.slice(0, 160).replace(/\n/g, ' ')
        });
      }
    }
  }
}

console.log(`Found ${allMismatches.length} slides where problem equation is missing in script:`);
for (const m of allMismatches) {
  console.log(`L${m.lec} S${m.slide}: ${m.title}`);
  console.log(`   Expected in script: [${m.problemEq}]`);
  console.log(`   Script actual snippet: [${m.scriptSnippet}]`);
}
