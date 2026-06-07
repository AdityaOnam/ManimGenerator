import os
import subprocess
import sys

def find_file(filename, search_path):
    latest_file = None
    latest_mtime = 0
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            full_path = os.path.abspath(os.path.join(root, filename))
            mtime = os.path.getmtime(full_path)
            if mtime > latest_mtime:
                latest_mtime = mtime
                latest_file = full_path
    return latest_file

def merge():
    print("Searching for compiled video files...")
    media_dir = "media"

    quiz_path = find_file("QuizScene.mp4", media_dir)
    closing_hook_path = find_file("ClosingHook.mp4", media_dir)

    if not quiz_path:
        print("Error: Could not find QuizScene.mp4 under 'media/' directory.")
        print("Please compile TYPE2.py first using: manim -ql TYPE2.py QuizScene")
        sys.exit(1)

    if not closing_hook_path:
        print("Error: Could not find ClosingHook.mp4 under 'media/' directory.")
        print("Please compile end.py first using: manim -ql end.py ClosingHook")
        sys.exit(1)

    print(f"Found QuizScene at: {quiz_path}")
    print(f"Found ClosingHook at: {closing_hook_path}")

    concat_file = "concat_list_type2.txt"
    try:
        with open(concat_file, "w") as f:
            f.write(f"file '{quiz_path.replace(os.sep, '/')}'\n")
            f.write(f"file '{closing_hook_path.replace(os.sep, '/')}'\n")

        output_file = "final_output_type2.mp4"
        if os.path.exists(output_file):
            try:
                os.remove(output_file)
            except OSError:
                print(f"Error: {output_file} is currently open or locked. Please close it and run the script again.")
                sys.exit(1)

        print("Merging videos using FFmpeg concat demuxer (lossless)...")
        command = [
            "ffmpeg",
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", concat_file,
            "-c", "copy",
            output_file
        ]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print(f"\n[SUCCESS] Videos merged losslessly into: {os.path.abspath(output_file)}")
        else:
            print("\n[ERROR] FFmpeg merge failed. Detailed logs below:")
            print(result.stderr)
            sys.exit(1)

    finally:
        if os.path.exists(concat_file):
            os.remove(concat_file)

if __name__ == "__main__":
    merge()
