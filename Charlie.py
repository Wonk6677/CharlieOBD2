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
import time
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.graphics import *

#-------------------------------------
connection = obd.OBD() #automagically connects to car ECU
Builder.load_file('screenmanager.kv')


class MainScreen(Screen):
    pass

class speed(Screen):
    pass

#create screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='MainScreen'))
sm.add_widget(speed(name='speed'))

class ScreenManagerApp(App):
    def build(self):
        return sm

    def obdrpm(self):
        #while True:
        #    RPM = obd.commands.RPM
        #    response = connection.query(RPM)
        #    return (response.value)
        #    time.sleep(1)
        w = "2000 or something"  #place holder while not in car
        return w

    def speed(self):
        x = "60 or less"
        return x

if __name__ == '__main__':
    MainScreen().run()