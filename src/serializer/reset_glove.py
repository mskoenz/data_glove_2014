#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    27.10.2014 16:01:20 CET
# File:    reset_glove.py

import sys

class reset_glove_class(object):
    def __init__ (self, com):
        self.data_ = "'no data'"
        self.com = com
        
    def write(self):
        self.com.write(b'x')
    
    def name(self):
        return "reset_glove"
