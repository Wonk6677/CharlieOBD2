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

class ScreenManagerApp(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(MainScreen(name='MainScreen'))
        root.add_widget(speed(name='speed'))
        return root

    def obdrpm(self):
        #while True:
         #   RPM = obd.commands.RPM
          #  response = connection.query(RPM)
           # return (response.value)
            #time.sleep(1)
        w = "2000 or something"  #place holder while not in car
        return w

    def speed(self):
        while true:
            t = 1
            x = t+1
            t = x
            time.sleep(1)
            return t

if __name__ == '__main__':
    ScreenManagerApp().run()