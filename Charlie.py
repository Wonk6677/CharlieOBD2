#!/usr/bin/env python
###########################################################################
# Charlie Carputer
#
# Created by Ben Bament
# Based on piOBD2 code by Paul Bartek (pbartek@cowfishstudios.com)
#
###########################################################################

import os
import obd
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.graphics import *
from kivy.graphics import Color
from kivy.properties import StringProperty
from kivy.clock import Clock

#-------------------------------------
connection = obd.OBD() #automagically connects to car ECU
#Builder.load_file('screenmanager.kv')


class MainScreen(Screen):
    pass

class speed(Screen):
    pass

class ScreenManagerApp(App):
    hsvcolor = Color(122, 91, 21, mode='hsv')

    def build(self):
        root = ScreenManager()
        root.add_widget(MainScreen(name='MainScreen'))
        root.add_widget(speed(name='speed'))
        return root

    def obdrpm(self):
        RPM = obd.commands.RPM
        response = connection.query(RPM)
        return str(response.value)

    def speedmph(self):
        y = 1
        while True:
            t = y
            t += 1
            y = t
            return str(t)

    Clock.schedule_interval(speedmph, 1)
    Clock.schedule_interval(obdrpm, 0.5)

if __name__ == '__main__':
    ScreenManagerApp().run()