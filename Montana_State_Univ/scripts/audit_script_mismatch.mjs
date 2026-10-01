import { MONTANA_ALL_SLIDES } from '../../src/data/montanaSlidesData.js';

const issues = [];

for (let l = 1; l <= 45; l++) {
  const slides = MONTANA_ALL_SLIDES[l.toString()] || [];
  slides.forEach((s, idx) => {
    const slideNum = idx + 1;
    const title = s.title || '';
    const prob = s.problem || '';
    const scr = s.script || '';

    // Check if problem contains specific equations like 'g(x) = ...' or 'h(x) = ...' or 'f(x) = ...'
    const funcMatches = [
      ...title.matchAll(/([fghp]\(x\)\s*=\s*[^,:\$\)]+)/gi),
      ...prob.matchAll(/([fghp]\(x\)\s*=\s*[^,:\$\)\n]+)/gi)
    ];

    for (const fm of funcMatches) {
      let fnExpr = fm[1].trim().replace(/[\$\*\\]/g, '').replace(/\s+/g, '');
      fnExpr = fnExpr.replace(/[.,;]+$/, '');
      if (fnExpr.length > 5 && !scr.replace(/\s+/g, '').includes(fnExpr)) {
        const rhs = fnExpr.split('=')[1];
        if (rhs && !scr.replace(/\s+/g, '').includes(rhs)) {
          issues.push({
            lec: l,
            slide: slideNum,
            title: title,
            expr: fnExpr,
            scriptSnippet: scr.substring(0, 100)
          });
          break;
        }
      }
    }
  });
}

console.log('Total potential mismatches:', issues.length);
for (const iss of issues) {
  console.log(`L${iss.lec} S${iss.slide}: ${iss.title}`);
  console.log(`  Target Expr: ${iss.expr}`);
  console.log(`  Script snippet: ${iss.scriptSnippet.replace(/\n/g, ' ')}`);
}
