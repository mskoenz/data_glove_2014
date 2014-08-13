#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    13.08.2014 15:16:44 CEST
# File:    userbase_test.py

import package_proxy as px
import sys

if __name__ == "__main__":
    print("userbase_test.py")
    
    ub = px.userbase()
    
    d = {}
    d["fname"] = "Mario"
    d["lname"] = "Koenz"
    d["tag"] = "mkoenz"
    d["study"] = "N"
    d["age"] = "24"
    d["gender"] = "m"
    ub.add_user(**d)
    
    ub.add_user(fname = "Andreas", lname = "Frutiger", tag = "afrutig", study = "ing", age = "25", gender = "m")
    
    ub.write("test")
    print(ub.all_user)
    
    ub2 = px.userbase()
    ub2.load("test")
    print(ub2.all_user)
