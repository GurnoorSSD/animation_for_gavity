#for running this code, open cmd in the folder in which you have saved this code and type(manim -pqh your file name.py video name you want)
from manim import *
from gtts import gTTS
import os

# ---------- AI Voice ----------
voice_text = """
Gravity is the force that pulls objects toward each other.
It was discovered by Isaac Newton when he saw an apple fall.
The force of gravity is given by F equals G times m one times m two divided by r squared.
G is the universal gravitational constant.
g is the acceleration due to gravity on Earth.
Gravity keeps objects on the ground and planets in orbit.
"""

audio_file = "gravity_voice.mp3"
if not os.path.exists(audio_file):
    tts = gTTS(text=voice_text, lang='en')
    tts.save(audio_file)

# ---------- Manim Config ----------
config.output_file = "gravity_complex"
config.media_dir = "."
config.format = "mp4"

class GravityComplex(Scene):
    def construct(self):
        self.camera.background_color = "#f0f4f8"

        # ---------- Add AI voice ----------
        self.add_sound(audio_file)

        # ---------- Title ----------
        title = Text("Gravity: The Force That Rules the Universe", font_size=42, color="#1f77b4")
        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(1)
        self.play(FadeOut(title, shift=UP), run_time=1)

        # ---------- Isaac Newton + Apple ----------
        newton = SVGMobject("newton.svg").scale(0.5).to_edge(LEFT) if os.path.exists("newton.svg") else Circle(radius=0.5, color=BLUE).to_edge(LEFT)
        apple = Circle(radius=0.2, color=RED).next_to(newton, UP*2)
        self.play(FadeIn(newton), FadeIn(apple), run_time=2)

        # Apple falls
        self.play(apple.animate.shift(DOWN*2), run_time=2)

        # ---------- Text Explanation ----------
        text1 = Text("Isaac Newton observed objects falling 🍎", font_size=28, color="#1f77b4").to_edge(UP)
        self.play(Write(text1), run_time=2)
        self.wait(1)

        # ---------- Formulas ----------
        # Left formula: smaller and slightly lower
        formula_F = Text("F = G * (m1 × m2) / r²", font_size=22, color="#1f77b4").to_corner(UL).shift(DOWN*0.5)
        # Right formula stays the same
        formula_g = Text("g = (G × M) / r²", font_size=26, color="#2ca02c").to_corner(UR)
        self.play(FadeIn(formula_F), FadeIn(formula_g), run_time=2)

        # ---------- Label Constants ----------
        label_G = Text("G = 6.674×10^-11 N·m²/kg²", font_size=22, color=YELLOW).next_to(formula_F, DOWN, buff=0.1)
        label_F = Text("F = gravitational force", font_size=22, color=YELLOW).next_to(formula_F, LEFT, buff=0.1)
        label_g = Text("g ≈ 9.8 m/s² on Earth", font_size=24, color=YELLOW).next_to(formula_g, DOWN, buff=0.1)
        self.play(FadeIn(label_G), FadeIn(label_g), FadeIn(label_F), run_time=2)
        self.wait(1)

        # ---------- Planet Example ----------
        planet = Circle(radius=2, color="#ff7f0e", fill_opacity=0.8).shift(DOWN)
        satellite = Dot(color="#2ca02c").shift(UP*3)
        self.play(FadeIn(planet), FadeIn(satellite), run_time=2)

        # Satellite orbits
        self.play(satellite.animate.move_to(planet.get_top() + UP*0.2), run_time=3)
        self.play(Rotate(satellite, angle=TAU, about_point=planet.get_center()), run_time=5)

        # ---------- Final Text ----------
        final = Text("Gravity keeps everything in orbit 🌍", font_size=32, color="#1f77b4")
        self.play(FadeOut(formula_F), FadeOut(formula_g), FadeOut(label_G), FadeOut(label_g), FadeOut(label_F), FadeOut(text1), run_time=1)
        self.play(FadeIn(final), run_time=2)
        self.wait(2)

