#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    28.10.2014 14:19:14 CET
# File:    hist.py

import sys

class hist_class(object):
    def __init__ (self, com):
        self.data_ = [0, [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.com = com
        
    def read(self):
        self.com.write(b'h')
        self.com.waitForReadyRead(10)
        d = self.com.readAll()
        while(self.com.waitForReadyRead(10)):
            d += self.com.readAll()
        
        d = d.data()
        
        
        if len(d) == 27:
            i = 0
            
            self.data_[0] = int(d[0]) + (int(d[1]) << 8)
            
            i += 2
            for k in range(5):
                self.data_[k + 1][0] = int(d[i])
                i += 1
                self.data_[k + 1][1] = 0
                for l in range(4):
                    self.data_[k + 1][1] += (int(d[i+l]) << 8*l)
                i += 4
    
    def name(self):
        return "hist"
