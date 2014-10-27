#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    14.08.2014 10:24:04 CEST
# File:    calibrate.py

from src_import import *
from src.serializer import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import *

import sys

class Q2SerializeIOWidget(QWidget):
    def __init__(self):
        super(Q2SerializeIOWidget, self).__init__()
        #=================== logic ===================
        self.sp = QSerialPort()
        self.sp.setPortName("/dev/ttyUSB0")
        self.sp.open(QIODevice.ReadWrite)
        
        time.sleep(2)
        
        self.logic_units = [  pos_class(self.sp)
                            , n_gest_class(self.sp)
                            , gest_class(self.sp, 0)
                            , gest_class(self.sp, 1)
                            , gest_class(self.sp, 2)
                            , gest_class(self.sp, 3)
                            , gest_class(self.sp, 4)
                            , eeprom_write_class(self.sp)
                            , remove_all_class(self.sp)
                            , reset_glove_class(self.sp)
                            , reset_time_class(self.sp)
                           ]
        
        
        self.init_ui()
        
    def init_ui(self):
        #=================== widgets ==================
        self.lbls = []
        self.texts = []
        self.btns = []
        for l in self.logic_units:
            
            self.lbls.append(QLabel(l.name(), self))
            self.texts.append(QTextEdit(str(l.data_), self))
            self.btns.append(QPushButton("Read", self))
            self.btns.append(QPushButton("Write", self))
        #=================== properties ===============
        
        #=================== connects =================
        def read_helper(logic, textw):
            def res():
                logic.read()
                textw.setText(str(logic.data_))
            return res
        
        def write_helper(logic, textw):
            def res():
                logic.data_ = eval(textw.toPlainText())
                logic.write()
            return res
        
        for l, l_i in zipi(self.logic_units):
            if hasattr(l, "read"):
                self.btns[2*l_i].clicked.connect(read_helper(l, self.texts[l_i]))
            else:
                self.btns[2*l_i].setEnabled(False)
            
            
            if hasattr(l, "write"):
                self.btns[2*l_i + 1].clicked.connect(write_helper(l, self.texts[l_i]))
            else:
                self.btns[2*l_i + 1].setEnabled(False)
        #=================== layout ===================
        grid = QGridLayout(self)
        
        n_layout = 6
        
        for w, w_i in zipi(self.lbls):
            grid.addWidget(w, 2*(w_i%n_layout), 3*(w_i//n_layout), 2, 1)
        
        for w, w_i in zipi(self.texts):
            grid.addWidget(w, 2*(w_i%n_layout), 3*(w_i//n_layout)+1, 2, 1)
        for w, w_i in zipi(self.btns):
            grid.addWidget(w, (w_i%(2*n_layout)), 3*(w_i//(2*n_layout))+2, 1, 1)
        
        self.setLayout(grid)
        #=================== finish ===================
        self.show()
    
    
    def write(self, obj):
        obj.write()
    
    def read(self, obj):
        obj.read()
