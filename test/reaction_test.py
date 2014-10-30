#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    13.08.2014 15:28:36 CEST
# File:    reaction_test.py

import package_proxy as px
import sys
if __name__ == "__main__":
    print("reaction_test.py")
    #~ r = px.reaction(['z', 'u', 'i', 'o', 'p'], px.drange(1000, 5000, 500), 5)
    r = px.reaction(['z'], [1000], 5)
    
    while not r.done:
        key, delay = r.start()
        print("wait for it...")
        r.wait()
        x = input("press {}".format(key))
        print(r.stop(x))
    
    print([msm["react"] for msm in r.result])
    print(r.evaluate)
    r.write("mkoenz")
