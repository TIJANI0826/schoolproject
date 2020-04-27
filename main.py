from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.uix.popup import Popup
from kivymd.theming import ThemeManager
from Practice.SCHOOL_PROJECT.kv.connected import Connected
from Practice.SCHOOL_PROJECT.screens import Mathematics, English, Civic, Islamic, Arabic
class CustomLayout(BoxLayout):
    pass


class ShowcaseScreen(Screen):
    fullscreen = BooleanProperty(False)

    def add_widget(self, *args):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args)
        return super(ShowcaseScreen, self).add_widget(*args)


class LoginApp(App):
    theme_cls = ThemeManager()
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Register(name='register'))
        manager.add_widget(Connected(name='connected'))

        return manager

    def go_view(self):
        setting = Popup(title='Settings',\
                        size_hint=(.7, 0.7),\
                        background_color=(0, 0, .9, .5),\
                        auto_dismiss=True)
        setting.open()


    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )


if __name__ == '__main__':
    LoginApp().run()
