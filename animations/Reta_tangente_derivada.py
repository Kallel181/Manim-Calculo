from manim import *
from manim_slides import Slide

class tangente(Slide):
    def construct(self):
        #Definindo configurações do eixos
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
        
        axes_labels = axes.get_axis_labels(x_label="x",y_label="y")
        
        def f(x):
            return 0.1 * (x - 2) * (x - 5) * (x - 7) + 7

        graph = axes.plot(
            f, x_range=[0,10], color=BLUE
        )

        x = ValueTracker(7)
        dx = ValueTracker(2)

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

        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(x.get_value(), f(x.get_value())))
        )
        
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(
                x.get_value() + dx.get_value(),
                f(x.get_value() + dx.get_value())
            ))
        )

        self.add(axes,axes_labels,graph)
        self.wait(0.1)
        self.next_slide() 

        self.play(Create(VGroup(dot1,dot2,secant)))
        self.next_slide()

        self.play(dx.animate.set_value(0.001),run_time=8)
        self.next_slide()

        self.play(x.animate.set_value(1),run_time=5)
        self.next_slide()

        self.play(x.animate.set_value(7),run_time=5)
        self.next_slide()

        self.play(x.animate.set_value(2),run_time=5)
        self.next_slide()