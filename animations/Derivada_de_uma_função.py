from manim import *
from manim_presentation import Slide

class derivada(Slide):
    def construct(self):
        axes = (
            Axes(
                x_range = [-3,3,1],
                x_length = 6,
                y_range = [0,6,1],
                y_length = 6,
                axis_config = {"include_numbers": True, "include_tip":False},
            )
            .set_color(WHITE)
        )

        axes_labels = axes.get_axis_labels(x_label="x",y_label="y")

        def f(x):
            return (x**2)
        
        graph = axes.plot(f,x_range=[-2.1,2.1])


        function_tex = MathTex('f(x)=x^2')
        function_tex_target = function_tex.generate_target()
        function_tex_target.shift(UP*3)


        derivative_definition = MathTex('f\'(p)=','\\lim_{x\\rightarrow p}\\frac{f(x)-f(p)}{x-p}')
        derivative_definition.shift(UP*2)

        p = MathTex('p=','1').scale(0.8).shift(LEFT*3+UP*3)

        derivative_definition_calc1 = MathTex('f\'(1)=','\\lim_{x\\rightarrow 1}\\frac{f(x)-f(1)}{x-1}')
        derivative_definition_calc1.shift(UP*2)








        self.play(Write(function_tex))
        self.wait(0.1)
        self.pause()

        self.play(MoveToTarget(function_tex))
        self.wait(0.1)
        self.pause()

        self.play(Write(derivative_definition))
        self.wait(0.1)
        self.pause()

        self.play(Write(p))
        self.wait(0.1)
        self.pause()

        self.play(FadeIn(derivative_definition_calc1),FadeOut(derivative_definition))
        self.wait(0.1)
        self.pause()

        





