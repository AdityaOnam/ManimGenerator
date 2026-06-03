import subprocess
import sys
import argparse

def run_command(command):
    print(f"\nExecuting: {' '.join(command)}")
    # We use shell=True on Windows to ensure executable lookup works as expected
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"\n[ERROR] Command failed with exit code {result.returncode}: {' '.join(command)}")
        sys.exit(result.returncode)

def main():
    parser = argparse.ArgumentParser(description="Run the entire Manim generation and merging pipeline.")
    parser.add_argument(
        "-q", "--quality",
        choices=["l", "m", "h", "k"],
        default="l",
        help="Compilation quality: l (low/480p), m (medium/720p), h (high/1080p), k (4k/2160p). Default is 'l'."
    )
    args = parser.parse_args()
    
    quality_flag = f"-q{args.quality}"
    
    # Map selection for nice console output
    quality_names = {
        "l": "Low (480p)",
        "m": "Medium (720p)",
        "h": "High (1080p)",
        "k": "4K (2160p)"
    }
    
    print("=" * 60)
    print(f"Starting Manim Pipeline (Quality: {quality_names[args.quality]})")
    print("=" * 60)
    
    # 1. Compile Intro (Static Image)
    print("\n--- Step 1/4: Compiling Intro (Static Image) ---")
    run_command(["manim", "-s", "begin.py", "IntroScene"])
    
    # 2. Compile Main Problem (Video)
    print("\n--- Step 2/4: Compiling Main Problem (Video) ---")
    run_command(["manim", quality_flag, "1.py", "MathProblem"])
    
    # 3. Compile Outro (Video)
    print("\n--- Step 3/4: Compiling Outro Hook (Video) ---")
    run_command(["manim", quality_flag, "end.py", "ClosingHook"])
    
    # 4. Merge Videos
    print("\n--- Step 4/4: Merging Videos ---")
    run_command([sys.executable, "merge_videos.py"])
    
    print("\n" + "=" * 60)
    print("[SUCCESS] Pipeline completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
