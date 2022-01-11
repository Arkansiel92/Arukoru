from re import MULTILINE
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
from Class_Players import Player
from copy import copy
from kivy.uix.textinput import TextInput
from Class_Players import *



Builder.load_file('Players.kv')


class Players(Screen):
    i = 0
    L_name = []
    Joueur1 = StringProperty("")
    Joueur2 = StringProperty("")
    Joueur3 = StringProperty("")
    Joueur4 = StringProperty("")
    Joueur5 = StringProperty("")
    Joueur6 = StringProperty("")
    Joueur7 = StringProperty("")
    Joueur8 = StringProperty("")
    Joueur9 = StringProperty("")
    Joueur10 = StringProperty("")

    def add_player(self):
        player = self.ids.name_of_player
        if player.text != "" and self.i < 10:
            self.i += 1
            if self.i == 1:
                self.Joueur1 = str(player.text)
                player.text = ""
            elif self.i == 2:
                self.Joueur2 = str(player.text)
                player.text = ""
            elif self.i == 3:
                self.Joueur3 = str(player.text)
                player.text = ""
            elif self.i == 4:
                self.Joueur4 = str(player.text)
                player.text = ""
            elif self.i == 5:
                self.Joueur5 = str(player.text)
                player.text = ""
            elif self.i == 6:
                self.Joueur6 = str(player.text)
                player.text = ""
            elif self.i == 7:
                self.Joueur7 = str(player.text)
                player.text = ""
            elif self.i == 8:
                self.Joueur8 = str(player.text)
                player.text = ""
            elif self.i == 9:
                self.Joueur9 = str(player.text)
                player.text = ""
            elif self.i == 10:
                self.Joueur10 = str(player.text)
                player.text = ""
        print("Nombre de joueur :", self.i)
        

    def check_players(self):
        self.L_name.clear()
        if self.i >= 2:
            self.L_name.append(self.Joueur1)
            self.L_name.append(self.Joueur2)
        if self.i >= 3:
            self.L_name.append(self.Joueur3)
        if self.i >= 4:
            self.L_name.append(self.Joueur4)
        if self.i >= 5:
            self.L_name.append(self.Joueur5)
        if self.i >= 6:
            self.L_name.append(self.Joueur6)
        if self.i >= 7:
            self.L_name.append(self.Joueur7)
        if self.i >= 8:
            self.L_name.append(self.Joueur8)
        if self.i >= 9:
            self.L_name.append(self.Joueur9)
        if self.i >= 10:
            self.L_name.append(self.Joueur10)
        print(self.L_name)