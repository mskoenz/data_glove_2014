#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    29.10.2014 09:20:32 CET
# File:    learning_progress.py

import sys

class learning_progress_class(object):
    def __init__ (self, com):
        self.data_ = 0
        self.com = com
        
    def read(self):
        self.com.write(b'b')
        self.com.waitForReadyRead(-1) #wait 10ms
        d = self.com.readAll()
        d = d.data()
        
        self.data_ = int(d[0])
    
    def name(self):
        return "learning_progress"
