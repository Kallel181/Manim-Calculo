from manim import *
from manim_presentation import Slide

class maximo_minimo(Slide):
    def construct(self):      
        WM = MathTex('KallelFiori').scale(0.5)
        WM.set_opacity(0.4)
        WM.move_to([6,-3.5,0])
        self.add(WM)
        
        #Objeto Manim que armazena o texto Latex da função as ser desenhada
        function_tex = MathTex(r'f(x)=x^3-12x^2+45x-48')
        
        #Objeto Manim que armazena o texto Latex da derivada da função as ser desenhada
        derivative_tex = MathTex('f\'(x)=3x^2-24x+45')
        #raizes: 5 e 3 

        #Objeto Manim que armazena os eixos cartesianos
        #Com alterações na função a ser mostrada é importante mudar o valores do graficos para que
        #a função seja melhor desenhada.
        axes1 = (
            Axes(
                x_range = [0,8,1],
                x_length = 8,
                y_range = [0,20,5],
                y_length = 6,
                axis_config = {"include_numbers": True, "include_tip":False},
            )
            .set_color(WHITE)
        )
        
        #Adicionando texto para indicar os eixos
        axes1_labels = axes1.get_axis_labels(x_label="x",y_label="y")
        
        #Função para desenharmos o grafico
        def f(x):
            return (x**3 - (12*(x**2)) + 45*x) - 48
        
        #Função para desenharmos o grafico da função derivada
        def derivative(x):
            return ((3*x**2)-(24*x)+45)
        
        graph1 = axes1.plot(
            f, x_range=[1.8,6.5], color=BLUE
        )

        x = ValueTracker(2)
        dx = 0.001

        tangent = always_redraw(
            lambda: axes1.get_secant_slope_group(
                x = x.get_value(),
                graph = graph1,
                dx = dx,
                secant_line_color = GREEN,
                secant_line_length = 4,
            )
        )

        #Objeto Manim que armazena o ponto no grafico correspondente ao valor de p.
        #O objeto precisa estar dentro da função always_redraw uma vez que os valores de p ira ser
        #alterado posteriomente.
        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes1.c2p(x.get_value(),f(x.get_value())))
        )
        
        #Movendo o ponto para a camada mais acima, para que a reta tangente e o grafico não sejam desenhados
        #acima do ponto
        dot1.z_index = 1

        left_elements = VGroup(tangent,graph1,axes1,axes1_labels,function_tex)

        axes2 = (
            Axes(
                x_range = [0,7,1],
                x_length = 7,
                y_range = [-3,2,1],
                y_length = 6,
                axis_config = {"include_numbers": True, "include_tip":False},
            )
            .set_color(WHITE)
        )
        axes2.z_index = 1

        axes2_labels = axes2.get_axis_labels(x_label="x",y_label="y")

        graph2 = axes2.plot(
            derivative, x_range=[2.8,5.2], color=BLUE
        )

        
        derivative_tex.shift(UP*3)
        right_elements = VGroup(derivative_tex,axes2,axes2_labels,graph2)
        right_elements.scale(0.7)
        right_elements.shift(RIGHT*4)
        right_elements.shift(DOWN*0.2)



        self.play(Write(function_tex))
        self.wait(0.1)
        self.pause()

        function_tex_target = function_tex.generate_target()
        function_tex_target.shift(UP*3)
        self.play(MoveToTarget(function_tex))
        self.wait(0.1)
        self.pause()

        self.play(Write(VGroup(axes1,graph1,axes1_labels,tangent,dot1)))
        self.wait(0.1)
        self.pause()

        left_elements_target = left_elements.generate_target()
        left_elements_target.scale(0.7)
        left_elements_target.shift(LEFT*3)
        self.play(MoveToTarget(left_elements))
        self.wait(0.1)
        self.pause()


        self.play(Write(derivative_tex))
        self.wait(0.1)
        self.pause()

        self.play(Write(VGroup(axes2,axes2_labels,graph2)))
        self.wait(0.1)
        self.pause()

        derivative_tex_target = derivative_tex.generate_target()
        derivative_tex_target.shift(UP)
        self.play(MoveToTarget(derivative_tex))

        solution_tex = MathTex('f\'(x)=0\\left\\{\\begin{matrix}x=3\\\\x=5\\end{matrix}\\right.').scale(0.7)
        solution_tex.next_to(derivative_tex,DOWN)
        self.play(Write(solution_tex))

        right_dot1 = Dot().move_to(axes2.c2p(3,0))
        right_dot2 = Dot().move_to(axes2.c2p(5,0))
        
        right_dot1.z_index = 1
        right_dot2.z_index = 1

        self.play(Write(VGroup(right_dot1,right_dot2))) 
        self.wait(0.1)
        self.pause()

        x_value_tex = always_redraw(
            lambda:
            MathTex('x=',str(x.get_value())[:5])
            .scale(0.7)
            .shift(UP*3+LEFT)
        )
        
        derivative_function_value_tex = always_redraw (
            lambda:  
                MathTex('f\'(',str(x.get_value())[:5],')=',str(derivative(x.get_value()))[:5])
                .scale(0.7)   
                .next_to(x_value_tex,DOWN)
        )
    
        derivative_function_value_tex.next_to(x,DOWN)

        self.play(Write(VGroup(x_value_tex,derivative_function_value_tex)))
        self.wait(0.1)
        self.pause()

        self.play(x.animate.set_value(3),run_time=2)
        self.wait(0.1)
        self.pause()

        self.play(x.animate.set_value(5),run_time=2)
        self.wait(0.1)
        self.pause()
        





















        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait()