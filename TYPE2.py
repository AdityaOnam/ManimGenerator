from manim import *

# Configure for 9:16 vertical resolution (short-form video)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.background_color = "#000000"

# --- Color Palette ---
YELLOW  = "#ffff00"
CYAN    = "#00e1ff"
WHITE   = "#ffffff"
GREEN_C = "#2ecc71"
RED_C   = "#e74c3c"
LIGHT_GREY = "#bbbbbb"
ORANGE  = "#ff9500"

class QuizScene(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # SCENE 1: Title Dialog Box (same style as 1.py / inp.py)
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

        # Bottom Call-to-Action
        bottom_cta = VGroup(
            Text("Comment", font_size=32, weight=BOLD, color=YELLOW),
            Text("Your Answer", font_size=32, weight=BOLD, color=YELLOW)
        ).arrange(DOWN, buff=0.1).to_edge(DOWN, buff=0.4)

        self.play(FadeIn(title_group, shift=UP), FadeIn(bottom_cta, shift=UP))
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 2: Question Card
        # ---------------------------------------------------------
        # Question text — split into manageable lines for 9:16 frame
        q_line1 = Tex(r"If $g(x) = \int_0^x \cos 4t\,dt$,").scale(0.9)
        q_line2 = Tex(r"then $g(x+\pi)$ equals:").scale(0.9)
        q_text = VGroup(q_line1, q_line2).arrange(DOWN, buff=0.22)

        # Options
        opt_A = Tex(r"A. $\dfrac{g(x)}{8\pi}$").scale(0.95)
        opt_B = Tex(r"B. $g(x) + g(\pi)$").scale(0.95)
        opt_C = Tex(r"C. $g(x) - g(\pi)$").scale(0.95)
        opt_D = Tex(r"D. $g(x) \cdot g(\pi)$").scale(0.95)

        options_list = [opt_A, opt_B, opt_C, opt_D]

        # Put together the full question group
        q_full = VGroup(q_text, *options_list).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

        # Safety width clamp
        if q_full.width > 7.8:
            q_full.scale(7.8 / q_full.width)

        question_box = RoundedRectangle(
            corner_radius=0.15,
            height=q_full.height + 0.9,
            width=8.2,
            color=GRAY_D,
            stroke_width=3,
            fill_opacity=0.05
        )
        question_box.next_to(title_group, DOWN, buff=0.5)
        q_full.move_to(question_box.get_center())

        self.play(FadeIn(question_box))
        self.play(Write(q_text))
        self.wait(0.3)
        self.play(
            AnimationGroup(*[FadeIn(opt, shift=RIGHT * 0.3) for opt in options_list], lag_ratio=0.15)
        )
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 3: PAUSE & TRY Timer
        # ---------------------------------------------------------
        timer_width = 7.0
        timer_bg  = Line(LEFT, RIGHT, color=GRAY_E, stroke_width=6).scale(timer_width / 2).next_to(bottom_cta, UP, buff=0.5)
        timer_bar = Line(LEFT, RIGHT, color=CYAN, stroke_width=6).scale(timer_width / 2).align_to(timer_bg, LEFT).next_to(bottom_cta, UP, buff=0.5)
        timer_label = Text("PAUSE & TRY!", font_size=32, weight=BOLD, color=CYAN).next_to(timer_bg, UP, buff=0.3)

        self.play(Create(timer_bg), FadeIn(timer_label))
        self.play(
            timer_bar.animate(rate_func=linear).scale(0, about_edge=LEFT),
            run_time=5
        )
        self.play(FadeOut(timer_label), FadeOut(timer_bg), FadeOut(timer_bar))
        self.wait(0.3)

        # ---------------------------------------------------------
        # SCENE 4: Reveal Answer
        # Correct answer: A, B and D only
        # Options A (index 0), B (index 1), D (index 3) are correct
        # ---------------------------------------------------------

        # Shrink title to mini version to make room for answer reveal
        self.play(title_group.animate.scale(0.65).to_edge(UP, buff=0.4))
        self.wait(0.2)

        # Highlight each option individually with color coding
        CORRECT_OPTS = {1}   # B is correct

        highlight_anims = []
        for i, opt in enumerate(options_list):
            if i in CORRECT_OPTS:
                highlight_anims.append(opt.animate.set_color(GREEN_C))
            else:
                highlight_anims.append(opt.animate.set_opacity(0.25))

        self.play(*highlight_anims, run_time=0.8)
        self.wait(0.5)

        # Show answer label
        answer_line1 = Text("Correct Answer:", font_size=30, weight=BOLD, color=WHITE)
        answer_line2 = Tex(r"B. $g(x) + g(\pi)$").scale(1.2).set_color(GREEN_C)
        answer_group = VGroup(answer_line1, answer_line2).arrange(DOWN, buff=0.2)

        answer_box = RoundedRectangle(
            corner_radius=0.15,
            width=answer_group.width + 1.2,
            height=answer_group.height + 0.7,
            color=GREEN_C,
            stroke_width=3,
            fill_opacity=0.08
        ).move_to(answer_group)

        answer_full = VGroup(answer_box, answer_group)
        answer_full.next_to(question_box, DOWN, buff=0.5)

        self.play(FadeIn(answer_full, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        # ---------------------------------------------------------
        # SCENE 5: Fast fade out → hand off to outro
        # ---------------------------------------------------------
        self.play(
            FadeOut(VGroup(
                title_group, question_box, q_full,
                answer_full, bottom_cta
            )),
            run_time=0.5
        )
        self.wait(0.2)