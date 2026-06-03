import os
import subprocess
import sys

def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.abspath(os.path.join(root, filename))
    return None

def merge():
    print("Searching for compiled video files...")
    media_dir = "media"
    
    math_problem_path = find_file("MathProblem.mp4", media_dir)
    closing_hook_path = find_file("ClosingHook.mp4", media_dir)
    
    if not math_problem_path:
        print("Error: Could not find MathProblem.mp4 under 'media/' directory.")
        print("Please compile 1.py first using: manim -ql 1.py MathProblem")
        sys.exit(1)
        
    if not closing_hook_path:
        print("Error: Could not find ClosingHook.mp4 under 'media/' directory.")
        print("Please compile end.py first using: manim -ql end.py ClosingHook")
        sys.exit(1)
        
    print(f"Found MathProblem at: {math_problem_path}")
    print(f"Found ClosingHook at: {closing_hook_path}")
    
    # Create temp concat list file for FFmpeg demuxer
    concat_file = "concat_list.txt"
    try:
        with open(concat_file, "w") as f:
            # We use forward slashes for cross-platform compatibility in ffmpeg paths
            f.write(f"file '{math_problem_path.replace(os.sep, '/')}'\n")
            f.write(f"file '{closing_hook_path.replace(os.sep, '/')}'\n")
            
        output_file = "final_output.mp4"
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
        
        # Run command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print(f"\n[SUCCESS] Videos merged losslessly into: {os.path.abspath(output_file)}")
        else:
            print("\n[ERROR] FFmpeg merge failed. Detailed logs below:")
            print(result.stderr)
            sys.exit(1)
            
    finally:
        # Clean up temp file
        if os.path.exists(concat_file):
            os.remove(concat_file)

if __name__ == "__main__":
    merge()
