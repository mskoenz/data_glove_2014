#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    13.08.2014 19:38:35 CEST
# File:    survey.py

from src_import import *

class survey(object):
    def __init__ (self):
        self.label = ["comfort", "speed", "confine", "dependable", "precision", "style", "calibrate", "overall"]
        self.clear()
    
    def set_data(self, **kwargs):
        for l in self.label:
            self.survey[l] = kwargs[l]
            self.survey["comment"] = kwargs["comment"]
    
    def write(self, name):
        """
        Pickles the userbase into a file called name.pickle in the folder ./../userbase.
        This function overwrites files if same name.
        """
        path = abspath(__file__) + "/../data/"
        
        nr = 0
        while readable(path + name + "-{:0>2}.pickle".format(nr)):
            nr += 1
        
        GREEN("written react-data to " + name + "-{:0>2}.pickle".format(nr))
        
        f = open(path + name + "-{:0>2}.pickle".format(nr), "wb")
        pickle.dump(self.survey, f)
        f.close()
    
    def clear(self):
        self.survey = {}
    
