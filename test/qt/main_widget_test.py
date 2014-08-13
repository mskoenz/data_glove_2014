#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    13.08.2014 17:49:18 CEST
# File:    main_widget_test.py

from package_proxy import qt
import sys

if __name__ == "__main__":
    print("main_widget_test.py")
    app = qt.QApplication(sys.argv)
    w = qt.Q2main()
    app.exec_()
