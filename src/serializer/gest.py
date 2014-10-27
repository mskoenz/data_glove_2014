#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    14.10.2014 16:18:30 CEST
# File:    gest.py

import sys

class gest_class(object):
    def __init__ (self, com, id_):
        self.data_ = [[0, 0, 0, 0, 0, 0, 0, 0, 0]
                    , [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.gest_id = id_;
        self.com = com
        
    def read(self):
        self.com.write(bytes([ord('r'), self.gest_id]))
        
        self.com.waitForReadyRead(10)
        d = self.com.readAll()
        while(self.com.waitForReadyRead(10)): #wait 10ms and if time out, leave loop
            d += self.com.readAll()
        
        d = d.data()
        for i in range(9):
            self.data_[0][i] = d[i]
            self.data_[1][i] = d[9+i]
        self.gest_id = d[18]
    
    def write(self):
        b = self.data_[0] + self.data_[1] + [self.gest_id]
        self.com.write(bytes([ord('w'), self.gest_id] + b))
    
    def name(self):
        return "gest {}".format(self.gest_id)
