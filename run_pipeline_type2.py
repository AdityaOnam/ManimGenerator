import subprocess
import sys
import argparse

def run_command(command):
    print(f"\nExecuting: {' '.join(command)}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"\n[ERROR] Command failed with exit code {result.returncode}: {' '.join(command)}")
        sys.exit(result.returncode)

def main():
    parser = argparse.ArgumentParser(description="Run the TYPE2 Quiz Manim pipeline.")
    parser.add_argument(
        "-q", "--quality",
        choices=["l", "m", "h", "k"],
        default="l",
        help="Compilation quality: l (low/480p), m (medium/720p), h (high/1080p), k (4k/2160p). Default is 'l'."
    )
    args = parser.parse_args()

    quality_flag = f"-q{args.quality}"

    quality_names = {
        "l": "Low (480p)",
        "m": "Medium (720p)",
        "h": "High (1080p)",
        "k": "4K (2160p)"
    }

    print("=" * 60)
    print(f"Starting TYPE2 Quiz Pipeline (Quality: {quality_names[args.quality]})")
    print("=" * 60)

    # 1. Compile Quiz Scene
    print("\n--- Step 1/3: Compiling Quiz Scene ---")
    run_command(["manim", quality_flag, "TYPE2.py", "QuizScene"])

    # 2. Compile Outro Hook
    print("\n--- Step 2/3: Compiling Outro Hook ---")
    run_command(["manim", quality_flag, "end.py", "ClosingHook"])

    # 3. Merge
    print("\n--- Step 3/3: Merging Videos ---")
    run_command([sys.executable, "merge_videos_type2.py"])

    print("\n" + "=" * 60)
    print("[SUCCESS] TYPE2 Pipeline completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
