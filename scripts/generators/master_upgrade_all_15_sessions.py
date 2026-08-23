# -*- coding: utf-8 -*-
"""
Master 15-Session Curriculum Upgrade Engine
Course: The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom
Oikos University (www.oikos.edu) • Smart Insight Lab

Upgrades ALL 15 Sessions (675 slides) to:
- 7~10 Conversational turns per slide (Authentic NotebookLM Podcast Tikitaka)
- Natural ping-pong between Prof. Peter Kim, TA Sarah Jenkins, TA James Wilson
- 5 Enterprise Case Studies per session (75 total case studies)
- 4-Part clean architecture per session
- Full markdown generation for session1.md ~ session15.md
- Full synchronization with src/data/slidesData.js (SLIDES_SESSION_1 ~ SLIDES_SESSION_15)
"""

import os
import sys
import json
import re
import importlib.util

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Oikos Univ"
SLIDES_DATA_JS = os.path.join(BASE_DIR, "src", "data", "slidesData.js")

SESSION_TITLES = {
    1: "The Paradigm Shift: Chatbots to Autonomous Avatars",
    2: "24/7 Sleep-Free Guardian: Gemini Spark Architecture",
    3: "The Battle for the OS Shell: Windows Dominance and the 1.2GB Trojan Horse",
    4: "Grounded Intelligence on My Data: The RAG Revolution and Private Knowledge Factories",
    5: "Sovereign Cloud Architecture: Google Drive, Apps Script & Life OS Automation",
    6: "The Autonomous Dev Environment: WebMCP, CLI Mastery & Self-Directing Workspaces",
    7: "Agentic Orchestration: Subagents, Skills & Multi-Agent Swarms",
    8: "Agentic Knowledge Systems: KI Architecture & Autonomous Context Synthesis",
    9: "Agentic Multimodal Automation: Browser Subagents, Live DOM & Headless Workflows",
    10: "Enterprise Red-Teaming & Guardrails: MCP Security, Zero-Data Retention & Canary Defense",
    11: "Quantitative Tokenomics & Economic Arbitrage: SLM Routing, Speculative Decoding & 95% Cost Cut",
    12: "Autonomous Software Synthesis: AST Refactoring, Git Daemon Automation & Zero-Defect CI/CD",
    13: "High-Fidelity Multimodal UI: SVG Mastery, Dynamic LaTeX & Zero-Loss Visual Pipelines",
    14: "Cinematic AI Pipelines: Flow AI vs Runway ML",
    15: "The Grand Synthesis: The Sovereign Life OS, Soli Deo Gloria & The Architect's Commission"
}

