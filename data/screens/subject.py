from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.properties import ObjectProperty, StringProperty, ListProperty, AliasProperty, DictProperty, NumericProperty, \
    BooleanProperty


class Subject(Screen):
    fullscreen = BooleanProperty(True)

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
