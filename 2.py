from manim import *
import json

# Configure for 9:16 vertical resolution optimized for short-form video
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.background_color = "#000000"

# --- Define Colors ---
YELLOW = "#ffff00"
CYAN = "#00e1ff"
WHITE = "#ffffff"
GREEN_C = "#55ff55"
GREEN_A = "#a3ffa3"
LIGHT_GREY = "#bbbbbb"
ORANGE = "#ff9500"

class MathProblem(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # SCENE 1: Question Frame & Introductory Titles
        # ---------------------------------------------------------

        # Title box (identical to 1.py)
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

        # Introductory Bottom Text
        bottom_txt1 = VGroup(
            Text("Comment", font_size=32, weight=BOLD, color=YELLOW),
            Text("Your Answer", font_size=32, weight=BOLD, color=YELLOW)
        ).arrange(DOWN, buff=0.1).to_edge(DOWN, buff=0.4)

        # Question parts
        q_p1 = Tex(r"If $f(x) = \dfrac{2^x}{2^x + \sqrt{2}},\ x \in \mathbb{R}$,").scale(1.05)
        q_eq = MathTex(
            r"\sum_{k=1}^{81} f\!\left(\frac{k}{82}\right) = \ ?",
        ).scale(1.5).set_color(YELLOW)
        q_p2 = Tex(r"then the sum is equal to \_\_\_\_\_.").scale(1.05)
        q_options = Tex(
            r"(A)\ $81\sqrt{2}$ \qquad (B)\ $41$ \qquad (C)\ $82$ \qquad (D)\ $\dfrac{81}{2}$"
        ).scale(0.95).set_color(LIGHT_GREY)

        q_group = VGroup(q_p1, q_eq, q_p2, q_options).arrange(DOWN, buff=0.55)

        if q_group.width > 7.5:
            q_group.scale(7.5 / q_group.width)

        question_box = RoundedRectangle(
            corner_radius=0.15,
            height=q_group.height + 1.0,
            width=8.0,
            color=GRAY_D,
            stroke_width=3,
            fill_opacity=0.05
        ).move_to(ORIGIN).set_y(0.5)

        q_group.move_to(question_box.get_center())
        question_frame = VGroup(question_box, q_group)

        self.play(FadeIn(title_group, shift=UP), FadeIn(bottom_txt1, shift=UP))
        self.wait(0.5)
        self.play(FadeIn(question_frame))

        # PAUSE & TRY! Timer
        timer_width = 7.0
        timer_bg = Line(LEFT, RIGHT, color=GRAY_E, stroke_width=6).scale(timer_width/2).to_edge(DOWN, buff=2.3)
        timer_bar = Line(LEFT, RIGHT, color=CYAN, stroke_width=6).scale(timer_width/2).align_to(timer_bg, LEFT).to_edge(DOWN, buff=2.3)
        timer_label = Text("PAUSE & TRY!", font_size=36, weight=BOLD, color=CYAN).next_to(timer_bg, UP, buff=0.3)

        self.play(Create(timer_bg), FadeIn(timer_label))
        self.play(
            timer_bar.animate(rate_func=linear).scale(0, about_edge=LEFT),
            run_time=3
        )
        self.wait(0.5)

        # ---------------------------------------------------------
        # TRANSITION: Shrinking Headers & Setup for Solving
        # ---------------------------------------------------------

        bottom_txt2 = Text("Follow For More", font_size=35, weight=BOLD, color=CYAN)
        bottom_txt2.to_edge(DOWN, buff=0.8)

        self.play(FadeOut(question_frame), FadeOut(timer_bg), FadeOut(timer_label), FadeOut(timer_bar), FadeOut(bottom_txt1))
        self.play(
            title_group.animate.scale(0.65).to_edge(UP, buff=0.5),
            FadeIn(bottom_txt2, shift=UP)
        )
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 2: Key Identity via Substitution
        # ---------------------------------------------------------

        method_label = VGroup(
            Tex(r"Strategy: Use the symmetry property"),
            Tex(r"of $f(x)$ to find a pairing identity.")
        ).arrange(DOWN, buff=0.1).scale(0.85).set_color(LIGHT_GREY)
        method_label.next_to(title_group, DOWN, buff=0.7)
        self.play(Write(method_label))
        self.wait(0.5)

        # Show the function definition
        given_def = MathTex(
            r"f(x) = \frac{2^x}{2^x + \sqrt{2}}"
        ).scale(1.2).set_color(WHITE)
        given_def.next_to(method_label, DOWN, buff=0.6)
        self.play(Write(given_def))
        self.wait(0.5)

        sub1_step = Tex(r"Put $x \to 1 - x$:").scale(1.0).set_color(ORANGE)
        sub1_step.next_to(given_def, DOWN, buff=0.6)
        self.play(FadeIn(sub1_step, shift=RIGHT))
        self.wait(0.3)

        calc1 = MathTex(
            r"f(1-x) = \frac{2^{1-x}}{2^{1-x} + \sqrt{2}}"
        ).scale(1.1)
        calc1.next_to(sub1_step, DOWN, buff=0.4)
        self.play(TransformFromCopy(given_def, calc1))
        self.wait(0.3)

        simplify_cue = Tex(r"Simplify by multiplying numerator \& denominator by $2^x$:").scale(0.75).set_color(LIGHT_GREY)
        simplify_cue.next_to(calc1, DOWN, buff=0.5)
        self.play(Write(simplify_cue))
        self.wait(0.3)

        eqA_result = MathTex(r"f(1-x) = \frac{\sqrt{2}}{\sqrt{2} + 2^x}").scale(1.2).set_color(YELLOW)
        eqA_result.next_to(simplify_cue, DOWN, buff=0.4)

        boxA = RoundedRectangle(corner_radius=0.1, color=YELLOW, stroke_width=3, fill_opacity=0.05)
        boxA.surround(eqA_result, buff=0.2)

        tag1 = Tex(r"\textbf{(1)}", color=YELLOW, font_size=32).next_to(boxA, RIGHT, buff=0.2)

        self.play(Transform(calc1, eqA_result))
        self.play(Create(boxA), Write(tag1))
        self.wait(1)

        equation_A_group = VGroup(boxA, tag1, calc1)

        self.play(
            FadeOut(sub1_step),
            FadeOut(given_def),
            FadeOut(simplify_cue),
            FadeOut(method_label)
        )
        self.play(equation_A_group.animate.next_to(title_group, DOWN, buff=0.7))
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 3: Prove f(x) + f(1-x) = 1
        # ---------------------------------------------------------

        given_def2 = MathTex(
            r"f(x) = \frac{2^x}{2^x + \sqrt{2}}"
        ).scale(1.0).set_color(LIGHT_GREY).next_to(equation_A_group, DOWN, buff=0.6)
        self.play(FadeIn(given_def2))

        sum_cue = Tex(r"Add $f(x) + f(1-x)$:").scale(0.9).set_color(ORANGE)
        sum_cue.next_to(given_def2, DOWN, buff=0.5)
        self.play(FadeIn(sum_cue, shift=RIGHT))
        self.wait(0.3)

        calc2 = MathTex(
            r"f(x)+f(1-x)=\frac{2^x}{2^x+\sqrt{2}}+\frac{\sqrt{2}}{2^x+\sqrt{2}}"
        ).scale(0.95)
        calc2.next_to(sum_cue, DOWN, buff=0.4)
        self.play(Write(calc2))
        self.wait(0.3)

        eqB_result = MathTex(r"f(x) + f(1-x) = 1").scale(1.3).set_color(YELLOW)
        eqB_result.next_to(calc2, DOWN, buff=0.4)

        boxB = RoundedRectangle(corner_radius=0.1, color=YELLOW, stroke_width=3, fill_opacity=0.05)
        boxB.surround(eqB_result, buff=0.2)

        tag2 = Tex(r"\textbf{(2)}", color=YELLOW, font_size=32).next_to(boxB, RIGHT, buff=0.2)

        self.play(Transform(calc2, eqB_result))
        self.play(Create(boxB), Write(tag2))
        self.wait(1)

        equation_B_group = VGroup(boxB, tag2, calc2)

        self.play(
            FadeOut(sum_cue),
            FadeOut(given_def2)
        )
        self.play(equation_B_group.animate.next_to(equation_A_group, DOWN, buff=0.5))
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 4: Pair the 81 Terms & Evaluate
        # ---------------------------------------------------------

        solve_task = VGroup(
            Tex(r"Pair terms: $f(k/82) + f(1-k/82) = 1$"),
            Tex(r"i.e., $f(k/82) + f((82-k)/82) = 1$")
        ).arrange(DOWN, buff=0.1).scale(0.82).set_color(LIGHT_GREY)
        solve_task.next_to(equation_B_group, DOWN, buff=0.6)
        self.play(Write(solve_task))
        self.wait(0.5)

        add_tag = Tex(r"+", color=ORANGE, font_size=40).next_to(equation_B_group, LEFT, buff=0.5)
        underline_line = Line(
            start=boxA.get_left(),
            end=boxA.get_right() + UP * tag1.width * 2,
            color=WHITE
        ).next_to(equation_B_group, DOWN, buff=0.15)

        self.play(FadeIn(add_tag, shift=UP))
        self.play(Create(underline_line))
        self.wait(0.5)

        pair_result = MathTex(r"40 \text{ pairs} \times 1 = 40").scale(1.2)
        pair_result.next_to(underline_line, DOWN, buff=0.4)
        self.play(Write(pair_result))
        self.wait(0.8)

        middle_cue = Tex(r"Middle term: $k = 41 \Rightarrow f(41/82) = f(1/2)$").scale(0.82).set_color(LIGHT_GREY)
        middle_cue.next_to(pair_result, DOWN, buff=0.5)
        self.play(Write(middle_cue))
        self.wait(0.3)

        middle_val = MathTex(
            r"f\!\left(\tfrac{1}{2}\right) = \frac{2^{1/2}}{2^{1/2}+\sqrt{2}} = \frac{\sqrt{2}}{2\sqrt{2}} = \frac{1}{2}"
        ).scale(1.0).set_color(WHITE)
        middle_val.next_to(middle_cue, DOWN, buff=0.4)
        self.play(Write(middle_val))
        self.wait(1)

        self.play(
            FadeOut(equation_A_group),
            FadeOut(equation_B_group),
            FadeOut(add_tag),
            FadeOut(underline_line),
            FadeOut(solve_task),
            FadeOut(pair_result),
            FadeOut(middle_cue)
        )
        self.play(middle_val.animate.next_to(title_group, DOWN, buff=1.5).set_color(LIGHT_GREY))
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 5: Final Sum & Result
        # ---------------------------------------------------------

        final_calc_step = Tex(r"Total sum $= 40 \times 1 + f(1/2)$:").scale(0.8).set_color(LIGHT_GREY)
        final_calc_step.next_to(middle_val, DOWN, buff=0.7)
        self.play(FadeIn(final_calc_step, shift=UP))
        self.wait(0.3)

        final_step = MathTex(r"\sum_{k=1}^{81} f\!\left(\frac{k}{82}\right) = 40 + \frac{1}{2}").scale(1.2)
        final_step.next_to(final_calc_step, DOWN, buff=0.4)
        self.play(Write(final_step))
        self.wait(1.5)

        # ---------------------------------------------------------
        # SCENE 6: End Sequence
        # ---------------------------------------------------------

        self.play(FadeOut(final_calc_step), FadeOut(middle_val))
        final_res_step = MathTex(r"\sum_{k=1}^{81} f\!\left(\frac{k}{82}\right) = \frac{81}{2}").scale(1.2).next_to(final_step, DOWN, buff=0.4).set_color(WHITE)
        self.play(Transform(final_step, final_res_step))
        self.wait(0.5)

        self.play(FadeOut(title_group))

        self.play(final_step.animate.move_to(ORIGIN).scale(1.5).set_color(GREEN_C))

        final_box = RoundedRectangle(corner_radius=0.15, color=GREEN_A, stroke_width=4)
        final_box.surround(final_step, buff=0.3)

        self.play(Create(final_box), run_time=0.5)
        self.play(FadeOut(VGroup(final_step, final_box, bottom_txt2)), run_time=0.5)
        self.wait(0.2)
