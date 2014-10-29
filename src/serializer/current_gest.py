#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    29.10.2014 11:15:27 CET
# File:    current_gest.py

import sys

class current_gest_class(object):
    def __init__ (self, com):
        self.data_ = 0
        self.com = com
        
    def read(self):
        self.com.write(b'c')
        self.com.waitForReadyRead(-1) #wait forever
        d = self.com.readAll()
        d = d.data()
        
        self.data_ = int(d[0])
    
    def name(self):
        return "current_gest"
