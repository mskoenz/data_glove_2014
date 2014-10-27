#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    27.10.2014 15:49:56 CET
# File:    remove_all.py

import sys

class remove_all_class(object):
    def __init__ (self, com):
        self.data_ = "'no data'"
        self.com = com
        
    def write(self):
        self.com.write(b'd')
    
    def name(self):
        return "remove_all"
