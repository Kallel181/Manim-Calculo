from manim import *
from manim_presentation import Slide

class tangente(ThreeDScene,Slide):
    def construct(self):        
        WM = MathTex('KallelFiori').scale(0.5)
        WM.set_opacity(0.4)
        WM.move_to([6,-3.5,0])

        self.add_fixed_in_frame_mobjects(WM) 
        self.add(WM)

        #RM - Test
        axes1 = ThreeDAxes()
        labels1 = axes1.get_axis_labels(
            Text("x-axis").scale(0.7), Text("y-axis").scale(0.7), Text("")
        )
        self.add(axes1, labels1)
        #RM - Test    
    
        h = ValueTracker(1)
        sheet_value = 10

        self.set_camera_orientation(theta=270 * DEGREES,zoom=0.5)
        
        outer_sheet_full = always_redraw(
            lambda: Square(side_length=sheet_value,color=BLUE)
            .shift(np.array([0,0,-1])*(h.get_value()/2))
            .set_fill(color=BLUE,opacity=0.5)
        )

        self.play(Write(outer_sheet_full))
        self.wait(0.1)
        self.pause()  

        side_label = always_redraw(
            lambda: MathTable('10')
            .next_to(outer_sheet_full,DOWN)
        )

        self.play(Write(side_label))
        self.wait(0.1)
        self.pause()
        
        outer_sheet1 = always_redraw (
            lambda: Rectangle(height=sheet_value,width=sheet_value-2*h.get_value(),color=BLUE)
            .set_fill(color=BLUE,opacity=0.5)
            .move_to(ORIGIN)
            .shift(np.array([0,0,-1])*(h.get_value()/2))
        )

        outer_sheet2 = always_redraw (
            lambda: Rectangle(height=sheet_value-2*h.get_value(),width=sheet_value,color=BLUE)
            .set_fill(color=BLUE,opacity=0.5)
            .move_to(ORIGIN)
            .shift(np.array([0,0,-1])*(h.get_value()/2))
        )

        outer_sheet_union = always_redraw(
            lambda: Union(outer_sheet1,outer_sheet2)
            .move_to(outer_sheet_full.get_center())

        )   
        removed_squares = always_redraw(
            lambda: Difference(outer_sheet_full,outer_sheet_union,color=RED)
            .move_to(outer_sheet_full.get_center())
            .set_fill(color=RED,opacity=0.5)
        )        
        
        inner_sheet = always_redraw(        
            lambda: Square(side_length=sheet_value-2*h.get_value(),color=GREEN)
            .set_fill(color=GREEN,opacity=0.5)
            .move_to(outer_sheet1.get_center())
        )

        self.play(Write(inner_sheet))
        self.wait(0.1)
        self.pause()

        self.play(Write(removed_squares))
        self.wait(0.1)
        self.pause()

        h_label1 = always_redraw(
            lambda: MathTex('h')
            .move_to([(sheet_value-2*h.get_value())/2 + (h.get_value()/2),0,0])
            .shift(np.array([0,0,-1])*(h.get_value()/2))
        )

        h_label2 = always_redraw(
            lambda: MathTex('h')
            .move_to([0,(sheet_value-2*h.get_value())/2 + (h.get_value()/2),0])
            .shift(np.array([0,0,-1])*(h.get_value()/2))
        )
        
        line_y = always_redraw(
            lambda: Line(start=ORIGIN,end=[h.get_value(),0,0])
            .next_to(h_label1,DOWN)
        )

        line_x = always_redraw(
            lambda: Line(start=ORIGIN,end=[0,h.get_value(),0])
            .next_to(h_label2,LEFT)
        )

        h_value_label = always_redraw(
            lambda: MathTex('h=',str(h.get_value())[:3])
            .shift(UP*3)
            .shift(LEFT*4)
        )
        self.add_fixed_in_frame_mobjects(h_value_label) 

        self.play(Write(h_label1),Write(line_x),Write(h_label2),Write(line_y),Write(h_value_label))
        self.wait(0.1)
        self.pause()


        self.play(h.animate.set_value(3),run_time=2)
        self.wait(0.1)
        self.pause()

        #DBG
        self.move_camera(phi=70 * DEGREES, theta=315 * DEGREES,zoom=0.8)
        self.wait(0.1)
        self.pause()

        self.play(h.animate.set_value(1),run_time=2)
        self.wait(0.1)
        self.pause()

        self.play(Write(outer_sheet1),Write(outer_sheet2),FadeOut(outer_sheet_full),FadeOut(removed_squares))
        self.wait(0.1)
        self.pause()

        
        box = always_redraw(
            lambda: Prism(dimensions=[(sheet_value-(2*h.get_value())), 
                                      (sheet_value-(2*h.get_value())), 
                                      h.get_value()])
                                      .rotate(PI / 2)
        )

        self.play(Write(box))
        self.move_camera(phi=70 * DEGREES, theta=315 * DEGREES,zoom=0.8)
        self.wait(0.1)
        self.pause()

        self.play(h.animate.set_value(3),run_time=2)
        self.wait(0.1)
        self.pause()

        self.play(h.animate.set_value(1),run_time=2)
        self.wait(0.1)
        self.pause()








