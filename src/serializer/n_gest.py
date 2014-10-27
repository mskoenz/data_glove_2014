#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    09.10.2014 10:14:02 CEST
# File:    pos.py

import sys

class n_gest_class(object):
    def __init__ (self, com):
        self.data_ = 0
        self.com = com
        
    def read(self):
        self.com.write(b'n')
        self.com.waitForReadyRead(-1)
        d = self.com.readAll()
        d = d.data()
        
        self.data_ = int(d[0])
    
    def write(self):
        self.com.write(bytes([ord('m'), self.data_]))
    
    def name(self):
        return "n_gest"
