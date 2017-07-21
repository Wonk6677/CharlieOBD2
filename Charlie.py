from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder

Builder.load_file('screenmanager.kv')


class MainScreen(Screen):
    hue = NumericProperty(0)


class ScreenManagerApp(App):

    def build(self):
        root = ScreenManager()
        for x in range(4):
            root.add_widget(MainScreen(name='Screen %d' % x))
        return root

if __name__ == '__main__':
    ScreenManagerApp().run()