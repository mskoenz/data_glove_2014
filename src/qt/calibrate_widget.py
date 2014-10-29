#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    14.08.2014 10:24:04 CEST
# File:    calibrate.py

from src_import import *
from src.serializer import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import *

import sys

class Q2calibrate(QWidget):
    done = pyqtSignal()
    def __init__(self, parent = None):
        super(Q2calibrate, self).__init__(parent)
        #=================== logic ===================
        self.sp = QSerialPort()
        self.sp.setPortName("/dev/ttyUSB0")
        self.sp.open(QIODevice.ReadWrite)
        
        path = abspath(__file__) + "/../png/"
        self.icons = [path + "z_gest.png", path + "u_gest.png", path + "i_gest.png", path + "o_gest.png", path + "p_gest.png"]
        
        self.cur_gest = current_gest_class(self.sp)
        self.begin_learning = begin_learning_class(self.sp)
        self.learning_progress = learning_progress_class(self.sp)
        
        self.learn = False
        
        self.init_ui()
        
    def init_ui(self):
        #=================== widgets ==================
        self.btn = []
        for ic in self.icons:
            b = QPushButton(self)
            b.setIcon(QIcon(ic))
            b.setIconSize(QSize(50, 50))
            
            b.setAutoFillBackground(True)
            
            self.btn.append(b)
        self.end_btn = QPushButton("Done", self)
        self.timer = QTimer(self)
        #=================== properties ===============
        self.timer.setSingleShot(False)
        
        #=================== connects =================
        self.timer.timeout.connect(self.timer_timeout)
        self.end_btn.pressed.connect(self.done_handler)
        
        def learn_helper(idx):
            def res():
                if self.learn == True:
                    return
                self.learn = True
                self.timer.timeout.disconnect(self.timer_timeout)
                self.begin_learning.data_ = idx
                self.learn_idx = idx
                self.begin_learning.write()
                for b, b_i in zipi(self.btn):
                    b.setStyleSheet("background-color: #FFFFFF")
                self.timer.timeout.connect(self.timer_timeout_learn)
            return res
        
        for b, b_i in zipi(self.btn):
            b.pressed.connect(learn_helper(b_i))
        
        #=================== layout ===================
        grid = QGridLayout()
        for b, b_i in zipi(self.btn):
            grid.addWidget(b, b_i, 1, 1, 1)
        grid.addWidget(self.end_btn, len(self.btn), 1, 1, 1)
        self.setLayout(grid)
        #=================== finish ===================
        self.show()
        
        
    def timer_timeout_learn(self):
        self.learning_progress.read()
        #~ print(self.learning_progress.data_)
        self.btn[self.learn_idx].setText("{}/5".format(self.learning_progress.data_))
        if self.learning_progress.data_ == 5:
            self.btn[self.learn_idx].setText("")
            self.timer.timeout.disconnect(self.timer_timeout_learn)
            self.learn = False
            self.timer.timeout.connect(self.timer_timeout)
        
    def timer_timeout(self):
        
        self.cur_gest.read()
        
        for b, b_i in zipi(self.btn):
            if self.cur_gest.data_ == b_i:
                b.setStyleSheet("background-color: #00FF00")
            else:
                b.setStyleSheet("background-color: #FFFFFF")
    
    def enter_handle(self):
        self.timer.start(20)
    
    def done_handler(self):
        self.timer.stop()
        print("Q2calibrate done")
        self.done.emit()
