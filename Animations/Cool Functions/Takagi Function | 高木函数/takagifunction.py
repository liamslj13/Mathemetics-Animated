from manim import *
import numpy as np

class TakagiFunction(Scene):

    def construct(self):
        
        text = Text("Takagi Function")
        info = Text("This function is continuous everywhere.")
        info2 = Text("Yet, differentiable nowhere.", 
                     t2w={'nowhere':BOLD}, 
                     t2s={'nowhere':ITALIC}, 
                     t2c={'nowhere':BLUE}, 
                     disable_ligatures=True
        )
        
        q1 = Text("So what does it look like?", 
                  t2w={'So what does it look like?':BOLD}, 
                  t2s={'So what does it look like?':ITALIC}, 
                  t2c={'So what does it look like?':RED}, 
                  disable_ligatures=False
        )
        
        self.play(Write(text), run_time=2)
        self.wait(2)
        self.play(FadeOut(text), run_time=2)
        
        takagi_function_LaTex = MathTex(r"\text{T}(x) = \sum_{n=0}^{\infty} \frac{s(2^n x)}{2^n},")
        takagi_function_s_latex = MathTex(r"s(x) = \min_{n \in \mathbb{Z}} |x - n|")
        
        self.play(Write(takagi_function_LaTex))
        self.play(takagi_function_LaTex.animate.scale(0.7))
        self.play(takagi_function_LaTex.animate.to_edge(LEFT / 2))
        
        self.play(Write(takagi_function_s_latex))
        self.play(takagi_function_s_latex.animate.scale(0.7))
        self.play(takagi_function_s_latex.animate.next_to(takagi_function_LaTex))
        self.wait(2)
        self.play(FadeOut(takagi_function_LaTex, takagi_function_s_latex))
        
        info2.next_to(info, DOWN)
        
        self.play(Write(info), run_time=2)
        self.wait(1)
        self.play(Write(info2), run_time=2)
        self.wait(1)
        self.play(FadeOut(info, info2))
        self.play(Write(q1.scale(0.80)), run_time=2)
        self.wait(2)
        self.play(FadeOut(q1))
        
        axes = Axes(
            x_range=[-0.01, 1, 0.1],
            y_range=[-0.01, 1, 0.1],
            x_length=10,
            axis_config={"color":BLUE_B},
            x_axis_config={
                "numbers_to_include": np.arange(-0.01, 1.01, 0.2),
                "numbers_with_elongated_ticks": np.arange(0, 1, 0.2),
            },
            y_axis_config={
                "numbers_to_include": np.arange(-0.01, 1.01, 0.2),
                "numbers_with_elongated_ticks": np.arange(0, 1, 0.2),
            },
            tips=False
        )
        def s(x):
            return min(abs(x - n) for n in range(int(x) - 1, int(x) + 2))
        
 
        
        takagi_function = axes.plot(lambda x : sum(s(2**n * x) / 2**n for n in range(100)), color=RED)
        
        
        takagi_function_LaTex_two = MathTex(r"\text{T}(x) = \sum_{n=0}^{\infty} \frac{s(2^n x)}{2^n}", color=RED)
        
        self.play(Write(takagi_function_LaTex_two), run_time=2)
        self.play(takagi_function_LaTex_two.animate.scale(0.75))
        self.play(takagi_function_LaTex_two.animate.to_edge(RIGHT + UP))
        
        self.play(Write(axes), run_time=2)
        self.play(Write(takagi_function), run_time=2)
        self.play(FadeOut(takagi_function, takagi_function_LaTex_two), run_time=2)
        

        takagi_function_LaTex_internal = MathTex(r"f(x) = \frac{s(2^n x)}{2^n}, \text{  }s(x) = \min_{n \in \mathbb{Z}} |x - n|", color=YELLOW).scale(0.7)
        takagi_function_LaTex_internal.to_edge(RIGHT + UP)

        k = 0
        k_tracker = ValueTracker(k)
        n_text = Text("n = ").shift(UP * 2)

        self.play(Write(takagi_function_LaTex_internal))
        self.play(takagi_function_LaTex_internal.animate.to_edge(RIGHT + UP))
        
        h_value = Integer(k_tracker.get_value()).next_to(n_text, RIGHT)
        h_value.scale(1.1)

        def update_h_value(h_value):
            h_value.set_value(int(k_tracker.get_value()))
            
        k_group = VGroup(n_text, h_value).scale(0.45)
        k_group.color=YELLOW
        h_value.add_updater(update_h_value)
        
        self.play(Write(k_group.next_to(takagi_function_LaTex_internal, DOWN / 2)))
        self.wait(2)
        
        h = 0
        while h < 11:
            takagi_function_s = axes.plot(lambda x: (s(2**k * x) / 2**k), color=YELLOW)
            if h == 10:
                self.play(Write(takagi_function_s), run_time=2)
                self.wait(3)
            else:
                self.play(Write(takagi_function_s), run_time=1)
                self.play(FadeOut(takagi_function_s), run_time=1)
                self.play(k_tracker.animate.increment_value(1))
            h += 1
            k += 1
            
        self.play(Unwrite(takagi_function_s))
        self.play(Unwrite(n_text), Unwrite(h_value))
        self.play(Unwrite(takagi_function_LaTex_internal))
        self.play(Unwrite(axes))  
        
        bye_bye = Text("By Liam Jay (世樂)", 
                  t2w={'By Liam Jay (世樂)':BOLD}, 
                  t2s={'By Liam Jay (世樂)':ITALIC}, 
                  t2c={'By Liam Jay (世樂)':PURPLE}, 
                  disable_ligatures=True,
        ).scale(0.5)    
        
        self.play(Write(bye_bye), run_time=2)
        self.wait(2)
        self.play(Unwrite(bye_bye))
        self.wait(2)  