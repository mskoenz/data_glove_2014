#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    30.10.2014 10:09:02 CET
# File:    ranking.py

from src_import import *
import glob
from reaction import *
    
def generate_ranking():
    gest_data = []
    key_data = []

    path = abspath(__file__) + "/../data/"
    gest_files = glob.glob(path + "*gest*.pickle")
    key_files =  glob.glob(path + "*key*.pickle")
    gest_files.sort()
    key_files.sort()
    
    for f in gest_files:
        name = f.split("/")[-1].split("_")[0]
        ifs = open(f, "rb")
        temp = pickle.load(ifs)
        r = reaction([], [], 0)
        r.hist = temp
        gest_data.append([name, r.evaluate["mean"]])
        ifs.close()
    
    for f in key_files:
        name = f.split("/")[-1].split("_")[0]
        ifs = open(f, "rb")
        temp = pickle.load(ifs)
        r = reaction([], [], 0)
        r.hist = temp
        key_data.append([name, r.evaluate["mean"]])
        ifs.close()
    
    return sorted(key_data, key = lambda x: x[1]), sorted(gest_data, key = lambda x: x[1])

if __name__ == "__main__":
    #~ print("ranking.py")
    l = generate_ranking()
    
    print(" keyboard reaction ranking")
    print("===========================")
    print("")
    for u, u_i in zipi(l[0]):
        print("{:0>2}:  {:<12} {:>6.1f} ms".format(u_i+1, u[0], u[1]))
    print("")
    print("")
    print("data glove reaction ranking")
    print("===========================")
    print("")
    for u, u_i in zipi(l[1]):
        print("{:0>2}:  {:<12} {:>6.1f} ms".format(u_i+1, u[0], u[1]))
