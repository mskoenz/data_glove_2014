#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    13.08.2014 15:06:41 CEST
# File:    userbase.py

from src_import import *

class userbase(object):
    def __init__ (self):
        self.clear()
    
    def add_user(self, **kwargs):
        lbl = ["tag", "fname", "lname", "study", "age", "gender"]
        self.user[kwargs["tag"]] = {}
        for l in lbl:
            self.user[kwargs["tag"]][l] = kwargs[l]
    
    def write(self, name):
        """
        Pickles the userbase into a file called name.pickle in the folder ./../userbase.
        This function overwrites files if same name.
        """
        path = abspath(__file__) + "/../userbase/"
        
        f = open(path + name + ".pickle", "wb")
        pickle.dump(self.user, f)
        f.close()
    
    def load(self, name):
        """
        Unpickles a userbase from a file called name.pickle in the folder ./../userbase if there is one.
        """
        path = abspath(__file__) + "/../userbase/"
        
        if not readable(path + name + ".pickle"):
            return
        
        f = open(path + name + ".pickle", "rb")
        self.user = pickle.load(f)
        f.close()
    
    def __getitem__(self, key):
        return self.user[key]
    
    @property
    def all_user(self):
        return list(self.user.keys())
    
    def clear(self):
        self.user = {}
