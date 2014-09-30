#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    14.08.2014 10:24:04 CEST
# File:    calibrate.py

from src_import import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import *

import sys

class calibrate(QWidget):
    def __init__(self):
        super(calibrate, self).__init__()
        self.sp = QSerialPort()
        self.sp.setPortName("/dev/ttyUSB0")
        self.sp.open(QIODevice.ReadWrite)
        time.sleep(2)
        self.show()
    
    def send(self):
        self.sp.write(b's')
        #~ self.sp.waitForBytesWritten(1)
        self.sp.waitForReadyRead(9)
        d = self.sp.readAll()
        i = [int(c) for c in d.data()]
        print(i)
        
    def keyPressEvent(self, e):
        self.send()

if __name__ == "__main__":
    print("calibrate.py")
    app = QApplication(sys.argv)
    c = calibrate()
    app.exec_()
    
    
