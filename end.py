from manim import *
import os

# Background Color Standard (Complete Black to keep consistent across all videos)
COLOR_BG = "#000000"
YELLOW   = "#ffff00"
WHITE    = "#ffffff"
CYAN     = "#00e1ff"
BLUE     = "#3498db"

# Setting strictly to 9:16 for vertical short-form content
config.background_color = COLOR_BG
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

class ClosingHook(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # CLOSING HOOK
        # ---------------------------------------------------------

        # "Follow for More" — large, bold, yellow
        follow_line = Text(
            "Follow for More",
            font="Arial",
            font_size=68,
            weight=BOLD,
            color=YELLOW
        )
        if follow_line.width > 7.8:
            follow_line.scale(7.8 / follow_line.width)

        # Thin separator bar under the title
        separator = Line(LEFT * 3.5, RIGHT * 3.5, color=YELLOW, stroke_width=2)
        separator.next_to(follow_line, DOWN, buff=0.35)

        # --- Brand Logo + "prepAIred" text ---
        logo_path = "logo.png"
        if os.path.exists(logo_path):
            logo_img = ImageMobject(logo_path)
            logo_img.scale_to_fit_height(1.2)       # bigger icon size
        else:
            # Fallback circle if logo missing
            logo_img = Circle(radius=0.6, color=BLUE, fill_opacity=0.5)

        # "prepAIred" text
        brand_text = Text(
            "prepAIred",
            font="Arial",
            font_size=60,
            weight=BOLD,
            color=WHITE
        )

        # Place logo icon to left of brand text
        brand_group = Group(logo_img, brand_text).arrange(RIGHT, buff=0.4)
        brand_group.next_to(separator, DOWN, buff=0.6)

        # Group the main content and center it
        main_group = Group(follow_line, separator, brand_group)
        main_group.move_to(UP * 0.5)

        # --- Animate ---
        self.play(FadeIn(follow_line, shift=DOWN * 0.3), run_time=0.7)
        self.play(Create(separator), run_time=0.4)
        self.play(
            FadeIn(brand_group, shift=UP * 0.2),
            run_time=0.8
        )

        # Hold for engagement
        self.wait(3.0)

        # Fade out
        self.play(
            FadeOut(main_group, shift=DOWN),
            run_time=0.6
        )