from manim import *
from manim_presentation import Slide

class tangente(ThreeDScene,Slide):
    def construct(self):        
        WM = MathTex('KallelFiori').scale(0.5)
        WM.set_opacity(0.4)
        WM.move_to([6,-3.5,0])

        self.add_fixed_in_frame_mobjects(WM) 
        self.add(WM)

        h = ValueTracker(1)
        sheet_value = 10

        self.set_camera_orientation(zoom=0.6)

        outer_sheet = Square(side_length=sheet_value,color=BLUE)
        outer_sheet.set_fill(color=BLUE,opacity=0.5)
        
        inner_sheet = always_redraw(        
            lambda: Square(side_length=sheet_value-2*h.get_value(),color=GREEN)
            .set_fill(color=GREEN,opacity=0.5)
            .move_to(outer_sheet.get_center())
        )

        self.play(Write(outer_sheet),Write(inner_sheet))
        self.wait(0.1)
        self.pause()

        self.play(h.animate.set_value(3),run_time=2)
        self.wait(0.1)
        self.pause()

        self.play(h.animate.set_value(1),run_time=2)
        self.wait(0.1)
        self.pause()

        
        
        box = always_redraw(
            lambda: Prism(dimensions=[(sheet_value-(2*h.get_value())), 
                                      (sheet_value-(2*h.get_value())), 
                                      h.get_value()])
                                      .rotate(PI / 2)
        )

        self.play(Write(box),FadeOut(outer_sheet),FadeOut(inner_sheet))
        self.move_camera(phi=60 * DEGREES, theta=150 * DEGREES,zoom=1)
        self.wait(0.1)
        self.pause()

        self.play(h.animate.set_value(3),run_time=2)
        self.wait(0.1)
        self.pause()








