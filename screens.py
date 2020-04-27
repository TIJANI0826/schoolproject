from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang.builder import Builder
import os
from kivymd.theming import ThemeManager


class Subject(Screen):
    pass


class Library(Screen):
    pass


class Lab(Screen):
    pass


class Exam(Screen):
    pass


class Activity(Screen):
    pass


class ClassModule(Screen):
    pass


class Curriculum(Screen):
    pass


class Features(Screen):
    pass


class Practicals(Screen):
    pass


class VirtualPractical(Screen):
    pass


class Setting(Screen):
    pass


class Register(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""


class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""
