from manim import *
from manim_presentation import Slide

class tangente(Slide):
    def construct(self):
        #Objeto Manim que armazena os eixos cartesianos
        axes = (
            Axes(
                x_range = [0,10,1],
                x_length = 9,
                y_range = [0,20,5],
                y_length = 6,
                axis_config = {"include_numbers": True, "include_tip":False},
            )
            .to_edge(DL)
            .set_color(WHITE)
        )
        
        #Adicionando texto para indicar os eixos
        axes_labels = axes.get_axis_labels(x_label="x",y_label="y")
        
        #Função para desenharmos o grafico
        def f(x):
            return (x - 2) * (x - 5) * (x - 7) + 7
        
        #Objeto Manim que armazena o texto Latex da função que estamos desenhando o grafico
        func_text = Tex(r'f(x)=')

        #Objeto Manim que armazena o grafico da função previamente definida
        graph = axes.plot(
            f, x_range=[0,10], color=BLUE
        )

        #Value Trackers armazenam os valores de x e dx, e podem ser usados para animar a reta secante 
        #posteriormente.
        #Os valores iniciais podem ser alterados conforme necessidade.
        x = ValueTracker(7)
        dx = ValueTracker(2)

        #Objeto Manim que armazena a reta secante ao grafico conforme x e dx.
        #O objeto precisa estar dentro da função always_redraw uma vez que os calores de x e dx irão ser
        #alterados posteriomente.
        secant = always_redraw(
            lambda: axes.get_secant_slope_group(
                x = x.get_value(),
                graph = graph,
                dx = dx.get_value(),
                dx_line_color = YELLOW,
                dy_line_color = ORANGE,
                dx_label = "dx",
                secant_line_color = GREEN,
                secant_line_length = 8,
            )
        )

        #Objeto Manim que armazena o ponto no grafico correspondente ao valor de x.
        #O objeto precisa estar dentro da função always_redraw uma vez que os calores de x ira ser
        #alterado posteriomente.
        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(x.get_value(), f(x.get_value())))
        )
        
        #Objeto Manim que armazena o ponto no grafico correspondente ao valor de x + dx.
        #O objeto precisa estar dentro da função always_redraw uma vez que os calores de x e dx irão ser
        #alterados posteriomente.
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(
                x.get_value() + dx.get_value(),
                f(x.get_value() + dx.get_value())
            ))
        )
 
        #Funções de animação
        #Agora como todos os objetos já foram definidos, podemos continuar com a animação dos mesmos.
        self.play(Write(VGroup(axes,axes_labels,graph)))
        self.wait(0.1)
        self.pause()

        self.play(Create(VGroup(dot1,dot2,secant)))
        self.pause()

        #Uma vez que os objetos que dependem do valor de x e dx foram colocados dentro das funções 
        #always_redraw eles serão alterados de acordo conforme os valores de x e dx forem alterados.
        self.play(dx.animate.set_value(0.001),run_time=8)
        self.pause()

        self.play(x.animate.set_value(1),run_time=5)
        self.pause()

        self.play(x.animate.set_value(7),run_time=5)
        self.pause()

        self.play(x.animate.set_value(2),run_time=5)
        self.pause()

        self.wait()