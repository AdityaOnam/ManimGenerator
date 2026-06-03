# JEE Main/Advanced Manim Animation Suite

This directory contains Manim script pipelines designed for generating vertical (9:16 portrait) short-form content for math problem sets and outre.

## Workflow Overview

1. **Intro**: Display heading card + `question.png` image (compiled as a high-quality static PNG image).
2. **Main Video**: Animate the full derivation & final answer of the JEE PYQ question.
3. **Outro (Closing Hook)**: Play CTA transition ("Follow for More" + "@prepai_red" user handle).
4. **Merge**: Stitch the main video and outro video together into a single finished video file.

---https://github.com/AdityaOnam/ManimGenerator.git

## 💻 Commands Reference

Manim provides flags to compile videos at various quality levels and frame rates. The automation merge script (`merge_videos.py`) works dynamically for any compiled quality.

### 🌟 Quality Preset Reference Table

| Quality Level | Flag | Pixel Dimensions (Portrait) | Frame Rate | Recommended Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Low** | `-ql` | `480 x 853` | `15 fps` | Rapid testing / draft previews |
| **Medium** | `-qm` | `720 x 1280` | `30 fps` | Quick sharing / standard previews |
| **High** | `-qh` | `1080 x 1920` (Native) | `60 fps` | YouTube Shorts / TikTok Uploads |
| **4K (Best)** | `-qk` | `2160 x 3840` | `60 fps` | **Maximum Quality Master Export** |

---

### 1. Compile Intro (Static Image)
Generates a static `1080x1920` portrait PNG of the question slide:
```powershell
manim -s begin.py IntroScene
```
* **Output Path**: `media/images/begin/IntroScene_ManimCE_v0.19.0.png`
* *Note: Ensure your question graphic is saved at `question.png` in the directory.*

---

### 2. Compile Main Problem (Video)
Compile the solution animation at your desired quality level:

* **4K (Best Quality)**:
  ```powershell
  manim -qk 1.py MathProblem
  ```
* **High (Standard HD)**:
  ```powershell
  manim -qh 1.py MathProblem
  ```
* **Low (Fast Draft)**:
  ```powershell
  manim -ql 1.py MathProblem
  ```

---

### 3. Compile Outro Hook (Video)
Compile the outro CTA slide at the corresponding quality level:

* **4K (Best Quality)**:
  ```powershell
  manim -qk end.py ClosingHook
  ```
* **High (Standard HD)**:
  ```powershell
  manim -qh end.py ClosingHook
  ```
* **Low (Fast Draft)**:
  ```powershell
  manim -ql end.py ClosingHook
  ```

---

### 4. Merge Main Problem & Outro Video
Run the automated lossless merge python script to stitch them together instantly:
```powershell
python merge_videos.py
```
* **Required Tool**: `ffmpeg` (installed automatically with Manim).
* **Output Path**: `final_output.mp4` in the main workspace directory.
* *Note: The merge script recursively scans the `media/` directory and will automatically find and merge whichever quality level you recently compiled.*

