from manim import *
from manim_presentation import Slide

class maximo_minimo(Slide):
    def construct(self):      
        WM = MathTex('KallelFiori').scale(0.5)
        WM.set_opacity(0.4)
        WM.move_to([6,-3.5,0])
        self.add(WM)
        
        
        function = MathTex(r'f(x)=\frac{x^3}{10}-\frac{12x^2}{10}+\frac{45x}{10}-63')
        
        derivative = MathTex('f\'(x)=\\frac{3x^2}{10}-\\frac{24x}{10}+\\frac{45}{10}')
        #raizes: 5 e 3 

        axes = (
            Axes(
                x_range = [0,10,1],
                x_length = 9,
                y_range = [0,20,5],
                y_length = 6,
                axis_config = {"include_numbers": True, "include_tip":False},
            )
            .set_color(WHITE)
        )
        
        #Adicionando texto para indicar os eixos
        axes_labels = axes.get_axis_labels(x_label="x",y_label="y")
        
        #Função para desenharmos o grafico
        def f(x):
            return 0.1 * (x - 2) * (x - 5) * (x - 7) + 7
        
        def derivative(x):
            return 0.1 * ((3*x**2)-(24*x)+45)
        
        graph = axes.plot(
            f, x_range=[0,10], color=BLUE
        )

        x = ValueTracker(2)
        dx = 0.001

        tangent = always_redraw(
            lambda: axes.get_secant_slope_group(
                x = x.get_value(),
                graph = graph,
                dx = dx,
                secant_line_color = GREEN,
                secant_line_length = 8,
            )
        )