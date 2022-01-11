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
from Purple import Purple
from Players import *
from Class_Players import *

Builder.load_file('Main.kv')

class Menu(Screen):
    pass

class AndroidApp(App):
    title = 'Arukoru - KivyApp'
    def build(self):
        Window.fullscreen = 'auto'
        sm = ScreenManager()
        sm.add_widget(Menu(name='MainWindow'))
        sm.add_widget(Purple(name='PurpleWindow'))
        sm.add_widget(Players(name='PlayersWindow'))
        return sm

if __name__ == "__main__":
    AndroidApp().run()