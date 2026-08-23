# -*- coding: utf-8 -*-
"""
Batch 1 Master Upgrade: Sessions 1, 2, 3, 5 Ultra-Dense Podcast Tikitaka Generator
Based on design_oikos.md and authentic NotebookLM podcast structures in c:\smartinsightlab.
Upgrades every slide to 7~10 conversational turns with dynamic ping-pong, humor, DevOps war stories,
and theological grounding under Soli Deo Gloria.
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

def load_session_slides(session_num):
    gen_file = os.path.join(BASE_DIR, "scripts", "generators", f"build_clean_session{session_num}_45_slides.py")
    spec = importlib.util.spec_from_file_location(f"s{session_num}", gen_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    slides_var = getattr(mod, f"SLIDES_45_SESSION_{session_num}", None) or getattr(mod, "SLIDES_45", None)
    return slides_var

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
        print(f"✅ Successfully updated SLIDES_SESSION_{session_num} in slidesData.js!")
    else:
        print(f"❌ Could not find pattern for SLIDES_SESSION_{session_num} in slidesData.js!")

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
    print(f"✅ Successfully wrote {md_path}")

def enrich_script_to_podcast_tikitaka(slide, session_num):
    """
    Ensures script has 7~10 fast, dynamic turns with lively podcast banter.
    If turns are less than 7, automatically expands with authentic ping-pong exchanges.
    """
    raw_script = slide.get('script', '')
    turns = re.findall(r'\[(Prof\. Peter|TA Sarah|TA James)\]', raw_script)
    
    # If already 7+ turns with rich banter, return as is
    if len(turns) >= 7:
        return raw_script

    # Otherwise enrich based on slide type and title
    title = slide.get('title', '')
    subtitle = slide.get('subtitle', '')
    num = slide.get('num', 1)
    
    # Extract existing speaker content
    blocks = []
    current_speaker = None
    current_text = []
    
    for line in raw_script.split('\n'):
        line_clean = line.strip()
        m = re.match(r'^\[(Prof\. Peter|TA Sarah|TA James)\]\s*(.*)$', line_clean)
        if m:
            if current_speaker:
                blocks.append((current_speaker, ' '.join(current_text)))
            current_speaker = m.group(1)
            current_text = [m.group(2)] if m.group(2) else []
        elif line_clean:
            current_text.append(line_clean)
    if current_speaker:
        blocks.append((current_speaker, ' '.join(current_text)))
        
    # Rebuild as vibrant 7~10 turn podcast dialogue
    new_turns = []
    if num == 1:
        new_turns = [
            f"[Prof. Peter] Welcome, global scholars and engineering leaders, to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today on Slide 1, we inaugurate: \"Session {session_num}: {title}.\"",
            f"[TA Sarah] Hey everyone, Sarah Jenkins here! You know, James, when students look at Slide 1, they often wonder: what makes this curriculum fundamentally different from every other AI tutorial on YouTube?",
            f"[TA James] Haha, that's simple, Sarah! Regular tutorials teach you how to type prompts into a browser tab and wait like a robot. We teach you how to build 24/7 autonomous production systems that run while you sleep!",
            f"[TA Sarah] Exactly! We're not training prompt typists; we're training certified Intelligence Architects who command distributed agents, secure shell pipelines, and private knowledge vaults!",
            f"[TA James] And we do it with zero fluff—real code, real infrastructure, real enterprise case studies!",
            f"[Prof. Peter] Under our sacred cornerstone, \"SOLI DEO GLORIA—To God Alone Be the Glory,\" our ultimate aim is to redeem the time (Ephesians 5:16) and steward technology for human flourishing.",
            f"[TA Sarah] That's right! Let us open Part 1 on Slide 2 and begin our journey!"
        ]
    elif slide.get('type') == 'section':
        new_turns = [
            f"[TA Sarah] Look at Slide {num}: \"{title}.\" James, this marks a massive turning point in our architectural roadmap!",
            f"[TA James] Oh, absolutely, Sarah! In this module, we move past the theoretical hype and get our hands dirty in real engineering!",
            f"[TA Sarah] What is the single biggest bottleneck that engineers face when entering this phase?",
            f"[TA James] Trying to solve 2026 problems with 2020 tools! People try to hack together brittle Python scripts that crash on the first edge case instead of building resilient, self-healing pipelines!",
            f"[Prof. Peter] A house built on sand cannot withstand the storm. We must architect every subsystem on unbreakable principles of integrity and order.",
            f"[TA Sarah] That is why in this module, we dissect the core mechanics piece by piece.",
            f"[TA James] Let's jump straight into the first core concept on Slide {num + 1}!"
        ]
    elif slide.get('type') == 'casestudy':
        comp = slide.get('company', 'Enterprise Partner')
        prob = slide.get('problem', '')
        sol = slide.get('solution', '')
        imp = slide.get('impact', '')
        new_turns = [
            f"[Prof. Peter] Slide {num} presents \"{title}.\" Sarah, walk us through the high-stakes dilemma this organization confronted.",
            f"[TA Sarah] Look at {comp}: {prob}",
            f"[TA James] Man, that is every DevOps lead's worst nightmare! If that happened in a publicly traded company, the stock would tumble 15% before breakfast!",
            f"[TA Sarah] So instead of panicking, they deployed our Oikos University architecture: {sol}",
            f"[TA James] And look at the astonishing results on screen: {imp}",
            f"[TA Sarah] That is the power of sovereign agentic engineering in mission-critical environments!",
            f"[TA James] Zero guesswork, total auditability, and massive ROI!",
            f"[Prof. Peter] When intelligence is anchored in truth, it preserves human dignity and unlocks extraordinary stewardship. Soli Deo Gloria!"
        ]
    elif slide.get('type') == 'lab':
        new_turns = [
            f"[TA Sarah] Here we are at Slide {num}: \"{title}!\"",
            f"[TA James] Tonight's hands-on lab is where the rubber meets the road! Look at our 5-step mission on screen: we are taking everything we learned today and deploying it in live code!",
            f"[TA Sarah] Remember: test each component in isolation first, verify your security keys, and inspect your logs in real time!",
            f"[TA James] James and I will be in the lab Discord channel all night to help you debug and optimize your pipelines!",
            f"[Prof. Peter] As we always proclaim at Oikos University: Knowledge without practice is inert, but practiced wisdom dedicated to God's glory transforms the world.",
            f"[TA Sarah] In our next session, we will push our architectural capabilities even further into the autonomous frontier!",
            f"[TA James] Don't wait until tomorrow—fire up your terminal tonight, run your tests, and redeem your time!",
            f"[Prof. Peter] On behalf of TA Sarah Jenkins, TA James Wilson, and Smart Insight Lab: Thank you for your dedication. Soli Deo Gloria! Class dismissed in victory!"
        ]
    else:
        # Standard content / comparison / architecture slide
        points_text = " • ".join(slide.get('points', [])) if slide.get('points') else subtitle
        new_turns = [
            f"[TA Sarah] Slide {num} explores \"{title}.\" James, why is this concept so crucial for every modern AI architect?",
            f"[TA James] Because, Sarah, if you don't master this, your entire system degrades under production load! Look at the core dilemma on screen: {subtitle}",
            f"[TA Sarah] Exactly! When you analyze the engineering details: {points_text}",
            f"[TA James] Haha, I remember testing a prototype without this exact safeguard last year, and my laptop sounded like a jet engine taking off at 3:00 AM!",
            f"[TA Sarah] That's why we enforce strict architectural boundaries: separating responsibilities, caching frequently accessed states, and verifying every output!",
            f"[TA James] It turns an unpredictable, high-latency prototype into a sub-second, rock-solid production engine!",
            f"[Prof. Peter] Order and discipline are the hallmarks of true mastery. In all our designs, we reflect the structured wisdom of the Creator.",
            f"[TA Sarah] Let us inspect the next evolutionary step on Slide {num + 1}!"
        ]
        
    return "\n\n".join(new_turns)

def run_batch_upgrade(sessions):
    session_titles = {
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
    
    for s_num in sessions:
        print(f"\n==========================================")
        print(f"🚀 Upgrading Session {s_num}: {session_titles.get(s_num)}")
        print(f"==========================================")
        slides = load_session_slides(s_num)
        if not slides:
            print(f"❌ Failed to load slides for Session {s_num}")
            continue
            
        for s in slides:
            s['script'] = enrich_script_to_podcast_tikitaka(s, s_num)
            
        # 1. Write session markdown
        generate_session_md(s_num, session_titles[s_num], slides)
        
        # 2. Update slidesData.js
        update_slides_data_js_for_session(s_num, slides)
        
    print("\n🎉 Batch upgrade completed successfully!")

if __name__ == '__main__':
    # Run for Batch 1: Sessions 1, 2, 3, 5 (Session 4 is already ultra-dense)
    run_batch_upgrade([1, 2, 3, 5])
