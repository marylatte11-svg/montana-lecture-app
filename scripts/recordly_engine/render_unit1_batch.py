# -*- coding: utf-8 -*-
"""
Montana State University - Gallatin College: M090 Introductory Algebra
Unit 1 (Lectures 01~15) Master Batch Runner
- Automatically iterates through Lectures 01 to 15
- Renders full 1080p 60fps Recordly videos with precision camera panning
- Skips already completed master videos unless --force is specified
- Works seamlessly on both Local PC and Google Colab GPU
"""

import os
import sys
import time
import argparse
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ENGINE_DIR = os.path.join(BASE_DIR, "scripts", "recordly_engine")
RENDER_SCRIPT = os.path.join(ENGINE_DIR, "render_montana_recordly.py")
RECORDLY_VIDEOS_DIR = os.path.join(BASE_DIR, "Montana_State_Univ", "recordly_videos")

def is_lecture_completed(lec_id):
    master_path = os.path.join(RECORDLY_VIDEOS_DIR, f"Lecture{lec_id:02d}", f"MSU_M090_Lecture{lec_id:02d}_Full_Master.mp4")
    return os.path.exists(master_path) and os.path.getsize(master_path) > 10 * 1024 * 1024

def main():
    parser = argparse.ArgumentParser(description="MSU M090 Unit 1 (Lectures 1-15) Batch Runner")
    parser.add_argument("--start", type=int, default=1, help="Start lecture ID (default: 1)")
    parser.add_argument("--end", type=int, default=15, help="End lecture ID (default: 15)")
    parser.add_argument("--lectures", type=str, default=None, help="Specific comma-separated lectures (e.g., '1,2,3')")
    parser.add_argument("--force", action="store_true", help="Force re-render even if master video already exists")
    args = parser.parse_args()

    if args.lectures:
        lec_ids = [int(x.strip()) for x in args.lectures.split(",") if x.strip().isdigit()]
    else:
        lec_ids = list(range(args.start, args.end + 1))

    total = len(lec_ids)
    print("\n" + "=" * 70)
    print(f"🎬 MSU M090 UNIT 1 BATCH RENDER: Lectures {lec_ids[0]:02d} ~ {lec_ids[-1]:02d} (Total {total} lectures)")
    print("=" * 70 + "\n")

    start_total_time = time.time()
    results = []

    for idx, lec in enumerate(lec_ids, 1):
        master_file = os.path.join(RECORDLY_VIDEOS_DIR, f"Lecture{lec:02d}", f"MSU_M090_Lecture{lec:02d}_Full_Master.mp4")
        if not args.force and is_lecture_completed(lec):
            sz_mb = os.path.getsize(master_file) / (1024 * 1024)
            print(f"[{idx}/{total}] ⏩ Lecture {lec:02d}: ALREADY COMPLETED ({sz_mb:.2f} MB) -> Skipping")
            results.append({"lec": lec, "status": "CACHED", "size_mb": sz_mb, "time_sec": 0})
            continue

        print(f"\n" + "-" * 70)
        print(f"🚀 [{idx}/{total}] Starting Full Render for Lecture {lec:02d}...")
        print("-" * 70)

        lec_start_time = time.time()
        cmd = [sys.executable, RENDER_SCRIPT, "--lecture", str(lec), "--all"]
        if args.force:
            cmd.append("--force")

        p = subprocess.run(cmd, cwd=BASE_DIR)
        lec_elapsed = time.time() - lec_start_time

        if p.returncode == 0 and os.path.exists(master_file):
            sz_mb = os.path.getsize(master_file) / (1024 * 1024)
            print(f"✅ Lecture {lec:02d} Finished in {lec_elapsed/60:.1f} mins ({sz_mb:.2f} MB)")
            results.append({"lec": lec, "status": "SUCCESS", "size_mb": sz_mb, "time_sec": lec_elapsed})
        else:
            print(f"❌ Lecture {lec:02d} Failed with exit code {p.returncode}")
            results.append({"lec": lec, "status": "FAILED", "size_mb": 0, "time_sec": lec_elapsed})

    total_elapsed = time.time() - start_total_time
    print("\n" + "=" * 70)
    print(f"🏆 UNIT 1 BATCH SUMMARY (Total Time: {total_elapsed/60:.1f} mins)")
    print("=" * 70)
    for r in results:
        status_icon = "✅" if r["status"] in ["SUCCESS", "CACHED"] else "❌"
        print(f"  {status_icon} Lecture {r['lec']:02d}: {r['status']:<7} | Size: {r['size_mb']:>6.2f} MB | Time: {r['time_sec']/60:>4.1f}m")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
