#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    09.10.2014 10:14:02 CEST
# File:    pos.py

import sys

class pos_class(object):
    def __init__ (self, com):
        self.data_ = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.com = com
        
    def read(self):
        self.com.write(b's')
        self.com.waitForReadyRead(10)
        d = self.com.readAll()
        while(self.com.waitForReadyRead(10)):
            d += self.com.readAll()
        
        d = d.data()
        
        if len(d) == 9:
            for i in range(9):
                self.data_[i] = int(d[i])
    
    def name(self):
        return "pos"
