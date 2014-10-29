#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    29.10.2014 09:20:52 CET
# File:    begin_learning.py

import sys

class begin_learning_class(object):
    def __init__ (self, com):
        self.data_ = 255
        self.com = com
        
    def write(self):
        self.com.write(bytes([ord('a'), 5, self.data_]))
        
    def name(self):
        return "begin_learning"
