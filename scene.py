# @Author: two_0
# @Date:   05-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 05-09-2020
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
        for c in range(10):
            circle = Circle()
            circle.set_fill(PINK, opacity=0.5)

            square = Square()
            square.flip(RIGHT)
            square.rotate(-3 * TAU / 8)

            self.play(ShowCreation(square))
            self.play(Transform(square, circle))
            self.play(FadeOut(square))
