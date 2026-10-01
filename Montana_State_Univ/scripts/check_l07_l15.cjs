const fs = require('fs');

const content = fs.readFileSync('src/data/montanaSlidesData.js', 'utf8');

for (let num = 7; num <= 15; num++) {
  const pad = num < 10 ? '0' + num : '' + num;
  const startTag = `export const SLIDES_MONTANA_L${pad} = [`;
  const nextTag = num < 15 ? `export const SLIDES_MONTANA_L${num < 9 ? '0' + (num + 1) : '' + (num + 1)} = [` : 'export const MONTANA_ALL_SLIDES';
  const startIdx = content.indexOf(startTag);
  const endIdx = content.indexOf(nextTag);
  const slice = content.slice(startIdx, endIdx);
  
  console.log(`\n================== LECTURE ${pad} ==================`);
  
  // Extract slide objects roughly
  const matches = slice.match(/\{\s*"num":\s*\d+,[\s\S]*?"script":\s*"[\s\S]*?"\s*\}/g);
  if (!matches) {
    console.log('No slides parsed');
    continue;
  }
  
  matches.forEach(s => {
    try {
      const obj = JSON.parse(s);
      console.log(`Slide ${obj.num}: [${obj.slideTypeLabel}] ${obj.title}`);
      console.log(`   Subtitle: ${obj.subtitle}`);
      console.log(`   Problem: ${obj.problem ? obj.problem.replace(/\n/g, ' ') : '(none)'}`);
    } catch (e) {
      // If JSON.parse fails due to escaping, print title
      const titleMatch = s.match(/"title":\s*"([^"]+)"/);
      const subMatch = s.match(/"subtitle":\s*"([^"]+)"/);
      const probMatch = s.match(/"problem":\s*"([^"]*)"/);
      console.log(`Slide (raw): ${titleMatch ? titleMatch[1] : 'unknown'} | ${subMatch ? subMatch[1] : ''}`);
      if (probMatch) console.log(`   Problem: ${probMatch[1].slice(0, 100)}...`);
    }
  });
}
