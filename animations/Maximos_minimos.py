from manim import *
from manim_presentation import Slide

class maximos_minimos(Slide):
    def construct(self):  
        WM = MathTex('KallelFiori').scale(0.5)
        WM.set_opacity(0.4)
        WM.move_to([6,-3.5,0])
        self.add(WM)

        #Objeto Manim que armazena o texto Latex do "enunciado" do problema que vamos analisar
        example1 = MathTex("Estude f com relação a máximos e mínimos",tex_environment="flushleft")
        example1.scale(0.8)
        example1.shift(UP*3.5 + LEFT*3)
        
        #Objeto Manim que armazena o texto Latex da função as ser desenhada
        function_tex = MathTex(r'f(x)=x^3-3x^2+3')

        #Objeto Manim que armazena os eixos cartesianos
        #Com alterações na função a ser mostrada é importante mudar o valores do graficos para que
        #a função seja melhor desenhada.
        axes1 = (
            Axes(
                x_range = [-1,3,1],
                x_length = 5,
                y_range = [-1,4,1],
                y_length = 5,
                axis_config = {"include_numbers": True, 
                               "include_tip":False}
            )
            .set_color(WHITE)
        )
        axes1.z_index = 1 #Movendo os eixos para uma camada mais acima

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
        graph1_group = VGroup(tangent,graph1,axes1,axes1_labels,dot1)
        graph1_group.scale(0.8)

        self.play(Write(VGroup(example1)))
        self.wait(0.1)
        self.pause()        
        
        self.play(Write(function_tex))
        self.wait(0.1)
        self.pause()

        function_tex_target = function_tex.generate_target()
        function_tex_target.shift(UP*2)
        self.play(MoveToTarget(function_tex))
        self.wait(0.1)
        self.pause()

        #Alinhamentos precisa ser definido apos a modunça de posição do objeto function_tex
        graph1_group.next_to(function_tex,DOWN)
        self.play(Write(VGroup(axes1,graph1,axes1_labels)))
        self.wait(0.1)
        self.pause()

        #Movendo os elementos mais a esquerda para abrir espaço a direita
        left_elements = VGroup(graph1_group,function_tex)
        left_elements_target = left_elements.generate_target()
        left_elements_target.scale(1.1)
        left_elements_target.shift(LEFT*3)
        self.play(MoveToTarget(left_elements))
        self.wait(0.1)
        self.pause()

        derivative_tex = MathTex('f\'(x)= 3x^2 - 6x')
        derivative_tex.shift(RIGHT*3.5)       
        derivative_tex.shift(UP*(function_tex.get_center()[1])) #alinhamento com a função anterior
        self.play(Write(derivative_tex))
        self.wait(0.1)
        self.pause()

        solution_tex1 = MathTex('f\'(x)=0').scale(0.7)
        solution_tex2 = MathTex('x = 0').scale(0.7)
        solution_tex3 = MathTex('ou').scale(0.7)
        solution_tex4 = MathTex('x = 2').scale(0.7)
        
        solution_tex3.next_to(solution_tex2,DOWN)
        solution_tex4.next_to(solution_tex3,DOWN)
        
        solution_tex_x_values = VGroup(solution_tex2,solution_tex3,solution_tex4)
        solution_tex_x_values.next_to(solution_tex1,RIGHT)

        solution_tex = VGroup(solution_tex_x_values,solution_tex1)        
        
        solution_tex.next_to(derivative_tex,DOWN)
        self.play(Write(solution_tex))     
        self.wait(0.1)
        self.pause()

        #Objeto Manim que armazena uma linha de numeros, funcionando como o objeto Axes(), mas mostrando
        #apenas um eixo.
        derivative_number_line = NumberLine(
            x_range =[-0.9,2.9,2],
            length = 4,
            color = WHITE,
            numbers_to_include = {0,2},
            label_direction=UP
        )
        derivative_number_line.next_to(solution_tex,DOWN,buff=1.0)
        derivative_number_line_label = MathTex("f\'").scale(0.6).next_to(derivative_number_line,LEFT)
        
        #Função python que retorna os falores da função derivada
        def derivative(x):
            return (3*(x**2) - 6*x)        
        
        #Objeto Manim que muda de acordo com o valor da derivada da f.
        #O objeto precisa estar dentro da função always_redraw uma vez que o valor de x vai ser
        #alterado posteriomente.        
        derivative_text = always_redraw(
            lambda: Tex('f\'(x)='+str(derivative(x.get_value()))[:4])
            .scale(0.6)
            .next_to(derivative_number_line,UP)
            .shift(LEFT*2)
        ) 
        
        #Objeto Manim que muda de acordo com o valor de x.
        #O objeto precisa estar dentro da função always_redraw uma vez que o valor de x vai ser
        #alterado posteriomente.  
        x_text = always_redraw(
            lambda: Tex(r'x='+str(x.get_value())[:4])
            .scale(0.6)
            .next_to(derivative_text,UP)
        )

        dot2 = always_redraw(
            #n2p é semelhante a função c2p do objeto Axes(
            lambda: Dot(derivative_number_line.n2p(x.get_value()))
        )

        function_number_line = NumberLine(
            x_range =[-0.9,2.9,2],
            length = 4,
            color = WHITE,
            numbers_to_include = {0,2},
            label_direction=UP
        )
        function_number_line.next_to(derivative_number_line,DOWN,buff=1.0)
        function_number_line_label = MathTex("f").scale(0.6).next_to(function_number_line,LEFT)


        self.play(Write(VGroup(derivative_number_line,
                               x_text,
                               dot2,
                               derivative_text,
                               derivative_number_line_label,
                               function_number_line,
                               function_number_line_label)))
        self.wait(0.1)
        self.pause()

        #Nos blocos abaixo fazemos as variações de x indo de -0.5 até 2.5, fazendo pequenas pausas
        #para mostrar os valores da derivada, assim, obtendo as informações para classificarmos
        #os pontos em minimos e maximos locais.
        
        #valor 0
        self.play(x.animate.set_value(0),run_time=2)
        self.wait(0.1)
        self.pause()

        plus1 = MathTex("+").move_to(derivative_number_line.n2p(-0.5))
        plus1.shift(UP*0.3)
        self.play(Write(plus1))
        self.wait(0.1)
        self.pause()

        up_arrow1 = Vector(UR*0.3).scale(0.8)
        up_arrow1.move_to(function_number_line.n2p(-0.5))
        up_arrow1.shift(UP*0.3)
        self.play(Write(up_arrow1))
        self.wait(0.1)
        self.pause()

        #valor 2
        
        self.play(x.animate.set_value(2),run_time=2)
        self.wait(0.1)
        self.pause()

        minus = MathTex("-").move_to(derivative_number_line.n2p(1))
        minus.shift(UP*0.3)
        self.play(Write(minus))
        self.wait(0.1)
        self.pause()

        down_arrow1 = Vector(DR*0.3).scale(0.8).move_to(function_number_line.n2p(1))
        down_arrow1.shift(UP*0.3)
        self.play(Write(down_arrow1))
        self.wait(0.1)
        self.pause()

        #valor 2.5

        self.play(x.animate.set_value(2.5),run_time=2)
        self.wait(0.1)
        self.pause()

        plus2 = MathTex("+").move_to(derivative_number_line.n2p(2.5))
        plus2.shift(UP*0.3) 
        self.play(Write(plus2))
        self.wait(0.1)
        self.pause()

        up_arrow2 = Vector(UR*0.3).scale(0.8).move_to(function_number_line.n2p(2.5))
        up_arrow2.shift(UP*0.3)
        self.play(Write(up_arrow2))
        self.wait(0.1)
        self.pause()

        #Agrupamento dos elementos a direita
        function_number_line_elements = VGroup(plus1,
                                               plus2,
                                               minus,
                                               function_number_line,
                                               function_number_line_label)
        derivative_number_line_elements = VGroup(up_arrow1,
                                                 up_arrow2,
                                                 down_arrow1,
                                                 derivative_number_line_label,
                                                 derivative_number_line,
                                                 dot2)
        
        right_elements = VGroup(derivative_tex,
                                derivative_text,
                                solution_tex,
                                x_text,
                                function_number_line_elements,
                                derivative_number_line_elements)
        right_elements_target = right_elements.generate_target()

        right_elements_target.shift(UP)
        self.play(MoveToTarget(right_elements))       
        
        res1 = MathTex("x=0 Máximo Local",tex_environment="flushleft").scale(0.8)
        res1.next_to(right_elements,DOWN)
        res2 = MathTex("x=2 Mínimo Local",tex_environment="flushleft").scale(0.8)
        res2.next_to(res1,DOWN)

        self.play(Write(VGroup(res1,res2)))
        self.wait(0.1)
        self.pause()

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait()