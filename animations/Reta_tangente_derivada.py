from manim import *
from manim_presentation import Slide

class tangente(Slide):
    def construct(self):
        #Objeto Manim que armazena os eixos cartesianos
        #Com alterações na função a ser mostrada é importante mudar o valores do graficos para que
        #a função seja melhor desenhada.
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
        
        #Objeto Manim que armazenada o texto Latex da definição de derivada (Guidorizzi)
        derivative = MathTex('f\'(p)=','\\lim_{x\\rightarrow p}\\frac{f(x)-f(p)}{x-p}')
        derivative_target = derivative.generate_target()
        derivative_target.shift(UP*2)

        #Objeto Manim que armazena o texto Latex apenas do limite da definição anterior
        limit = MathTex('\\lim_{x\\rightarrow p}\\frac{f(x)-f(p)}{x-p}').shift(UP*2)

        #Objeto Manim que armazena o grafico da função previamente definida
        graph = axes.plot(
            f, x_range=[0,10], color=BLUE
        )

        #Value Trackers armazenam os valores de p e dx, e podem ser usados para animar a reta secante 
        #posteriormente.
        #Os valores iniciais podem ser alterados conforme necessidade.
        p = ValueTracker(7)
        dx = ValueTracker(2)

        #Objeto Manim que armazena a reta secante ao grafico conforme p e dx.
        #O objeto precisa estar dentro da função always_redraw uma vez que os valores de p e dx irão ser
        #alterados posteriomente.
        secant = always_redraw(
            lambda: axes.get_secant_slope_group(
                x = p.get_value(),
                graph = graph,
                dx = dx.get_value(),
                dx_line_color = YELLOW,
                dy_line_color = ORANGE,
                dy_label = "f(x)-f(p)",
                dx_label = "x-p",
                secant_line_color = GREEN,
                secant_line_length = 8,
            )
        )

        #Objeto Manim que armazena o ponto no grafico correspondente ao valor de p.
        #O objeto precisa estar dentro da função always_redraw uma vez que os valores de p ira ser
        #alterado posteriomente.
        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(p.get_value(), f(p.get_value())))
        )
        
        #Objeto Manim que armazena o ponto no grafico correspondente ao valor de p + dx.
        #O objeto precisa estar dentro da função always_redraw uma vez que os valores de p e dx irão ser
        #alterados posteriomente.
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(
                p.get_value() + dx.get_value(),
                f(p.get_value() + dx.get_value())
            ))
        )

        #Movendo os pontos para a camada mais acima, para que a reta secante e o grafico não sejam desenhados
        #acima dos pontos
        dot1.z_index = 1
        dot2.z_index = 1

        #Objeto Manim que muda de acordo com o valor de x+dx, indicando nosso x
        #O objeto precisa estar dentro da função always_redraw uma vez que os valores de p e dx irão ser
        #alterados posteriomente.
        x_text = always_redraw(
            lambda: Tex(r'x='+str(p.get_value()+dx.get_value())[:3]).scale(0.6).shift(UP+2*LEFT)
        )

        #Objeto Manim que muda de acordo com o valor de x, indicando nosso p
        #O objeto precisa estar dentro da função always_redraw uma vez que o valor de p ira ser
        #alterado posteriomente.
        p_text = always_redraw(
            lambda: Tex(r'p='+str(p.get_value())[:3]).scale(0.6).next_to(x_text,DOWN)
        )  
        
        self.play(Write(derivative))
        self.wait(0.1)
        self.pause()

        self.play(MoveToTarget(derivative))
        self.wait(0.1)
        self.pause()        
        
        #Funções de animação
        #Agora como todos os objetos já foram definidos, podemos continuar com a animação dos mesmos.
        self.play(Write(VGroup(axes,axes_labels,graph)))
        self.wait(0.1)
        self.pause()

        self.play(TransformMatchingTex(derivative,limit))
        self.wait(0.1)
        self.pause()

        self.play(Create(VGroup(dot1,dot2,secant)))
        self.wait(0.1)
        self.pause()

        #Uma vez que os objetos que dependem do valor de x e dx foram colocados dentro das funções 
        #always_redraw eles serão alterados de acordo conforme os valores de x e dx forem alterados.
        self.play(Write(VGroup(x_text,p_text)))
        self.wait(0.1)
        self.pause()        
        
        self.play(dx.animate.set_value(0.001),run_time=8)
        self.wait(0.1)
        self.pause()

        self.play(FadeOut(x_text))
        self.play(p.animate.set_value(1),run_time=5)
        self.wait(0.1)
        self.pause()

        self.play(p.animate.set_value(7),run_time=5)
        self.wait(0.1)
        self.pause()

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        self.wait()