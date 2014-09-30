#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    14.08.2014 10:19:38 CEST
# File:    calibration_widget.py


import qt.language as lg

from src.reaction import *

from src.addon import *
from src.addon.qt5 import *

class Q2calibrate(QWidget):
    def __init__(self, parent = None):
        super(Q2calibrate, self).__init__(parent)
    
    def init_ui(self):
        #=================== widgets ==================
        
        #=================== properties ===============
        
        #=================== connects =================
        
        #=================== layout ===================
        
        #=================== finish ===================
        self.show()
