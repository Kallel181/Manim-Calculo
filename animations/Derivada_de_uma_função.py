from manim import *
from manim_presentation import Slide

class derivada(Slide):
    def construct(self):
        WM = MathTex('KallelFiori').scale(0.5)
        WM.set_opacity(0.4)
        WM.move_to([6,-3.5,0])
        self.add(WM)

        #Texto Latex para a funçã oque vamos derivaar usando limite
        function_tex = MathTex('f(x)=x^2')
        function_tex_target = function_tex.generate_target()
        function_tex_target.shift(UP*3.5)

        #Definição de derivada por limite apresentada no Guidorizzi
        derivative_definition = MathTex('f\'(p)=','\\lim_{x\\rightarrow p}\\frac{f(x)-f(p)}{x-p}')
        derivative_definition.shift(UP*2.5)

        #Valor da função para encontrarmos a derivada
        p = MathTex('p=','1').scale(0.8).shift(LEFT*3+UP*3.5)

        #Substituiçã de p pelo valor 1
        derivative_definition_calc1 = MathTex('f\'(1)=','\\lim_{x\\rightarrow 1}\\frac{f(x)-f(1)}{x-1}')
        derivative_definition_calc1.move_to(derivative_definition.get_center())
        #posicionamos a derivada para a mesma possição da definição para substituirmos posteriormente

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

        #O objeto abaixo armazena todos os passos para o desenvolvimento da conta
        steps = MathTex('&= \\lim_{x\\rightarrow 1}\\frac{x^2-1}{x-1}\\\\',
                        '&= \\lim_{x\\rightarrow 1}\\frac{x^2-1^2}{x-1}\\\\',
                        '&= \\lim_{x\\rightarrow 1}\\frac{\\left(x-1\\right)\\left(x+1\\right)}{x-1}\\\\',
                        '&= \\lim_{x\\rightarrow 1}\\ \\left(x+1\\right)\\\\',
                        '&= 2\\\\')

        steps.next_to(derivative_definition_calc1,DOWN)
        steps.shift(RIGHT)

        #A estrutura de loop abaixo intera sobre todos os elementos da variavel step
        #apresentando uma a uma na tela e fazando uma pausa entre elas.
        for line in range(0,len(steps)):
            self.play(Write(steps[line]))
            self.wait(0.1)
            self.pause()
        #A função len(steps) nos retorna a quantidade de elementos dentro do objeto
        #steps, nesse casos, a quantidade de linhas as serem escritas na tela.
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait()



