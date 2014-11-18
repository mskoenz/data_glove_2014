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
    gest_wo5_data = []
    key_wo5_data = []
    mink_data = []
    ming_data = []
    wrongk_data = []
    wrongg_data = []
    
    fastestk_ = [[],[],[],[],[]]
    fastestg_ = [[],[],[],[],[]]
    
    key = ["z", "u", "i", "o", "p"]
    
    path = abspath(__file__) + "/../data/"
    gest_files = glob.glob(path + "*gest*.pickle")
    key_files =  glob.glob(path + "*key*.pickle")
    gest_files.sort()
    key_files.sort()
    
    for f in key_files:
        name = f.split("/")[-1].split("_")[0]
        ifs = open(f, "rb")
        temp = pickle.load(ifs)
        r = reaction([], [], 0)
        r.hist = temp
        key_data.append([name, r.evaluate["mean"]])
        key_wo5_data.append([name, np.mean(sorted([x["react"] for x in r.valid_result])[:29])])
        mink_data.append([name, r.evaluate["min"]])
        wrongk_data.append([name, r.evaluate["wrong"]])
        
        for i in range(5):
            fastestk_[i].append([name, np.min([x["react"] for x in r.valid_result if x["key"] == key[i]])])
        
        ifs.close()
    
    for f in gest_files:
        name = f.split("/")[-1].split("_")[0]
        ifs = open(f, "rb")
        temp = pickle.load(ifs)
        r = reaction([], [], 0)
        r.hist = temp
        gest_data.append([name, r.evaluate["mean"]])
        gest_wo5_data.append([name, np.mean(sorted([x["react"] for x in r.valid_result])[:29])])
        ming_data.append([name, r.evaluate["min"]])
        wrongg_data.append([name, r.evaluate["wrong"]])
        
        for i in range(5):
            fastestg_[i].append([name, np.min([x["react"] for x in r.valid_result if x["key"] == key[i]])])
        
        ifs.close()
    
    def sort_second(data):
        return sorted(data, key = lambda x: x[1])
    
    res = [sort_second(key_data)
         , sort_second(gest_data)
         , sort_second(key_wo5_data)
         , sort_second(gest_wo5_data)
         , sort_second(mink_data) 
         , sort_second(ming_data)]
    
    for i in range(5):
        res.append(sort_second(fastestk_[i]))
    for i in range(5):
        res.append(sort_second(fastestg_[i]))
    
    #~ res.append(sort_second(wrongk_data))
    #~ res.append(sort_second(wrongg_data))
    
    return res

if __name__ == "__main__":
    #~ print("ranking.py")
    l = generate_ranking()
    
    title = [ "  mean keyboard reaction   "
            , " mean data glove reaction  "
            , " mean keyb. w/o worst time "
            , "mean datagl. w/o worst time"
            , " minimal keyboard reaction "
            , "minimal data glove reaction"
            , "    fastest z key react    "
            , "    fastest u key react    "
            , "    fastest i key react    "
            , "    fastest o key react    "
            , "    fastest p key react    "
            , "       fastest fist        "
            , "    fastest two finger     "
            , "   fastest three finger    "
            , "    fastest four finger    "
            , "     fastest open hand     "
            ]
    
    for t, t_i in zipi(title):
        print(t)
        print("===========================")
        print("")
        for u, u_i in zipi(l[t_i]):
            print("{:0>2}:  {:<12} {:>6.1f} ms".format(u_i+1, u[0], u[1]))
        print("")
        print("")
