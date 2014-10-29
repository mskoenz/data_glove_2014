#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    14.08.2014 10:24:04 CEST
# File:    calibrate.py

from src_import import *
from serializer import *

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
        
        #~ time.sleep(2)
        
        self.pos = pos_class(self.sp)
        self.n_gest = n_gest_class(self.sp)
        self.gest_0 = gest_class(self.sp, 0)
        self.show()
    
    def write(self, obj):
        obj.write()
    
    def read(self, obj):
        obj.read()
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_R:
            self.read(self.gest_0)
            print(self.gest_0)
        if e.key() == Qt.Key_W:
            self.n_gest.n_ += 1
            print(self.gest_0)
            self.write(self.gest_0)
        if e.key() == Qt.Key_E:
            self.sp.write(b'e')
            print("EEPROM")
        if e.key() == Qt.Key_N:
            self.read(self.n_gest)
            print(self.n_gest)
        if e.key() == Qt.Key_P:
            self.read(self.pos)
            print(self.pos)
        

if __name__ == "__main__":
    print("calibrate.py")
    app = QApplication(sys.argv)
    c = calibrate()
    app.exec_()
