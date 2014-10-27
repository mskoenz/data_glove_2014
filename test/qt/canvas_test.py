#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    13.10.2014 15:25:37 CEST
# File:    canvas_test.py

import sys

from package_proxy import *

if __name__ == "__main__":
    print("canvas_test.py")
    app = qt.QApplication(sys.argv)
    w = qt.Q2CanvasWidget()
    app.exec_()
    
