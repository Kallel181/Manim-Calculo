from manim import *
from manim_presentation import Slide

class caixa(ThreeDScene,Slide):
    def construct(self):        
        WAIT_TIME = 1
        
        WM = MathTex('KallelFiori').scale(0.5)
        WM.set_opacity(0.4)
        WM.move_to([6,-3.5,0])

        self.add_fixed_in_frame_mobjects(WM) 
        self.add(WM)  

        h = ValueTracker(1)
        sheet_value = 10

        self.set_camera_orientation(theta=270 * DEGREES,zoom=0.5)
        
        outer_sheet_full = Square(side_length=sheet_value,color=BLUE)
        outer_sheet_full.set_fill(color=BLUE,opacity=0.5)
        outer_sheet_full.move_to(ORIGIN)

        self.play(Write(outer_sheet_full))
        self.wait(WAIT_TIME)
        self.pause()  

        side_label = MathTex('10').scale(2).next_to(outer_sheet_full,DOWN)

        self.play(Write(side_label))
        self.wait(WAIT_TIME)
        self.pause()

        self.play(FadeOut(side_label))
        self.wait(WAIT_TIME)
        self.pause()
        
        outer_sheet1_fixed = always_redraw(
            lambda: Rectangle(height=sheet_value,width=sheet_value-2*h.get_value(),color=BLUE)
            .set_fill(color=BLUE,opacity=0.5)
            .move_to(outer_sheet_full.get_center())
        )


        outer_sheet2_fixed = always_redraw(
            lambda: Rectangle(height=sheet_value-2*h.get_value(),width=sheet_value,color=BLUE)
            .set_fill(color=BLUE,opacity=0.5)
            .move_to(outer_sheet_full.get_center())
        )


        outer_sheet_union = always_redraw(
            lambda: Union(outer_sheet1_fixed,outer_sheet2_fixed)
            .move_to(outer_sheet_full.get_center())
        ) 

        removed_squares = always_redraw(
            lambda: Difference(outer_sheet_full,outer_sheet_union,color=RED)
            .move_to(ORIGIN)
            .set_fill(color=RED,opacity=0.5)
        )        
        
        inner_sheet_fixed = always_redraw(        
            lambda: Square(side_length=sheet_value-2*h.get_value(),color=GREEN)
            .set_fill(color=GREEN,opacity=0.5)
            .move_to(outer_sheet_full.get_center())
        )

        h_label1_fixed = always_redraw(
            lambda: MathTex('h')
            .move_to([(sheet_value-2*h.get_value())/2 + (h.get_value()/2),0,0])
        )

        h_label2_fixed = always_redraw(
            lambda: MathTex('h')
            .move_to([0,(sheet_value-2*h.get_value())/2 + (h.get_value()/2),0])
        )
        
        line_y_fixed = always_redraw(
            lambda: Line(start=ORIGIN,end=[h.get_value(),0,0])
            .next_to(h_label1_fixed,DOWN)
        )

        line_x_fixed = always_redraw(
            lambda: Line(start=ORIGIN,end=[0,h.get_value(),0])
            .next_to(h_label2_fixed,LEFT)
        )

        h_value_label = always_redraw(
            lambda: MathTex('h=',str(h.get_value())[:3])
            .shift(UP*3)
            .shift(LEFT*4)
        )
        self.add_fixed_in_frame_mobjects(h_value_label) 

        self.play(Write(removed_squares),
                  FadeOut(outer_sheet_full),
                  FadeIn(outer_sheet1_fixed),
                  FadeIn(outer_sheet2_fixed),
                  Write(inner_sheet_fixed),
                  Write(h_label1_fixed),
                  Write(line_x_fixed),
                  Write(h_label2_fixed),
                  Write(line_y_fixed),
                  Write(h_value_label))
        self.wait(WAIT_TIME)
        self.pause()

        self.play(FadeOut(removed_squares))
        self.play(h.animate.set_value(3),run_time=2)
        self.wait(WAIT_TIME)
        self.pause()

        self.play(h.animate.set_value(1),run_time=2)
        self.wait(WAIT_TIME)
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

        inner_sheet = always_redraw(        
            lambda: Square(side_length=sheet_value-2*h.get_value(),color=GREEN)
            .set_fill(color=GREEN,opacity=0.5)
            .move_to(outer_sheet1.get_center())
        )

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

        self.play(FadeOut(h_label1_fixed),FadeOut(line_x_fixed),FadeOut(h_label2_fixed),FadeOut(line_y_fixed))
        
        outer_sheet_full.move_to(inner_sheet.get_center())
        self.play(outer_sheet1_fixed.animate.move_to(inner_sheet.get_center()),
                  outer_sheet2_fixed.animate.move_to(inner_sheet.get_center()),
                  inner_sheet_fixed.animate.move_to(inner_sheet.get_center()))
        
        self.play(Write(outer_sheet1),
                  Write(outer_sheet2),
                  FadeOut(outer_sheet1_fixed),
                  FadeOut(outer_sheet2_fixed),
                  FadeOut(inner_sheet_fixed),
                  Write(h_label1),
                  Write(h_label2),
                  Write(line_y),
                  Write(line_x),
                  Write(inner_sheet))
        self.wait(WAIT_TIME)
        self.pause()
        
        box = always_redraw(
            lambda: Prism(dimensions=[(sheet_value-(2*h.get_value())), 
                                      (sheet_value-(2*h.get_value())), 
                                      h.get_value()])
                                      .rotate(PI / 2)
        )

        self.play(Write(box))
        self.move_camera(phi=70 * DEGREES, theta=315 * DEGREES,zoom=0.8)
        self.wait(WAIT_TIME)
        self.pause()

        self.play(h.animate.set_value(3),run_time=2)
        self.wait(WAIT_TIME)
        self.pause()

        self.play(h.animate.set_value(2),run_time=2)
        self.wait(WAIT_TIME)
        self.pause()

        h_label_high = always_redraw(
            lambda: MathTex('h')
            .move_to([(sheet_value-(2*h.get_value()))/2,0.5,0])
            .rotate(90 * DEGREES,[1,0,0])
            .rotate(90 * DEGREES,[0,0,1])
        )
        line_high = always_redraw(
            lambda: Line(start=[0,0,h.get_value()/2],end=[0,0,-h.get_value()/2])
            .move_to([(sheet_value-(2*h.get_value()))/2,0,0])
        )

        self.play(Write(h_label_high),Write(line_high))
        self.wait(WAIT_TIME)
        self.pause()
        
        side1_label = always_redraw(
            lambda: MathTex('10-2h')
            .move_to([0,(-(sheet_value-(2*h.get_value()))/2) - 0.5,-h.get_value()/2])
        )

        side2_label = always_redraw(
            lambda: MathTex('10-2h')
            .move_to([((sheet_value-(2*h.get_value()))/2) + 0.5,0,-h.get_value()/2])
            .rotate(angle=90 * DEGREES, axis=[0,0,1])
        )

        self.play(FadeOut(outer_sheet1),
                  FadeOut(outer_sheet2),
                  FadeOut(inner_sheet),
                  FadeOut(h_label1),
                  FadeOut(h_label2),
                  FadeOut(line_y),
                  FadeOut(line_x))
        self.play(Write(side1_label),Write(side2_label))
        self.wait(WAIT_TIME)
        self.pause()

        #=============== Part 2 ===============
        volume_func = MathTex('V(h)=h(10-2h)^2')
        self.add_fixed_in_frame_mobjects(volume_func) 
        volume_func.shift(UP*3)

        self.play(Write(volume_func))
        self.wait(WAIT_TIME)
        self.pause()

        axes = (
            Axes(
                x_range = [0,5,1],
                x_length = 5,
                y_range = [0,75,5],
                y_length = 6,
                x_axis_config = {"include_numbers": True, "include_tip":False},
                y_axis_config={
                "numbers_to_include": np.arange(0, 75.1, 5),
                "include_tip":False},
            )
            .set_color(WHITE)
        )
        
        def vol(x):
            return x * (10-2*x)**2
        
        graph = axes.plot(
            vol, x_range=[0,5], color=BLUE
        )   

        self.move_camera(theta=300 * DEGREES,zoom=0.4,frame_center=[0,6,-1])
        self.add_fixed_in_frame_mobjects(axes) 
        axes.scale(0.9)
        axes.shift(RIGHT*4)
        self.add_fixed_in_frame_mobjects(graph) 
        graph.scale(0.9)
        graph.shift(RIGHT*4)


        self.play(Write(axes),Write(graph),h.animate.set_value(1),run_time=1)
        volume_func_target = volume_func.generate_target()
        volume_func_target.scale(0.8)
        volume_func_target.shift(UP*0.3)

        self.play(MoveToTarget(volume_func))
        self.wait(WAIT_TIME)
        self.pause()

        line_vertical = always_redraw(
            lambda: Line(start = axes.c2p(h.get_value(),0),
                         end = axes.c2p(h.get_value(),vol(h.get_value())),
                         color = YELLOW
                        )
        )
        line_horizontal = always_redraw(
            lambda: Line(start = axes.c2p(h.get_value(),vol(h.get_value())),
                         end = axes.c2p(0,vol(h.get_value())),
                         color = YELLOW
                        )
        )
        self.add_fixed_in_frame_mobjects(line_vertical)
        self.add_fixed_in_frame_mobjects(line_horizontal)

        dot = always_redraw(
            lambda: Dot(point=axes.c2p(h.get_value(),vol(h.get_value())),color=YELLOW)
        )
        self.add_fixed_in_frame_mobjects(dot)

        volume_label = always_redraw(
            lambda: MathTex('V(h)=',str(vol(h.get_value()))[:4])
            .next_to(h_value_label,DOWN)
        )
        self.add_fixed_in_frame_mobjects(volume_label) 

        self.play(Write(line_vertical),Write(line_horizontal),Write(dot),Write(volume_label))
        self.wait(WAIT_TIME)
        self.pause()        

        self.play(h.animate.set_value(4.5),run_time=5)
        self.wait(WAIT_TIME)
        self.pause()

        self.play(h.animate.set_value(1),run_time=5)
        self.wait(WAIT_TIME)
        self.pause()   

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait()
