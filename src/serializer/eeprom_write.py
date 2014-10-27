#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    27.10.2014 15:42:38 CET
# File:    eeprom_write.py

import sys

class eeprom_write_class(object):
    def __init__ (self, com):
        self.data_ = "'no data'"
        self.com = com
        
    def write(self):
        self.com.write(b'e')
    
    def name(self):
        return "eeprom_write"
