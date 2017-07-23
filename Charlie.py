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
    def obdrpm(self):
        #while True:
        #    RPM = obd.commands.RPM
        #    response = connection.query(RPM)
        #    return (response.value)
        #    time.sleep(1)
        w = "2000 or something"  #place holder while not in car
        return w


#class ScreenManagerApp(App):
#    def build(self):
 #       root = ScreenManager()
#       # for x in range(4):
#        root.add_widget(MainScreen(name='Screen1'))
#        return root

if __name__ == '__main__':
    ScreenManagerApp().run()