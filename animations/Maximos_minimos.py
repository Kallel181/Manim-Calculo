from manim import *
from manim_presentation import Slide

class maximos_minimos(Slide):
    def construct(self):  
        WM = MathTex('KallelFiori').scale(0.5)
        WM.set_opacity(0.4)
        WM.move_to([6,-3.5,0])
        self.add(WM)

        #Objeto Manim que armazena o texto Latex da função as ser desenhada
        function_tex = MathTex(r'f(x)=x^3-12x^2+45x-48')

        #Objeto Manim que armazena os eixos cartesianos
        #Com alterações na função a ser mostrada é importante mudar o valores do graficos para que
        #a função seja melhor desenhada.
        axes1 = (
            Axes(
                x_range = [-1,3,1],
                x_length = 5,
                y_range = [-1,3,1],
                y_length = 5,
                axis_config = {"include_numbers": True, "include_tip":False},
            )
            .set_color(WHITE)
        )

        #Adicionando texto para indicar os eixos
        axes1_labels = axes1.get_axis_labels(x_label="x",y_label="y")
        
        #Função para desenharmos o grafico
        def f(x):
            return (x**3 - (3*(x**2)) + 3)

        #Objeto Manim que armazena o grafico da função previamente definida por f
        graph1 = axes1.plot(
            f, x_range=[-1,3], color=BLUE
        )

        #Value Tracker armazena o valor de x, e pode ser usado para animar a reta tangente 
        #posteriormente.
        #Os valores iniciais podem ser alterados conforme necessidade.
        x = ValueTracker(-0.5)
        
        #dx nesse exemplo não precisa ser um ValueTracker, uma vez que só estamos 
        #interessados na animação da reta tangente.
        dx = 0.001 

        #Objeto Manim que armazena a reta secante ao grafico conforme x e dx.
        #O objeto precisa estar dentro da função always_redraw uma vez que o valor de x vai ser
        #alterado posteriomente.
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

        #VGroup é usado para agrupar elementos em um unico lugar, assim modificações posteriores podem ser
        #feitas diretamente no grupo ao invez de elemento a elemento.
        left_elements = VGroup(tangent,graph1,axes1,axes1_labels,function_tex)



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

        




        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait()