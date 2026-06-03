from manim import *

# Professional Color Palette
COLOR_BG = "#121212"
COLOR_PRIMARY = "#3498db" # Soft Blue
COLOR_ACCENT = "#f1c40f"  # Gold/Yellow
COLOR_CORRECT = "#2ecc71" # Green
COLOR_INCORRECT = "#e74c3c" # Red

config.background_color = COLOR_BG
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

class QuizAnimation(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # 1. INTRO HOOK (Social Media Safe)
        # ---------------------------------------------------------
        hook_text = VGroup(
            Tex(r"\textbf{JEE Adv. 2026: Physics}", font_size=42, color=COLOR_PRIMARY),
            Tex(r"Projectile Motion", font_size=48, color=WHITE)
        ).arrange(DOWN, buff=0.3)
        
        # Max width safety check
        if hook_text.width > 7.5:
            hook_text.scale(7.5 / hook_text.width)

        hook_bg = RoundedRectangle(
            corner_radius=0.2, 
            width=hook_text.width + 1.0, 
            height=hook_text.height + 0.8, 
            color=COLOR_PRIMARY, 
            fill_opacity=0.1
        ).move_to(hook_text)
        
        intro = VGroup(hook_bg, hook_text)
        self.play(FadeIn(hook_bg), Write(hook_text), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(intro, shift=UP))

        # ---------------------------------------------------------
        # 2. THE QUESTION CARD
        # ---------------------------------------------------------
        q_header = Tex("Analyze this:", color=GRAY_A, font_size=38)
        
        # Exact text from the image provided
        question = Tex(
            r"A ball is thrown from the location $(x_0, y_0) = (0, 0)$ of a\\"
            r"horizontal playground with an initial speed $v_0$ at an angle $\theta_0$\\"
            r"from the $+x$-direction. The ball is to be hit by a stone, which\\"
            r"is thrown at the same time from the location $(x_1, y_1) = (L, 0)$.\\[0.3cm]"
            r"The stone is thrown at an angle $(180^\circ - \theta_1)$ from the\\"
            r"$+x$-direction with a suitable initial speed. For a fixed $v_0$,\\"
            r"when $(\theta_0, \theta_1) = (45^\circ, 45^\circ)$, the stone hits the ball after\\"
            r"time $T_1$, and when $(\theta_0, \theta_1) = (60^\circ, 30^\circ)$, it hits the ball\\"
            r"after time $T_2$.\\[0.3cm]"
            r"In such a case, $(T_1 / T_2)^2$ is \_\_\_\_\_.", 
            font_size=38
        )
        
        q_group = VGroup(q_header, question).arrange(DOWN, buff=0.4)
        
        # Enforce max width of 7.5 for safe zones
        if q_group.width > 7.5:
            q_group.scale(7.5 / q_group.width)
            
        question_box = RoundedRectangle(
            corner_radius=0.15, 
            height=q_group.height + 1.0, 
            width=max(q_group.width + 1.0, 7.5), # Standardize width if small
            color=GRAY_D, 
            fill_opacity=0.05
        ).to_edge(UP, buff=1.0)
        
        q_group.move_to(question_box.get_center())

        self.play(Create(question_box), FadeIn(q_header))
        self.play(Write(question))
        self.wait(1)

        # ---------------------------------------------------------
        # 3. THE OPTIONS (Dynamically Sized but width-capped)
        # ---------------------------------------------------------
        options_raw = [
            r"1",
            r"2",
            r"3",
            r"4"
        ]
        
        option_vgroup = VGroup()
        for text in options_raw:
            txt = Tex(text, font_size=38)
            if txt.width > 6.5: # Strict width for options to allow padding
                txt.scale(6.5 / txt.width)
                
            bg = RoundedRectangle(
                corner_radius=0.1, 
                height=txt.height + 0.6, 
                width=7.5, # Fixed safe width for uniform look
                color=GRAY_E, 
                fill_opacity=0.2
            )
            txt.move_to(bg.get_center())
            opt = VGroup(bg, txt)
            option_vgroup.add(opt)
            
        option_vgroup.arrange(DOWN, buff=0.4).next_to(question_box, DOWN, buff=0.8)

        self.play(
            AnimationGroup(
                *[FadeIn(opt, shift=RIGHT*0.5) for opt in option_vgroup],
                lag_ratio=0.2
            )
        )

        # ---------------------------------------------------------
        # 4. MODERN PROGRESS TIMER
        # ---------------------------------------------------------
        timer_width = 7.0 # Well within safe bounds
        timer_bg = Line(LEFT, RIGHT, color=GRAY_E, stroke_width=8).scale(timer_width/2).to_edge(DOWN, buff=2.0)
        timer_bar = Line(LEFT, RIGHT, color=COLOR_PRIMARY, stroke_width=8).scale(timer_width/2).align_to(timer_bg, LEFT).to_edge(DOWN, buff=2.0)
        
        timer_label = Tex("PAUSE \& TRY!", font_size=36, color=COLOR_PRIMARY).next_to(timer_bg, UP, buff=0.3)

        self.play(Create(timer_bg), FadeIn(timer_label))
        self.play(timer_bar.animate(rate_func=linear).scale(0, about_edge=LEFT), run_time=5)
        self.play(FadeOut(timer_label), timer_bar.animate.set_color(COLOR_INCORRECT))

        # ---------------------------------------------------------
        # 5. THE EXPLANATION
        # ---------------------------------------------------------
        CORRECT_INDEX = 1
        
        incorrect_anims = []
        for i in range(4):
            if i != CORRECT_INDEX:
                incorrect_anims.append(option_vgroup[i].animate.set_opacity(0.15))
                
        self.play(
            *incorrect_anims,
            option_vgroup[CORRECT_INDEX][0].animate.set_color(COLOR_CORRECT).set_fill(opacity=0.3),
            option_vgroup[CORRECT_INDEX][1].animate.scale(1.1).set_color(WHITE)
        )
        
        logic_text = VGroup(
            Tex("Logic:", color=COLOR_ACCENT, font_size=42),
            Tex(r"The correct integer answer is 2.", font_size=38),
            Tex(r"$(T_1/T_2)^2 = 2$", font_size=38, color=COLOR_CORRECT)
        ).arrange(DOWN, buff=0.3)

        if logic_text.width > 7.0:
            logic_text.scale(7.0 / logic_text.width)

        logic_bg = RoundedRectangle(
            corner_radius=0.15,
            width=logic_text.width + 1.2,
            height=logic_text.height + 0.8,
            color=GRAY_C,
            fill_color=GRAY_E,
            fill_opacity=0.85
        ).move_to(logic_text)
        
        explanation = VGroup(logic_bg, logic_text).next_to(option_vgroup[CORRECT_INDEX], DOWN, buff=0.8)

        # Shift up slightly if it's too close to the bottom (avoiding captions)
        if explanation.get_bottom()[1] < -6.5:
            shift_amount = -6.5 - explanation.get_bottom()[1]
            self.play(
                option_vgroup.animate.shift(UP * shift_amount),
                question_box.animate.shift(UP * shift_amount),
                q_group.animate.shift(UP * shift_amount)
            )
            explanation.shift(UP * shift_amount)

        self.play(FadeIn(explanation, shift=UP*0.3))
        self.wait(3)