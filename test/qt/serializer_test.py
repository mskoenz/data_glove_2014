#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    27.10.2014 15:02:45 CET
# File:    serializer_test.py

import sys

from package_proxy import *

if __name__ == "__main__":
    print("serializer_test.py")
    app = qt.QApplication(sys.argv)
    w = qt.Q2SerializeIOWidget()
    app.exec_()
    
