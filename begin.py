from manim import *
import json
import os

# Configure for 9:16 vertical resolution
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.background_color = "#000000" # Complete black background to merge with image

# Load colors from configuration file
with open("colors.json", "r") as f:
    colors = json.load(f)

YELLOW = colors.get("YELLOW", "#ffff00")
CYAN = colors.get("CYAN", "#00e1ff")
WHITE = colors.get("WHITE", "#ffffff")

class IntroScene(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # SCENE 1: Header Titles (Matching 1.py exactly)
        # ---------------------------------------------------------
        title_line1 = Text("MOST REPEATED", font_size=36, weight=BOLD, color=YELLOW)
        title_line2 = Text("PYQs", font_size=36, weight=BOLD, color=WHITE)
        title_line3 = Text("JEE MAIN 2027", font_size=36, weight=BOLD, color=CYAN)
        title_text = VGroup(title_line1, title_line2, title_line3).arrange(DOWN, buff=0.35)
        
        title_box = RoundedRectangle(
            corner_radius=0.15,
            width=title_text.width + 2.0,
            height=title_text.height + 1.0,
            color=GRAY_D,
            stroke_width=3,
            fill_color="#1e1e1e",
            fill_opacity=0.9
        )
        title_text.move_to(title_box.get_center())
        title_group = VGroup(title_box, title_text).to_edge(UP, buff=0.6)
        
        # ---------------------------------------------------------
        # SCENE 2: Center Image Plugin (Border removed to merge seamlessly)
        # ---------------------------------------------------------
        image_path = "question.png"
        
        if os.path.exists(image_path):
            image = ImageMobject(image_path)
            # Scale the image to fit safety width (8.0 units) to zoom out slightly
            image.scale_to_fit_width(8.0)
            # Ensure it doesn't overflow vertically into the header
            if image.height > 6.0:
                image.scale_to_fit_height(6.0)
            image.move_to(ORIGIN)
            image_mobject = image # No border, merges seamlessly with black background
        else:
            # Fallback beautiful placeholder if the user hasn't copied the image yet
            placeholder_bg = RoundedRectangle(
                corner_radius=0.15,
                width=7.5,
                height=5.0,
                color=GRAY_D,
                stroke_width=3,
                fill_color="#1e1e1e",
                fill_opacity=0.5
            ).move_to(ORIGIN)
            placeholder_text = Text(
                "Please place 'question.png'\nin the workspace directory:\n\nC:\\Users\\adity\\OneDrive\\Desktop\\Manim\\",
                font_size=22,
                color=WHITE,
                line_spacing=1.2
            ).move_to(placeholder_bg.get_center())
            image_mobject = VGroup(placeholder_bg, placeholder_text)
            
        # ---------------------------------------------------------
        # Direct Display (For generating a single static image)
        # ---------------------------------------------------------
        self.add(title_group, image_mobject)
