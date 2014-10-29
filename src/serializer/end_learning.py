#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    29.10.2014 09:20:43 CET
# File:    end_learning.py

import sys

class end_learning_class(object):
    def __init__ (self, com):
        self.data_ = "'no data'"
        self.com = com
        
    def write(self):
        self.com.write(b'f')
    
    def name(self):
        return "end_learning"
