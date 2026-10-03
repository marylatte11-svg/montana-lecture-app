# -*- coding: utf-8 -*-
"""
Montana State University - Gallatin College: M090 Introductory Algebra
Batch Render Orchestrator for All 45 Lectures
- Automated multi-lecture processing
- Smart resume / skip already completed master videos
- Real-time progress tracking and ETA calculation
- Markdown manifest generation
"""

import os
import sys
import time
import argparse
import subprocess
from datetime import datetime, timedelta

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Oikos Univ"
MONTANA_DIR = os.path.join(BASE_DIR, "Montana_State_Univ")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts", "recordly_engine")
RENDER_SCRIPT = os.path.join(SCRIPTS_DIR, "render_montana_recordly.py")
VIDEOS_ROOT = os.path.join(MONTANA_DIR, "recordly_videos")

def get_lecture_master_video(lecture_id):
    lecture_dir = os.path.join(VIDEOS_ROOT, f"Lecture{lecture_id:02d}")
    master_path = os.path.join(lecture_dir, f"MSU_M090_Lecture{lecture_id:02d}_Full_Master.mp4")
    return master_path

def format_duration(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins}m {secs:02d}s"

def update_manifest_file(results, unit_label="Unit 1"):
    manifest_path = os.path.join(MONTANA_DIR, f"{unit_label.upper().replace(' ', '_')}_VIDEO_MANIFEST.md")
    
    total_size_mb = sum(r.get("size_mb", 0) for r in results if r.get("status") in ["Completed", "Cached"])
    total_runtime_sec = sum(r.get("duration_sec", 0) for r in results if r.get("status") in ["Completed", "Cached"])
    completed_count = sum(1 for r in results if r.get("status") in ["Completed", "Cached"])
    
    lines = [
        f"# 🎬 Montana State University M090: {unit_label} Video Production Manifest",
        f"\n**Generated / Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\n- **Total Lectures:** {len(results)}",
        f"- **Completed / Verified:** {completed_count} / {len(results)}",
        f"- **Total Storage Size:** {total_size_mb:.2f} MB ({total_size_mb/1024:.2f} GB)",
        f"- **Total Render Time:** {format_duration(total_runtime_sec)}",
        "\n| Lecture | Title | Status | Size | Render Time | Master Video File |",
        "| :---: | :--- | :---: | :---: | :---: | :--- |"
    ]
    
    for r in results:
        lec_id = r["lecture_id"]
        status_icon = "✅" if r["status"] in ["Completed", "Cached"] else "❌"
        size_str = f"{r.get('size_mb', 0):.2f} MB" if r.get('size_mb', 0) > 0 else "-"
        dur_str = format_duration(r.get('duration_sec', 0)) if r.get('duration_sec', 0) > 0 else "-"
        file_link = f"[{os.path.basename(r['master_path'])}](file:///{r['master_path'].replace(os.sep, '/')})" if os.path.exists(r['master_path']) else "-"
        
        lines.append(f"| **L{lec_id:02d}** | {r.get('title', f'Lecture {lec_id:02d}')} | {status_icon} {r['status']} | {size_str} | {dur_str} | {file_link} |")
        
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
        
    print(f"📄 Updated Manifest: {manifest_path}")

def run_batch(lectures, force=False, unit_label="Unit 1"):
    print("=" * 70)
    print(f"🚀 MSU M090 BATCH VIDEO RENDER ENGINE — {unit_label}")
    print(f"   Target Lectures: {lectures}")
    print(f"   Force Re-render: {force}")
    print(f"   Started At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    results = []
    batch_start_time = time.time()
    total_lectures = len(lectures)
    
    for idx, lec_id in enumerate(lectures, 1):
        master_path = get_lecture_master_video(lec_id)
        exists = os.path.exists(master_path) and os.path.getsize(master_path) > 5 * 1024 * 1024
        
        record = {
            "lecture_id": lec_id,
            "master_path": master_path,
            "title": f"M090 Lecture {lec_id:02d}",
            "status": "Pending",
            "size_mb": 0,
            "duration_sec": 0
        }
        
        if exists and not force:
            size_mb = os.path.getsize(master_path) / (1024 * 1024)
            record["status"] = "Cached"
            record["size_mb"] = size_mb
            print(f"\n[{idx}/{total_lectures}] ⚡ Lecture {lec_id:02d} already rendered ({size_mb:.2f} MB). Skipping.")
            results.append(record)
            continue
            
        print(f"\n----------------------------------------------------------------------")
        print(f"[{idx}/{total_lectures}] 🎬 Starting Render for Lecture {lec_id:02d}...")
        print(f"----------------------------------------------------------------------")
        
        lec_start_time = time.time()
        cmd = [sys.executable, RENDER_SCRIPT, "--lecture", str(lec_id), "--all"]
        if force:
            cmd.append("--force")
            
        try:
            # Run sub-process and stream output live
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
            for line in process.stdout:
                line_str = line.rstrip()
                if line_str:
                    print(f"  [L{lec_id:02d}] {line_str}")
            process.wait()
            
            lec_duration = time.time() - lec_start_time
            if os.path.exists(master_path) and os.path.getsize(master_path) > 1024 * 1024:
                size_mb = os.path.getsize(master_path) / (1024 * 1024)
                record["status"] = "Completed"
                record["size_mb"] = size_mb
                record["duration_sec"] = lec_duration
                print(f"✨ [L{lec_id:02d}] SUCCESS! Master Video created: {size_mb:.2f} MB in {format_duration(lec_duration)}")
            else:
                record["status"] = "Failed"
                record["duration_sec"] = lec_duration
                print(f"⚠️ [L{lec_id:02d}] Finished without creating master video.")
                
        except Exception as e:
            record["status"] = f"Error: {e}"
            print(f"❌ [L{lec_id:02d}] Error: {e}")
            
        results.append(record)
        update_manifest_file(results, unit_label=unit_label)
        
        # Calculate ETA
        elapsed_total = time.time() - batch_start_time
        avg_per_lec = elapsed_total / idx
        remaining = total_lectures - idx
        eta_seconds = avg_per_lec * remaining
        print(f"⏱️ Progress: {idx}/{total_lectures} ({(idx/total_lectures)*100:.1f}%) • Elapsed: {format_duration(elapsed_total)} • ETA: {format_duration(eta_seconds)}")
        
    print("\n" + "=" * 70)
    total_elapsed = time.time() - batch_start_time
    print(f"🏆 BATCH PRODUCTION FINISHED in {format_duration(total_elapsed)}!")
    print("=" * 70)
    update_manifest_file(results, unit_label=unit_label)

def main():
    parser = argparse.ArgumentParser(description="Batch Render Montana M090 Lectures")
    parser.add_argument("--start", type=int, default=3, help="Start lecture ID (default: 3)")
    parser.add_argument("--end", type=int, default=10, help="End lecture ID (default: 10)")
    parser.add_argument("--lectures", type=str, default=None, help="Comma-separated lecture IDs (e.g. 3,4,5,6)")
    parser.add_argument("--force", action="store_true", help="Force re-rendering even if master video exists")
    parser.add_argument("--unit", type=str, default="Unit 1", help="Unit label for reporting (default: Unit 1)")
    args = parser.parse_args()
    
    if args.lectures:
        lec_ids = [int(x.strip()) for x in args.lectures.split(",") if x.strip().isdigit()]
    else:
        lec_ids = list(range(args.start, args.end + 1))
        
    run_batch(lec_ids, force=args.force, unit_label=args.unit)

if __name__ == "__main__":
    main()
