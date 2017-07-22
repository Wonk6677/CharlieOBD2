#!/usr/bin/env python
###########################################################################
# Charlie Carputer
#
# Created by Ben Bament
# Based on piOBD2 code by Paul Bartek (pbartek@cowfishstudios.com)
#
###########################################################################

import os
import wx
import time
from threading import Thread
from obd_capture import OBD_Capture
from obd_sensors import SENSORS
from obd_sensors import *
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder


def obd_connect(o):
    o.connect()

#-------------------------------------------------------


class OBDConnection(object):
    """
    Class for OBD connection. Use a thread for connection.
    """

    def __init__(self):
        self.c = OBD_Capture()

    def get_capture(self):
        return self.c

    def connect(self):
        self.t = Thread(target=obd_connect, args=(self.c,))
        self.t.start()

    def is_connected(self):
        return self.c.is_connected()

    def get_output(self):
        if self.c and self.c.is_connected():
            return self.c.capture_data()
        return ""

    def get_port(self):
        return self.c.is_connected()

    def get_port_name(self):
        if self.c:
            port = self.c.is_connected()
            if port:
                try:
                    return port.port.name
                except:
                    pass
        return None

    def get_sensors(self):
        sensors = []
        if self.c:
            sensors = self.c.getSupportedSensorList()
        return sensors


#---------------------------------------------------------------------------------

class OBDLoadingPanel(wx.Panel):
    """
    Main panel for OBD application.

    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super(OBDLoadingPanel, self).__init__(*args, **kwargs)
        # Create an accelerator table
        cid = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onCtrlC, id=cid)
        self.accel_tbl = wx.AcceleratorTable([
            (wx.ACCEL_CTRL, ord('C'), cid),
        ])
        self.SetAcceleratorTable(self.accel_tbl)

        # Connection
        self.c = None

        # Sensors list
        self.sensors = []

        # Port
        self.port = None

    def getConnection(self):
        return self.c

    def showLoadingScreen(self):
        """
        Display the loading screen.
        """
        boxSizer = wx.BoxSizer(wx.VERTICAL)
        self.textCtrl = OBDText(self)
        boxSizer.Add(self.textCtrl, 1, wx.EXPAND | wx.ALL, 92)
        self.SetSizer(boxSizer)
        font3 = wx.Font(16, wx.ROMAN, wx.NORMAL, wx.NORMAL, faceName="Monaco")
        self.textCtrl.SetFont(font3)
        self.textCtrl.AddText(" Opening interface (serial port)\n")
        self.textCtrl.AddText(" Trying to connect...\n")

        self.timer0 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.connect, self.timer0)
        self.timer0.Start(1000)

    def connect(self, event):
        if self.timer0:
            self.timer0.Stop()

        # Connection
        self.c = OBDConnection()
        self.c.connect()
        connected = False
        while not connected:
            connected = self.c.is_connected()
            self.textCtrl.Clear()
            self.textCtrl.AddText(" Trying to connect ..." + time.asctime())
            if connected:
                break

        if not connected:
            self.textCtrl.AddText(" Not connected\n")
            return False
        else:
            self.textCtrl.Clear()
            # self.textCtrl.AddText(" Connected\n")
            port_name = self.c.get_port_name()
            if port_name:
                self.textCtrl.AddText(" Failed Connection: " + port_name + "\n")
                self.textCtrl.AddText(" Please hold alt & esc to view terminal.")
            self.textCtrl.AddText(str(self.c.get_output()))
            self.sensors = self.c.get_sensors()
            self.port = self.c.get_port()

            self.GetParent().update(None)

    def getSensors(self):
        return self.sensors

    def getPort(self):
        return self.port

    def onCtrlC(self, event):
        self.GetParent().Close()

    def OnPaint(self, event):
        self.Paint(wx.PaintDC(self))

    def Paint(self, dc):
        dc.DrawBitmap(self.bitmap, 0, 0)

#----------------------------------------------------------------------


Builder.load_file('screenmanager.kv')


class MainScreen(Screen):
    hue = NumericProperty(122)


class ScreenManagerApp(App):
    rpm = sensors.rpm
    def build(self):
        root = ScreenManager()
       # for x in range(4):
        root.add_widget(MainScreen(name='Screen1'))
        return root

if __name__ == '__main__':
    ScreenManagerApp().run()