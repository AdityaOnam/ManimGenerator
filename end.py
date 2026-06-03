from manim import *

# Background Color Standard (Complete Black to keep consistent across all videos)
COLOR_BG = "#000000"
YELLOW = "#ffff00"
WHITE = "#ffffff"
BLUE = "#3498db"

# Setting strictly to 9:16 for vertical short-form content
config.background_color = COLOR_BG
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

class ClosingHook(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # CLOSING HOOK (Social Media Safe)
        # ---------------------------------------------------------
        
        # Follow for More (split into two lines in bold, highly-readable sans-serif)
        t1 = Text("Follow for", font_size=64, weight=BOLD, color=YELLOW)
        t2 = Text("More", font_size=64, weight=BOLD, color=YELLOW)
        follow_group = VGroup(t1, t2).arrange(DOWN, buff=0.25)
        
        # IIT Line (split into two lines in white)
        b1 = Text("One step closer to IIT", font_size=44, weight=BOLD, color=WHITE)
        b2 = Text("Everyday.", font_size=44, weight=BOLD, color=WHITE)
        iit_group = VGroup(b1, b2).arrange(DOWN, buff=0.2)
        
        # Handle Line (@prepai_red in Blue, positioned at the bottom of the frame)
        handle_txt = Text("@prepai_red", font_size=50, weight=BOLD, color=BLUE)
        
        # Safety scaling checks for 9:16 layout
        if t1.width > 7.5:
            t1.scale(7.5 / t1.width)
        if t2.width > 7.5:
            t2.scale(7.5 / t2.width)
        if b1.width > 7.5:
            b1.scale(7.5 / b1.width)
        if b2.width > 7.5:
            b2.scale(7.5 / b2.width)
        if handle_txt.width > 7.5:
            handle_txt.scale(7.5 / handle_txt.width)

        # Position Follow and IIT sections in the upper/mid portion
        outro_group = VGroup(follow_group, iit_group).arrange(DOWN, buff=0.8)
        outro_group.move_to(UP * 0.4)
        
        # Position handle_txt explicitly at the bottom of the frame
        handle_txt.to_edge(DOWN, buff=1.2)

        # Smooth animation sequence
        self.play(
            Write(follow_group),
            FadeIn(iit_group, shift=UP),
            FadeIn(handle_txt, shift=UP),
            run_time=1.8
        )
        
        # Hold for engagement
        self.wait(3.0) 
        
        # Fade out downwards as the video concludes
        self.play(
            FadeOut(follow_group, shift=DOWN),
            FadeOut(iit_group, shift=DOWN),
            FadeOut(handle_txt, shift=DOWN)
        )