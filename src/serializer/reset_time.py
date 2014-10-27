#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    27.10.2014 16:01:27 CET
# File:    reset_time.py

import sys

class reset_time_class(object):
    def __init__ (self, com):
        self.data_ = "'no data'"
        self.com = com
        
    def write(self):
        self.com.write(b'y')
    
    def read(self):
        self.com.write(b't')
        self.com.waitForReadyRead(10)
        d = self.com.readAll()
        while(self.com.waitForReadyRead(10)):
            d += self.com.readAll()
        
        d = d.data()
        
        if len(d) == 4:
            self.data_ = 0
            for i in range(4):
                self.data_ += (int(d[i]) << 8*i)
    
    def name(self):
        return "reset_time"
