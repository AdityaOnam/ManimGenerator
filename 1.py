from manim import *

# Configure for 9:16 vertical resolution optimized for short-form video
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.background_color = "#000000"

# --- Define Colors ---
YELLOW    = "#ffff00"
CYAN      = "#00e1ff"
WHITE     = "#ffffff"
GREEN_C   = "#55ff55"
GREEN_A   = "#a3ffa3"
LIGHT_GREY = "#bbbbbb"
ORANGE    = "#ff9500"

class MathProblem(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # SCENE 1: Question Frame & Introductory Titles
        # ---------------------------------------------------------

        # Title box
        title_line1 = Text("MOST REPEATED", font="Arial", font_size=36, weight=BOLD, color=YELLOW)
        title_line2 = Text("PYQs", font="Arial", font_size=36, weight=BOLD, color=WHITE)
        title_line3 = Text("JEE MAIN", font="Arial", font_size=36, weight=BOLD, color=CYAN)
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

        # Bottom call-to-action
        bottom_txt1 = Text("PAUSE & TRY!", font="Arial", font_size=36, weight=BOLD, color=CYAN).to_edge(DOWN, buff=0.8)

        # Question parts
        q_p1 = Tex(r"Let $\alpha, \beta$ be roots of $x^2 + \sqrt{2}x - 8 = 0$.").scale(0.9)
        q_p2 = Tex(r"If $U_n = \alpha^n + \beta^n$,").scale(0.9)
        q_p3 = Tex(r"then $\frac{U_{10} + \sqrt{2}U_9}{2U_8}$ is equal to:").scale(0.9)

        q_options1 = Tex(r"(A)\ $2$ \qquad (B)\ $4$")
        q_options2 = Tex(r"(C)\ $7$ \qquad (D)\ $8$")
        q_options = VGroup(q_options1, q_options2).arrange(DOWN, buff=0.25).scale(0.95).set_color(LIGHT_GREY)

        q_group = VGroup(q_p1, q_p2, q_p3, q_options).arrange(DOWN, buff=0.45)

        if q_group.width > 7.5:
            q_group.scale(7.5 / q_group.width)

        question_box = RoundedRectangle(
            corner_radius=0.15,
            height=q_group.height + 1.0,
            width=8.0,
            color=GRAY_D,
            stroke_width=3,
            fill_opacity=0.05
        ).move_to(ORIGIN).set_y(0.3)

        q_group.move_to(question_box.get_center())
        question_frame = VGroup(question_box, q_group)

        self.play(FadeIn(title_group, shift=UP), FadeIn(bottom_txt1, shift=UP))
        self.wait(0.5)
        self.play(FadeIn(question_frame))

        # PAUSE & TRY! Timer
        timer_width = 7.0
        timer_bg  = Line(LEFT, RIGHT, color=GRAY_E, stroke_width=6).scale(timer_width/2).to_edge(DOWN, buff=2.3)
        timer_bar = Line(LEFT, RIGHT, color=CYAN, stroke_width=6).scale(timer_width/2).align_to(timer_bg, LEFT).to_edge(DOWN, buff=2.3)
        timer_label = Group(
            Text("Comment Your", font="Arial", font_size=36, weight=BOLD, color=YELLOW),
            Group(
                Text("Answer!", font="Arial", font_size=36, weight=BOLD, color=YELLOW),
                ImageMobject("emoji.png").scale_to_fit_height(0.7)  # Ensure emoji.png is in your directory
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, buff=0.1).next_to(timer_bg, UP, buff=0.3)

        self.play(Create(timer_bg), FadeIn(timer_label))
        self.play(
            timer_bar.animate(rate_func=linear).scale(0, about_edge=LEFT),
            run_time=5
        )
        self.wait(0.5)

        # ---------------------------------------------------------
        # TRANSITION: Clear question, shrink title
        # ---------------------------------------------------------
        bottom_txt2 = VGroup(
            Text("Follow", font="Arial", font_size=28, weight=BOLD, color=CYAN),
            Text("For More", font="Arial", font_size=28, weight=BOLD, color=CYAN)
        ).arrange(DOWN, buff=0.1).to_edge(DOWN, buff=0.8)

        self.play(
            FadeOut(question_frame),
            FadeOut(timer_bg),
            FadeOut(timer_label),
            FadeOut(timer_bar),
            FadeOut(bottom_txt1)
        )
        self.play(
            title_group.animate.scale(0.65).to_edge(UP, buff=0.5),
            FadeIn(bottom_txt2, shift=UP)
        )
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 2: Root Property
        # ---------------------------------------------------------
        method_label = VGroup(
            Tex(r"Strategy: Use the root property of"),
            Tex(r"the quadratic equation.")
        ).arrange(DOWN, buff=0.1).scale(0.85).set_color(LIGHT_GREY)
        method_label.next_to(title_group, DOWN, buff=0.7)
        self.play(Write(method_label))
        self.wait(0.5)

        sub_cue = VGroup(
            Tex(r"Since $\alpha, \beta$ are roots, they satisfy:"),
            Tex(r"$x^2 + \sqrt{2}x - 8 = 0 \implies x^2 + \sqrt{2}x = 8$")
        ).arrange(DOWN, buff=0.15).scale(0.85).set_color(ORANGE)
        sub_cue.next_to(method_label, DOWN, buff=0.5)
        self.play(FadeIn(sub_cue, shift=RIGHT))
        self.wait(0.3)

        calc1 = VGroup(
            MathTex(r"\alpha^2 + \sqrt{2}\alpha = 8"),
            MathTex(r"\beta^2 + \sqrt{2}\beta = 8")
        ).arrange(DOWN, buff=0.15).scale(0.9)
        calc1.next_to(sub_cue, DOWN, buff=0.4)
        self.play(Write(calc1))
        self.wait(0.3)

        simplify_cue = Tex(r"We will use this substitution:").scale(0.85).set_color(LIGHT_GREY)
        simplify_cue.next_to(calc1, DOWN, buff=0.5)
        self.play(Write(simplify_cue))
        self.wait(0.3)

        eqA_result = MathTex(r"x^2 + \sqrt{2}x = 8").scale(1.1).set_color(YELLOW)
        eqA_result.next_to(simplify_cue, DOWN, buff=0.4)

        boxA = RoundedRectangle(corner_radius=0.1, color=YELLOW, stroke_width=3, fill_opacity=0.05)
        boxA.surround(eqA_result, buff=0.2)
        tag1 = Tex(r"\textbf{(1)}", color=YELLOW, font_size=32).next_to(boxA, RIGHT, buff=0.2)

        self.play(Write(eqA_result))
        self.play(Create(boxA), Write(tag1))
        self.wait(1)

        equation_A_group = VGroup(boxA, tag1, eqA_result)

        self.play(FadeOut(sub_cue), FadeOut(calc1), FadeOut(simplify_cue), FadeOut(method_label))
        self.play(equation_A_group.animate.next_to(title_group, DOWN, buff=0.7))
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 3: Expand Numerator & Apply Condition
        # ---------------------------------------------------------
        resub_cue = VGroup(
            Tex(r"Expand the numerator $U_{10} + \sqrt{2}U_9$:")
        ).arrange(DOWN, buff=0.1).scale(0.85).set_color(LIGHT_GREY)
        resub_cue.next_to(equation_A_group, DOWN, buff=0.4)
        self.play(Write(resub_cue))
        self.wait(0.5)

        calc2 = MathTex(
            r"= (\alpha^{10} + \beta^{10}) + \sqrt{2}(\alpha^9 + \beta^9)"
        ).scale(0.85).set_color(WHITE)
        calc2.next_to(resub_cue, DOWN, buff=0.25)
        self.play(Write(calc2))
        self.wait(0.3)

        bc_cue = VGroup(
            Tex(r"Factor out $\alpha^8$ and $\beta^8$:"),
        ).arrange(DOWN, buff=0.15).scale(0.85).set_color(ORANGE)
        bc_cue.next_to(calc2, DOWN, buff=0.35)
        self.play(FadeIn(bc_cue, shift=RIGHT))
        self.wait(0.3)

        calc4 = MathTex(
            r"= \alpha^8(\alpha^2 + \sqrt{2}\alpha) + \beta^8(\beta^2 + \sqrt{2}\beta)"
        ).scale(0.85).set_color(WHITE)
        calc4.next_to(bc_cue, DOWN, buff=0.25)
        self.play(Write(calc4))
        self.wait(0.3)

        eqB_result = MathTex(
            r"= \alpha^8(8) + \beta^8(8) = 8(\alpha^8 + \beta^8)"
        ).scale(0.95).set_color(YELLOW)
        eqB_result.next_to(calc4, DOWN, buff=0.3)

        boxB = RoundedRectangle(corner_radius=0.1, color=YELLOW, stroke_width=3, fill_opacity=0.05)
        boxB.surround(eqB_result, buff=0.2)
        tag2 = Tex(r"\textbf{(2)}", color=YELLOW, font_size=32).next_to(boxB, RIGHT, buff=0.2)

        self.play(Write(eqB_result))
        self.play(Create(boxB), Write(tag2))
        self.wait(1)

        equation_B_group = VGroup(boxB, tag2, eqB_result)

        self.play(FadeOut(resub_cue), FadeOut(calc2), FadeOut(bc_cue), FadeOut(calc4))
        self.play(equation_B_group.animate.next_to(equation_A_group, DOWN, buff=0.5))
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 4: Evaluate Fraction
        # ---------------------------------------------------------
        eval_cue = Tex(r"Recall that $\alpha^8 + \beta^8 = U_8$. Evaluate:").scale(0.85).set_color(LIGHT_GREY)
        eval_cue.next_to(equation_B_group, DOWN, buff=0.6)
        self.play(Write(eval_cue))
        self.wait(0.3)

        final_step = MathTex(
            r"\frac{U_{10} + \sqrt{2}U_9}{2U_8} = \frac{8(\alpha^8 + \beta^8)}{2(\alpha^8 + \beta^8)}"
        ).scale(0.9).set_color(WHITE)
        final_step.next_to(eval_cue, DOWN, buff=0.4)
        self.play(Write(final_step))
        self.wait(0.5)

        final_res_step = MathTex(
            r"= \frac{8U_8}{2U_8} = 4"
        ).scale(1.1).set_color(WHITE)
        final_res_step.next_to(final_step, DOWN, buff=0.35)
        self.play(Write(final_res_step))
        self.wait(1)

        # ---------------------------------------------------------
        # SCENE 5: Final Answer
        # ---------------------------------------------------------
        self.play(
            FadeOut(equation_A_group),
            FadeOut(equation_B_group),
            FadeOut(title_group),
            FadeOut(eval_cue),
            FadeOut(final_step),
            FadeOut(final_res_step)
        )

        answer_label = MathTex(r"\text{Answer} = \mathbf{4}").scale(1.8).set_color(WHITE)
        answer_label.move_to(ORIGIN)
        self.play(Write(answer_label))

        final_box = RoundedRectangle(corner_radius=0.15, color=GREEN_A, stroke_width=4)
        final_box.surround(answer_label, buff=0.35)
        self.play(Create(final_box), answer_label.animate.set_color(GREEN_C), run_time=0.6)
        self.wait(1.5)
        
        self.play(FadeOut(VGroup(answer_label, final_box, bottom_txt2)), run_time=0.5)
        self.wait(0.2)
