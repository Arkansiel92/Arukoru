from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.clock import Clock

from Class_Players import *
from Players import *
from random import randint


Builder.load_file('Purple.kv')

class Purple(Screen):
    name_player = ObjectProperty(None)
    name_challenge = ObjectProperty(None)

    L_challenge = ["Dit autant de qualites à ton joueur de droite que tu veux \nen 15 secondes. 1 compliment = 1 gorgée",
    "Dans ma valise. Tu commences.",
    "Rap jeu : le joueur donne un rappeur ou chanteur \nle voisin de gauche doit dire un autre rappeur/chanteur qui a fait un feat avec lui, \npuis un autre qui a fait un feat avec le rappeur/chanteur precedemment dit, ect...",
    "verite ou verite : \nTu peux poser n'importe quelle question à n'importe qui"]

    def Game(self):
        self.name_player.text = Players.L_name[randint(0, len(Players.L_name) - 1)]
        self.name_challenge.text = self.L_challenge[randint(0, len(self.L_challenge) - 1)]