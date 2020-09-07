# @Author: two_0
# @Date:   05-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 06-09-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
#     ___ __ ._`.*.'_._ ____ רףאל
#    . +  * .\   o.* `.`. +.  א .
#   *  .ת' '  \^/|  `. * .  * `
#             \V/ . +
#    יהוה      /_\  .`.
#   ======== _/W\_ =אדני:By: Two.0:.*
from manim import *
class SquareToCircle(Scene):
    def construct(self):
        for i in range(2):
            circle = Circle()
            square = Square()
            square.flip(RIGHT)
            square.rotate(-3 * TAU / 8)
            circle.set_fill(PINK, opacity=0.5)
            self.wait()

            self.play(ShowCreation(square))
            self.play(Transform(square, circle))
            self.play(FadeOut(square))

class displayText(Scene):
    def construct(self):
        # Create TextMobjects
        first_line = TextMobject('Create cool animations')
        second_line = TextMobject('using Manim')
        third_line = TextMobject('Try it out yourself.', color=RED)

        # Position second line underneath first line
        second_line.next_to(first_line, DOWN)

        # Displaying text
        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(ReplacementTransform(first_line, third_line), FadeOut(second_line))
        self.wait(2)


class displayEquations(Scene):
    def construct(self):
        # Create TextMobjects
        first_line = TextMobject('Manim also allows you')
        second_line = TextMobject('to show beautiful math equations')
        equation = TextMobject('$d\\left(p, q\\right)=d\\left(q, p\\right)=\\sqrt{(q_1-p_1)^2+(q_2-p_2)^2+...+(q_n-p_n)^2}=\\sqrt{\\sum_{i=1}^n\\left(q_i-p_i\\right)^2}$')

        # Position second line underneath first line
        second_line.next_to(first_line, DOWN)

        # Displaying text and equation
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(ReplacementTransform(first_line, equation), FadeOut(second_line))
        self.wait(3)

class Shapes(Scene):
    def construct(self):
        ######Code######
        #Making shapes
        circle = Circle()
        square = Square()
        triangle=Polygon(np.array([1,0,0]),np.array([0,1,0]),np.array([0,0,1]))

        #Showing shapes
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))
        self.wait(5)

class Helloworld(Scene):
    def construct(self):
        text = TextMobject('Hello World!')
        self.play(Write(text))
        self.wait(3)

class CreateGraph(GraphScene):
    CONFIG = {
        'x_min': -3,
        'x_max': 3,
        'y_min': -5,
        'y_max': 5,
        'graph_origin': ORIGIN,
        'axes_color': BLUE
    }

    def construct(self):
        # Create Graph
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x: x**2, WHITE)
        graph_label = self.get_graph_label(graph, label='x^{2}')

        graph2 = self.get_graph(lambda x: x**3, WHITE)
        graph_label2 = self.get_graph_label(graph2, label='x^{3}')

        # Display graph
        self.play(ShowCreation(graph), Write(graph_label))
        self.wait(1)
        self.play(Transform(graph, graph2), Transform(graph_label, graph_label2))
        self.wait(1)
