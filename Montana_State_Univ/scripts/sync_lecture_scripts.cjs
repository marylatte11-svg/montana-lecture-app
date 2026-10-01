const fs = require('fs');

// Script to sync all 15 lectures from montanaSlidesData.js into Montana_State_Univ/lectures/lectureXX.md
const data = fs.readFileSync('src/data/montanaSlidesData.js', 'utf8');

for (let i = 1; i <= 30; i++) {
  const pad = i < 10 ? '0' + i : '' + i;
  const startTag = `export const SLIDES_MONTANA_L${pad} = [`;
  const nextTag = i < 30 ? `export const SLIDES_MONTANA_L${i < 9 ? '0' + (i + 1) : '' + (i + 1)} = [` : 'export const MONTANA_ALL_SLIDES';
  
  const startIdx = data.indexOf(startTag);
  const endIdx = data.indexOf(nextTag);
  if (startIdx === -1 || endIdx === -1) continue;
  
  const arrayCode = data.slice(startIdx + startTag.length - 1, endIdx).trim().replace(/;$/, '');
  
  let slides;
  try {
    slides = JSON.parse(arrayCode);
  } catch (e) {
    console.error(`Error parsing L${pad}:`, e.message);
    continue;
  }
  
  let md = `# Montana State University - Gallatin College\n`;
  md += `## M090 Introductory Algebra — Lecture ${pad}\n`;
  md += `**Instructors:** Prof. Eunju Park & TA Sora (Gallatin College MSU)\n`;
  md += `**Workbook Source:** M090 Full Student Workbook\n\n`;
  md += `---\n\n`;
  
  slides.forEach((s) => {
    md += `### [Slide ${s.num}] ${s.title}\n`;
    md += `*${s.subtitle}*\n\n`;
    if (s.problem) {
      md += `#### 📖 Official Workbook Problem\n${s.problem}\n\n`;
    }
    if (s.solution) {
      md += `#### 💡 Complete Step-by-Step Solution\n${s.solution}\n\n`;
    }
    if (s.pitfall) {
      md += `#### ⚠️ Pitfall & Strategy\n${s.pitfall}\n\n`;
    }
    if (s.script) {
      md += `#### 🎙️ Lecture Dialogue (Prof. Park & TA Sora)\n${s.script}\n\n`;
    }
    md += `---\n\n`;
  });
  
  fs.writeFileSync(`Montana_State_Univ/lectures/lecture${pad}.md`, md, 'utf8');
  console.log(`Updated Montana_State_Univ/lectures/lecture${pad}.md (${slides.length} slides)`);
}
