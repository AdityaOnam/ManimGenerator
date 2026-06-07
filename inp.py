from manim import *
import json

# Configure for 9:16 vertical resolution
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.background_color = "#000000"

# Load colors from configuration file
with open("colors.json", "r") as f:
    colors = json.load(f)

YELLOW = colors.get("YELLOW", "#ffff00")
CYAN = colors.get("CYAN", "#00e1ff")
WHITE = colors.get("WHITE", "#ffffff")
GREEN_C = colors.get("GREEN_C", "#55ff55")
GREEN_A = colors.get("GREEN_A", "#a3ffa3")
LIGHT_GREY = colors.get("LIGHT_GREY", "#bbbbbb")

class MathProblem(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # SCENE 1: Initial Question Frame & Titles
        # ---------------------------------------------------------
        # Titles (Split into 3 lines to fit vertical layout without clipping inside a container box)
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
        
        # Question Frame (Matrix Question)
        q_t1 = Tex(r"If $A$ is a $3 \times 3$ matrix and $|A|=2$,").scale(1.1)
        q_t2 = Tex(r"then the value of").scale(1.1)
        q_eq = MathTex(r"|3 \text{adj}(|3A| A^2)|").scale(1.4).set_color(YELLOW)
        q_t3 = Tex(r"is \_\_\_\_\_\_\_\_\_\_\_\_\_\_.").scale(1.1)
        
        q_group = VGroup(q_t1, q_t2, q_eq, q_t3).arrange(DOWN, buff=0.45)
        
        # Enforce safety max width
        if q_group.width > 7.0:
            q_group.scale(7.0 / q_group.width)
            
        question_box = RoundedRectangle(
            corner_radius=0.15,
            height=q_group.height + 0.9,
            width=7.5, # Fixed safe width matching begin.py
            color=GRAY_D,
            stroke_width=3,
            fill_opacity=0.05
        ).move_to(ORIGIN)
        
        q_group.move_to(question_box.get_center())
        
        question_frame = VGroup(question_box, q_group)

        # Animate Scene 1
        self.play(FadeIn(title_group, shift=UP))
        self.play(FadeIn(question_frame))
        
        # Progress Timer (Pause & Try)
        timer_width = 7.0
        timer_bg = Line(LEFT, RIGHT, color=GRAY_E, stroke_width=6).scale(timer_width/2).to_edge(DOWN, buff=2.2)
        timer_bar = Line(LEFT, RIGHT, color=CYAN, stroke_width=6).scale(timer_width/2).align_to(timer_bg, LEFT).to_edge(DOWN, buff=2.2)
        timer_label = Tex("PAUSE \& TRY!", font_size=36, color=CYAN).next_to(timer_bg, UP, buff=0.3)
        
        self.play(Create(timer_bg), FadeIn(timer_label))
        self.play(timer_bar.animate(rate_func=linear).scale(0, about_edge=LEFT), run_time=3)
        self.wait(0.5)

        # ---------------------------------------------------------
        # TRANSITION: Setup for Solving
        # ---------------------------------------------------------
        bottom_txt2_line1 = Text("Follow for", font_size=32, weight=BOLD, color=CYAN)
        bottom_txt2_line2 = Text("more", font_size=32, weight=BOLD, color=CYAN)
        bottom_txt2 = VGroup(bottom_txt2_line1, bottom_txt2_line2).arrange(DOWN, buff=0.1)
        bottom_txt2.to_edge(DOWN, buff=0.6)

        self.play(FadeOut(question_frame), FadeOut(timer_bg), FadeOut(timer_label), FadeOut(timer_bar))
        self.play(
            title_group.animate.scale(0.65).to_edge(UP, buff=0.5),
            FadeIn(bottom_txt2, shift=UP)
        )
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 2: First Substitution & Property
        # ---------------------------------------------------------
        given_text = MathTex(r"\text{Given: } A \text{ is a } 3 \times 3 \text{ matrix, } |A| = 2").scale(1.1)
        given_text.next_to(title_group, DOWN, buff=0.6)
        self.play(Write(given_text))
        
        eq_target = MathTex(r"E = |3 \text{adj}(|3A| A^2)|").scale(1.2)
        eq_target.next_to(given_text, DOWN, buff=0.8)
        self.play(Write(eq_target))
        self.wait(0.5)

        prop1 = MathTex(r"\text{Using: } |kA| = k^n|A|").scale(1.0).set_color(YELLOW)
        prop1.next_to(eq_target, DOWN, buff=0.8)
        self.play(FadeIn(prop1, shift=UP))
        
        calc1 = MathTex(r"|3A| = 3^3|A| = 3^3(2)").scale(1.1)
        calc1.next_to(prop1, DOWN, buff=0.4)
        self.play(Write(calc1))
        self.wait(0.5)
        
        eq1 = MathTex(r"E = |3 \text{adj}((3^3 \cdot 2) A^2)|").scale(1.2)
        eq1.next_to(calc1, DOWN, buff=0.6)
        self.play(TransformFromCopy(eq_target, eq1))
        self.wait(1)
        
        # Clean up
        self.play(FadeOut(VGroup(eq_target, prop1, calc1)))
        self.play(eq1.animate.next_to(given_text, DOWN, buff=0.6))
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 3: Pulling scalar from det & Adjoint Property
        # ---------------------------------------------------------
        step2_text = Tex(r"Pull scalar $3$ out of determinant ($n=3$):").scale(0.9).set_color(LIGHT_GREY)
        step2_text.next_to(eq1, DOWN, buff=0.6)
        
        eq2 = MathTex(r"E = 3^3 |\text{adj}((3^3 \cdot 2) A^2)|").scale(1.2)
        eq2.next_to(step2_text, DOWN, buff=0.4)
        self.play(Write(step2_text), TransformFromCopy(eq1, eq2))
        self.wait(0.8)

        prop2 = MathTex(r"\text{Using: } \text{adj}(kM) = k^{n-1}\text{adj}(M)").scale(1.0).set_color(YELLOW)
        prop2.next_to(eq2, DOWN, buff=0.8)
        self.play(FadeIn(prop2, shift=UP))
        
        eq3 = MathTex(r"E = 3^3 |(3^3 \cdot 2)^2 \text{adj}(A^2)|").scale(1.2)
        eq3.next_to(prop2, DOWN, buff=0.4)
        self.play(TransformFromCopy(eq2, eq3))
        self.wait(1)
        
        # Clean up
        self.play(FadeOut(VGroup(eq1, step2_text, eq2, prop2)))
        self.play(eq3.animate.next_to(given_text, DOWN, buff=0.6))
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 4: Pulling scalar from det again & Adjoint Det Property
        # ---------------------------------------------------------
        step3_text = Tex(r"Pull $(3^3 \cdot 2)^2$ out of determinant ($n=3$):").scale(0.9).set_color(LIGHT_GREY)
        step3_text.next_to(eq3, DOWN, buff=0.6)
        
        eq4 = MathTex(r"E = 3^3 ((3^3 \cdot 2)^2)^3 |\text{adj}(A^2)|").scale(1.1)
        eq4.next_to(step3_text, DOWN, buff=0.4)
        self.play(Write(step3_text), TransformFromCopy(eq3, eq4))
        
        eq5 = MathTex(r"E = 3^3 (3^3 \cdot 2)^6 |\text{adj}(A^2)|").scale(1.2)
        eq5.next_to(eq4, DOWN, buff=0.4)
        self.play(TransformFromCopy(eq4, eq5))
        self.wait(0.8)
        
        prop3 = MathTex(r"\text{Using: } |\text{adj}(M)| = |M|^{n-1}").scale(1.0).set_color(YELLOW)
        prop3.next_to(eq5, DOWN, buff=0.6)
        self.play(FadeIn(prop3, shift=UP))
        
        eq6 = MathTex(r"E = 3^3 (3^3 \cdot 2)^6 (|A^2|)^2").scale(1.2)
        eq6.next_to(prop3, DOWN, buff=0.4)
        self.play(TransformFromCopy(eq5, eq6))
        self.wait(1)
        
        # Clean up
        self.play(FadeOut(VGroup(eq3, step3_text, eq4, eq5, prop3)))
        self.play(eq6.animate.next_to(given_text, DOWN, buff=0.6))
        self.wait(0.5)

        # ---------------------------------------------------------
        # SCENE 5: Evaluating Powers & Final Answer
        # ---------------------------------------------------------
        step4_text = Tex(r"Substitute $|A^2| = |A|^2 = 2^2 = 4$").scale(0.9).set_color(LIGHT_GREY)
        step4_text.next_to(eq6, DOWN, buff=0.6)
        
        eq7 = MathTex(r"E = 3^3 (3^3 \cdot 2)^6 (4)^2").scale(1.2)
        eq7.next_to(step4_text, DOWN, buff=0.4)
        self.play(Write(step4_text), TransformFromCopy(eq6, eq7))
        
        eq8 = MathTex(r"E = 3^3 \cdot 3^{18} \cdot 2^6 \cdot (2^2)^2").scale(1.2)
        eq8.next_to(eq7, DOWN, buff=0.4)
        self.play(TransformFromCopy(eq7, eq8))
        
        eq9 = MathTex(r"E = 3^{21} \cdot 2^{10}").scale(1.3)
        eq9.next_to(eq8, DOWN, buff=0.4)
        self.play(TransformFromCopy(eq8, eq9))
        self.wait(1)

        step5_text = Tex(r"Rearrange: $3^{11} \cdot 3^{10} \cdot 2^{10}$").scale(0.9).set_color(LIGHT_GREY)
        step5_text.next_to(eq9, DOWN, buff=0.6)
        self.play(Write(step5_text))
        
        final_ans = MathTex(r"3^{11} \cdot 6^{10}").scale(2.0).set_color(GREEN_C)
        final_ans.next_to(step5_text, DOWN, buff=0.6)
        box_ans = RoundedRectangle(
            corner_radius=0.15,
            width=final_ans.width + 1.2,
            height=final_ans.height + 0.8,
            color=YELLOW,
            stroke_width=4,
            fill_opacity=0.1
        ).move_to(final_ans)
        
        # Combined fast animation for final answer and box
        self.play(Write(final_ans), Create(box_ans), run_time=0.5)
        # Fade out everything including the final answer and surrounding elements
        self.play(FadeOut(VGroup(final_ans, box_ans, title_group, given_text, eq6, step4_text,
            eq7, eq8, eq9, step5_text, bottom_txt2)), run_time=0.5)
        self.wait(0.2)