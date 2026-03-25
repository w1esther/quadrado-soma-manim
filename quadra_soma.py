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

        label_b1 = MathTex(r'b').shift(2.3*LEFT + 1.5*UP).scale(0.7)
        label_b2 = MathTex(r'b').shift(2.4*UP + 1.5*LEFT).scale(0.7)

        label_b1copia = MathTex(r'b').shift(2.3*LEFT + 1.5*UP).scale(0.7)
        label_b2copia = MathTex(r'b').shift(2.4*UP + 1.5*LEFT).scale(0.7)

        label_a1 = MathTex(r'a').shift(0.5*RIGHT + 2.4*UP).scale(0.7)
        label_a1copia = MathTex(r'a').shift(0.5*RIGHT + 2.4*UP).scale(0.7)

        label_b3 = MathTex(r'b').shift(2.3*RIGHT + 1.5*UP).scale(0.7)
        label_b3copia = MathTex(r'b').shift(2.3*RIGHT + 1.5*UP).scale(0.7)

        label_a2 = MathTex(r'a').shift(2.3*RIGHT + 0.5*DOWN).scale(0.7)
        label_a2copia = MathTex(r'a').shift(2.3*RIGHT + 0.5*DOWN).scale(0.7)

        label_a3 = MathTex(r'a').shift(2.4*DOWN + 0.5*RIGHT).scale(0.7)
        label_a3copia = MathTex(r'a').shift(2.4*DOWN + 0.5*RIGHT).scale(0.7)

        label_b4 = MathTex(r'b').shift(2.4*DOWN + 1.5*LEFT).scale(0.7)
        label_b4copia = MathTex(r'b').shift(2.4*DOWN + 1.5*LEFT).scale(0.7)

        label_a4 = MathTex(r'a').shift(2.3*LEFT + 0.5*DOWN).scale(0.7)
        label_a4copia = MathTex(r'a').shift(2.3*LEFT + 0.5*DOWN).scale(0.7)

        self.play(FadeIn(label_b1), FadeIn(label_b2), FadeIn(label_b1copia),
         FadeIn(label_b2copia), FadeIn(label_a1),
         FadeIn(label_a1copia), FadeIn(label_b3),
         FadeIn(label_b3copia), FadeIn(label_a2),
         FadeIn(label_a2copia), FadeIn(label_a3),
         FadeIn(label_a3copia), FadeIn(label_b4),
         FadeIn(label_b4copia), FadeIn(label_a4),
         FadeIn(label_a4copia))

        self.wait(2)

        multiplicacao_1 = MathTex(r'\cdot').shift(1.5*UP + 1.5*LEFT)

        self.play(label_b1copia.animate.shift(0.6*RIGHT), label_b2copia.animate.shift(0.9*DOWN + 0.2*RIGHT), FadeIn(multiplicacao_1))

        self.wait(2)

        b_quadrado = MathTex(r'b^2').shift(1.5*UP + 1.5*LEFT).scale(0.7)
        
        grupob1 = VGroup()
        grupob1.add(label_b1copia, label_b2copia)

        self.play(Transform(grupob1, b_quadrado), FadeOut(multiplicacao_1))

        self.wait(2)

        multiplicacao_2 = MathTex(r'\cdot').shift(1.5*UP + 0.4*RIGHT)

        self.play(label_a1.animate.shift(0.9*DOWN + 0.4*LEFT), FadeIn(multiplicacao_2), label_b3copia.animate.shift(1.6*LEFT))

        self.wait(2)

        multiplicacao_3 = MathTex(r'\cdot').shift(0.5*DOWN + 1.5*LEFT)

        self.play(label_a4copia.animate.shift(0.55*RIGHT), label_b4copia.animate.shift(1.9*UP + 0.25*RIGHT), FadeIn(multiplicacao_3))

        self.wait(2)

        multiplicacao_4 = MathTex(r'\cdot').shift(0.5*DOWN + 0.5*RIGHT)

        grupo_a = VGroup()
        grupo_a.add(label_a2copia, label_a3copia)

        a_quadrado = MathTex(r'a^2').shift(0.5*DOWN + 0.5*RIGHT).scale(0.7)

        self.play(label_a2copia.animate.shift(1.5*LEFT), FadeIn(multiplicacao_4), label_a3copia.animate.shift(1.9*UP + 0.3*LEFT))

        self.wait(2)

        self.play(Transform(grupo_a, a_quadrado), FadeOut(multiplicacao_4))

        self.wait(2)

        self.play(self.camera.frame.animate.shift(2*DOWN).scale(1.5))

        self.wait(2)

        quadrado_soma = MathTex(r'(a + b)^2').shift(4.0*DOWN + 0.2*LEFT)

        igual = MathTex(r'=').shift(4.1*DOWN + 1.0*RIGHT)

        self.play(FadeIn(quadrado_soma), FadeIn(igual))

        self.wait(2)

        grupo_ab1 = VGroup()
        grupo_ab1.add(label_a1, label_b3copia)
        grupo_ab1.scale(1.7)
        
        grupo_ab2 = VGroup()
        grupo_ab2.add(label_a4copia, label_b4copia)

        grupo_a.scale(1.7)

        mais1 = MathTex(r'+').shift(5.1*DOWN + 1.3*LEFT)
        mais2 = MathTex(r'+').shift(5.1*DOWN + 1.5*RIGHT)

        dois = MathTex(r'2').shift(5.1*DOWN + 0.6*LEFT)

        grupob1.scale(1.7)

        self.play(grupo_a.animate.shift(4.5*DOWN + 2.5*LEFT), FadeIn(mais1), 
        grupo_ab1.animate.shift(6.6*DOWN), multiplicacao_2.animate.shift(6.6*DOWN),
        FadeOut(grupo_ab2), FadeOut(multiplicacao_3), FadeIn(dois), FadeIn(mais2), grupob1.animate.shift(6.6*DOWN + 3*RIGHT))

        self.wait(2)