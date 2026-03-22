from manim import *
import numpy as np

class QuadradoSoma(MovingCameraScene):

    def construct(self):

        ponto1 = np.array([-2, 2, 0])
        ponto2 = np.array([-2, -2, 0])
        ponto3 = np.array([2, -2, 0])
        ponto4 = np.array([2, 2, 0])

        quadrado_maior = Polygon(ponto1, ponto2, ponto3, ponto4, color=WHITE)

        self.play(Create(quadrado_maior))

        self.wait(2)

        ponto5 = np.array([-2, 2, 0])
        ponto6 = np.array([-2, 1, 0])
        ponto7 = np.array([-1, 1, 0])
        ponto8 = np.array([-1, 2, 0])

        quadrado_b = Polygon(ponto5, ponto6, ponto7, ponto8, color=GREEN)
        quadrado_b.set_fill(GREEN, opacity=0.3)

        ponto9 = np.array([-2, -2, 0])
        ponto10 = np.array([-1, -2, 0])

        retangulo1 = Polygon(ponto6, ponto7, ponto10, ponto9, color=PURPLE_C)
        retangulo1.set_fill(PURPLE_C, opacity=0.3)

        ponto11 = np.array([2, 2, 0])
        ponto12 = np.array([2, 1, 0])

        retangulo2 = Polygon(ponto7, ponto8, ponto11, ponto12, color=PURPLE_C)
        retangulo2.set_fill(PURPLE_C, opacity=0.3)

        ponto13 = np.array([2, -2, 0])

        quadrado_a = Polygon(ponto7, ponto10, ponto13, ponto12, color=BLUE_C)
        quadrado_a.set_fill(BLUE_C, opacity=0.3)

        self.play(FadeIn(quadrado_b), FadeIn(retangulo1), FadeIn(retangulo2), FadeIn(quadrado_a))

        self.wait(2)

        label_b1 = MathTex(r'b').shift(2.3*LEFT + 1.5*UP)

        label_b2 = MathTex(r'b').shift(2.4*UP + 1.5*LEFT)

        label_b1copia = MathTex(r'b').shift(2.3*LEFT + 1.5*UP)

        label_b2copia = MathTex(r'b').shift(2.4*UP + 1.5*LEFT)

        label_a1 = MathTex(r'a').shift(0.5*RIGHT + 2.4*UP)

        label_a1copia = MathTex(r'a').shift(0.5*RIGHT + 2.4*UP)

        label_b3 = MathTex(r'b').shift(2.3*RIGHT + 1.5*UP)

        label_b3copia = MathTex(r'b').shift(2.3*RIGHT + 1.5*UP)

        label_a2 = MathTex(r'a').shift(2.3*RIGHT + 0.5*DOWN)

        label_a2copia = MathTex(r'a').shift(2.3*RIGHT + 0.5*DOWN)

        label_a3 = MathTex(r'a').shift(2.4*DOWN + 0.5*RIGHT)
        label_a3copia = MathTex(r'a').shift(2.4*DOWN + 0.5*RIGHT)

        label_b4 = MathTex(r'b').shift(2.4*DOWN + 1.5*LEFT)
        label_b4copia = MathTex(r'b').shift(2.4*DOWN + 1.5*LEFT)

        label_a4 = MathTex(r'a').shift(2.3*LEFT + 0.5*DOWN)
        label_a4copia = MathTex(r'a').shift(2.3*LEFT + 0.5*DOWN)

        self.play(FadeIn(label_b1), FadeIn(label_b2), FadeIn(label_b1copia),
         FadeIn(label_b2copia), FadeIn(label_a1),
         FadeIn(label_a1copia), FadeIn(label_b3),
         FadeIn(label_b3copia), FadeIn(label_a2),
         FadeIn(label_a2copia), FadeIn(label_a3),
         FadeIn(label_a3copia), FadeIn(label_b4),
         FadeIn(label_b4copia), FadeIn(label_a4),
         FadeIn(label_a4copia))

        self.wait(2)
