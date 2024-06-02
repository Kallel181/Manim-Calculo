from manim import *

class caixa(ThreeDScene):
    def construct(self):   
        self.camera.background_color = WHITE

        h = ValueTracker(1)
        sheet_value = 10

        self.set_camera_orientation(theta=270 * DEGREES,zoom=0.5)
        
        outer_sheet_full = Square(side_length=sheet_value,color=BLUE_E).set_fill(color=BLUE,opacity=0.5).move_to(ORIGIN)
        side_label = MathTex('10',color=BLACK).scale(2).next_to(outer_sheet_full,DOWN)

        self.add(side_label)
       
        outer_sheet1_fixed = always_redraw(
            lambda: Rectangle(height=sheet_value,width=sheet_value-2*h.get_value(),color=BLUE_E)
            .set_fill(color=BLUE_E,opacity=0.5)
            .move_to(outer_sheet_full.get_center())
        )


        outer_sheet2_fixed = always_redraw(
            lambda: Rectangle(height=sheet_value-2*h.get_value(),width=sheet_value,color=BLUE_E)
            .set_fill(color=BLUE_E,opacity=0.5)
            .move_to(outer_sheet_full.get_center())
        )


        outer_sheet_union = always_redraw(
            lambda: Union(outer_sheet1_fixed,outer_sheet2_fixed)
            .move_to(outer_sheet_full.get_center())

        )   
        removed_squares = always_redraw(
            lambda: Difference(outer_sheet_full,outer_sheet_union,color=RED_E)
            .move_to(ORIGIN)
            .set_fill(color=RED_E,opacity=0.5)
        )        
        
        inner_sheet_fixed = always_redraw(        
            lambda: Square(side_length=sheet_value-2*h.get_value(),color=GREEN_E)
            .set_fill(color=GREEN_E,opacity=0.5)
            .move_to(outer_sheet_full.get_center())
        )

        h_label1_fixed = always_redraw(
            lambda: MathTex('h',color=BLACK)
            .move_to([(sheet_value-2*h.get_value())/2 + (h.get_value()/2),0,0])
        )

        h_label2_fixed = always_redraw(
            lambda: MathTex('h',color=BLACK)
            .move_to([0,(sheet_value-2*h.get_value())/2 + (h.get_value()/2),0])
        )
        
        line_y_fixed = always_redraw(
            lambda: Line(start=ORIGIN,end=[h.get_value(),0,0],color=BLACK)
            .next_to(h_label1_fixed,DOWN)
        )

        line_x_fixed = always_redraw(
            lambda: Line(start=ORIGIN,end=[0,h.get_value(),0],color=BLACK)
            .next_to(h_label2_fixed,LEFT)
        )

        self.add(removed_squares,outer_sheet1_fixed,outer_sheet2_fixed,inner_sheet_fixed,h_label1_fixed,line_x_fixed,h_label2_fixed,line_y_fixed)