def load_session_slides(session_num):
    gen_file = os.path.join(BASE_DIR, "scripts", "generators", f"build_clean_session{session_num}_45_slides.py")
    if not os.path.exists(gen_file):
        return None
    spec = importlib.util.spec_from_file_location(f"s{session_num}", gen_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    
    # Check possible variable names
    candidates = [
        f"SLIDES_45_SESSION_{session_num}_VIBRANT",
        f"SLIDES_45_SESSION_{session_num}",
        f"SLIDES_{session_num}_45",
        "SLIDES_45",
        f"SLIDES_SESSION_{session_num}"
    ]
    for c in candidates:
        if hasattr(mod, c):
            return getattr(mod, c)
            
    for k in dir(mod):
        if k.startswith("SLIDES_"):
            val = getattr(mod, k)
            if isinstance(val, list) and len(val) == 45:
                return val
    return None

def enrich_script_to_podcast_tikitaka(slide, session_num):
    raw_script = slide.get('script', '')
    turns = re.findall(r'\[(Prof\. Peter|TA Sarah|TA James)\]', raw_script)
    
    # If already 7+ turns with rich banter, keep as is
    if len(turns) >= 7:
        return raw_script

    title = slide.get('title', '')
    subtitle = slide.get('subtitle', '')
    num = slide.get('num', 1)
    
    if num == 1:
        new_turns = [
            f"[Prof. Peter] Welcome, global scholars and engineering leaders, to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today on Slide 1, we embark on: \"Session {session_num}: {title}.\"",
            f"[TA Sarah] Hey everyone, Sarah Jenkins here! You know, James, when engineers look at Slide 1, they often ask: why is this specific module such a critical pillar of the sovereign architecture?",
            f"[TA James] Haha, that's simple, Sarah! Because in real production, if you don't master this layer, your entire autonomous stack collapses under real-world enterprise pressure!",
            f"[TA Sarah] Exactly! We're moving beyond basic tutorials and building hardened, production-grade intelligence that runs 24/7 with zero downtime!",
            f"[TA James] And we back it up with real code, real infrastructure patterns, and proven enterprise ROI!",
            f"[Prof. Peter] Under our sacred cornerstone, \"SOLI DEO GLORIA—To God Alone Be the Glory,\" our mission is to redeem the time (Ephesians 5:16) and steward technology for human flourishing.",
            f"[TA Sarah] That's right! Let us open Part 1 on Slide 2 and dive into the architecture!"
        ]
    elif slide.get('type') == 'section':
        new_turns = [
            f"[TA Sarah] Look at Slide {num}: \"{title}.\" James, this module marks a vital transition in our master curriculum!",
            f"[TA James] Oh, absolutely, Sarah! In this part, we roll up our sleeves and look straight under the engineering hood!",
            f"[TA Sarah] What is the biggest trap that junior architects fall into during this phase?",
            f"[TA James] Relying on fragile, synchronous scripts that crash the moment an external API slows down, instead of building resilient, asynchronous event-driven pipelines!",
            f"[Prof. Peter] A wise builder digs deep and lays the foundation on solid rock. We engineer every subsystem with unwavering discipline and architectural integrity.",
            f"[TA Sarah] That is why in this module, we dissect every layer with scientific precision.",
            f"[TA James] Let's jump straight into the first core concept on Slide {num + 1}!"
        ]
    elif slide.get('type') == 'casestudy':
        comp = slide.get('company', 'Enterprise Partner')
        prob = slide.get('problem', '')
        sol = slide.get('solution', '')
        imp = slide.get('impact', '')
        new_turns = [
            f"[Prof. Peter] Slide {num} presents \"{title}.\" Sarah, walk us through the high-stakes operational crisis this organization faced.",
            f"[TA Sarah] Look at {comp}: {prob}",
            f"[TA James] Man, that is every infrastructure lead's absolute worst nightmare! If a production cluster drops like that, you're losing tens of thousands of dollars per minute!",
            f"[TA Sarah] So instead of patching with band-aids, they deployed our Oikos University architecture: {sol}",
            f"[TA James] And look at the verified enterprise metrics on screen: {imp}",
            f"[TA Sarah] That is the transformative power of sovereign agentic engineering in real production!",
            f"[TA James] Zero guesswork, total auditability, and massive ROI!",
            f"[Prof. Peter] When intelligence is grounded in truth, it preserves human dignity and unlocks extraordinary stewardship. Soli Deo Gloria!"
        ]
    elif slide.get('type') == 'lab':
        new_turns = [
            f"[TA Sarah] Here we are at Slide {num}: \"{title}!\"",
            f"[TA James] Tonight's hands-on lab is where theory becomes reality! Look at our 5-step mission on screen: we are taking everything we mastered today and building it live in code!",
            f"[TA Sarah] Remember: test each component in isolation first, verify your security keys, and inspect your real-time execution logs!",
            f"[TA James] James and I will be holding lab office hours to help you optimize your pipelines and crush every bug!",
            f"[Prof. Peter] As we always proclaim at Oikos University: Knowledge without practice is inert, but practiced wisdom dedicated to God's glory transforms the world.",
            f"[TA Sarah] In our next session, we will push our architectural capabilities even further into the sovereign frontier!",
            f"[TA James] Don't wait until tomorrow—fire up your terminal tonight, run your tests, and redeem your time!",
            f"[Prof. Peter] On behalf of TA Sarah Jenkins, TA James Wilson, and Smart Insight Lab: Thank you for your dedication. Soli Deo Gloria! Class dismissed in victory!"
        ]
    else:
        points_text = " • ".join(slide.get('points', [])) if slide.get('points') else subtitle
        new_turns = [
            f"[TA Sarah] Slide {num} explores \"{title}.\" James, why is this concept so essential for every serious AI architect?",
            f"[TA James] Because, Sarah, if you ignore this layer, your entire system degrades under enterprise load! Look at the core challenge on screen: {subtitle}",
            f"[TA Sarah] Exactly! When you analyze the engineering details: {points_text}",
            f"[TA James] Haha, I remember testing an unoptimized prototype without this exact safeguard, and my server memory spiked to 98% in 30 seconds!",
            f"[TA Sarah] That's why we enforce strict architectural boundaries: decoupling state, caching hot paths, and verifying every payload!",
            f"[TA James] It transforms a brittle, high-latency prototype into a sub-second, rock-solid production engine!",
            f"[Prof. Peter] Order and discipline are the hallmarks of true mastery. In all our designs, we reflect the structured wisdom of the Creator.",
            f"[TA Sarah] Let us inspect the next evolutionary step on Slide {num + 1}!"
        ]
        
    return "\n\n".join(new_turns)

def generate_session_md(session_num, title, slides):
    lines = []
    lines.append(f"# Session {session_num}: {title}")
    lines.append("**Course:** The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom  ")
    lines.append("**Instructors:** Professor Peter Kim (Director), TA Sarah Jenkins (Senior AI Fellow) & TA James Wilson (DevOps TA) • Oikos University (www.oikos.edu)  ")
    lines.append("**Lecture Format:** Full 75-Minute Broadcast Trio Master Dialogue (4x Modules with 5 Enterprise Case Studies)  ")
    lines.append("**Total Slides:** 45 Slides (Expanded Multi-Presenter Master Edition)  ")
    lines.append("**Motto:** Soli Deo Gloria  ")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📌 Table of Contents (목차)")
    
    for s in slides:
        num_str = f"{s['num']:02d}"
        t = s['title']
        slug = f"slide-{num_str}-{t.lower().replace(' ', '-').replace(':', '').replace('.', '').replace('&', 'and').replace('(', '').replace(')', '').replace('•', '').replace('\'', '').replace('’', '').replace('/', '-')}"
        slug = re.sub(r'-+', '-', slug).strip('-')
        lines.append(f"- [Slide {num_str}: {t}](#{slug})")
        
    lines.append("")
    lines.append("---")
    lines.append("")
    
    for s in slides:
        num_str = f"{s['num']:02d}"
        lines.append(f"## Slide {num_str}: {s['title']}")
        if s.get('subtitle'):
            lines.append(f"**Subtitle:** {s['subtitle']}")
        lines.append(f"**Instructor:** Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab")
        lines.append("")
        
        lines.append("### 🎙️ English Lecture Script (Full 75-Min Broadcast Trio Dialogue)")
        lines.append(s['script'])
        lines.append("")
        
        lines.append("### 🇰🇷 한국어 강의 가이드 및 핵심 요약")
        kg = s.get('koreanGuide', {})
        lines.append(f"**개요 요약:** {kg.get('summary', '')}")
        lines.append("")
        lines.append("**핵심 티칭 포인트:**")
        for pt in kg.get('points', []):
            lines.append(f"- {pt}")
        lines.append("")
        lines.append(f"**강의 전달 팁:** {kg.get('tips', '')}")
        lines.append("")
        
        if s.get('keyTerms'):
            lines.append("### 📚 Key Technical Terms (핵심 용어)")
            for kt in s['keyTerms']:
                lines.append(f"- **{kt.get('term', '')}** ({kt.get('defKo', '')}): {kt.get('def', '')}")
            lines.append("")
            
        lines.append("---")
        lines.append("")
        
    md_path = os.path.join(BASE_DIR, f"session{session_num}.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"✅ Generated {md_path}")

def update_slides_data_js_for_session(session_num, slides):
    with open(SLIDES_DATA_JS, 'r', encoding='utf-8') as f:
        content = f.read()

    slides_json = json.dumps(slides, ensure_ascii=False, indent=2)
    new_export = f"export const SLIDES_SESSION_{session_num} = {slides_json};"
    
    pattern = rf"export\s+const\s+SLIDES_SESSION_{session_num}\s*=\s*\[[\s\S]*?\];"
    if re.search(pattern, content):
        updated_content = re.sub(pattern, lambda m: new_export, content, count=1)
        with open(SLIDES_DATA_JS, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"✅ Updated SLIDES_SESSION_{session_num} in slidesData.js")
    else:
        print(f"❌ Failed to find SLIDES_SESSION_{session_num} in slidesData.js")

def main():
    print("=================================================================")
    print("🏛️ OIKOS UNIVERSITY: MASTER 15-SESSION PODCAST TIKITAKA UPGRADE")
    print("=================================================================")
    
    success_count = 0
    for s_num in range(1, 16):
        title = SESSION_TITLES.get(s_num, f"Session {s_num}")
        print(f"\n[Processing Session {s_num:2d}/15] {title}...")
        
        slides = load_session_slides(s_num)
        if not slides:
            print(f"❌ Error: Could not load slides for Session {s_num}")
            continue
            
        # Enrich all 45 slides
        for s in slides:
            s['script'] = enrich_script_to_podcast_tikitaka(s, s_num)
            
        # Write session{N}.md
        generate_session_md(s_num, title, slides)
        
        # Update slidesData.js
        update_slides_data_js_for_session(s_num, slides)
        
        success_count += 1
        
    print(f"\n=================================================================")
    print(f"🎉 MASTER UPGRADE COMPLETED: {success_count}/15 Sessions Processed!")
    print("=================================================================")

if __name__ == '__main__':
    main()
