#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    29.10.2014 14:10:44 CET
# File:    generate_csv.py

#for plot
import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
matplotlib.use('Agg') #only save /no show /must happen before pylab
import pylab
#done plot

from src_import import *
import glob
from reaction import *

glob_ylim = [500, 1000]

gest_data = []
key_data = []
surv_data = []

def load_files():
    path = abspath(__file__) + "/../data/"
    gest_files = glob.glob(path + "*gest*.pickle")
    key_files =  glob.glob(path + "*key*.pickle")
    surv_files = glob.glob(path + "*surv*.pickle")
    
    
    for f in gest_files:
        ifs = open(f, "rb")
        gest_data.append(pickle.load(ifs))
        ifs.close()
    
    for f in key_files:
        ifs = open(f, "rb")
        key_data.append(pickle.load(ifs))
        ifs.close()
    
    
    for f in surv_files:
        ifs = open(f, "rb")
        surv_data.append(pickle.load(ifs))
        ifs.close()
    
    for i in range(len(key_data)):
        temp = key_data[i]
        key_data[i] = reaction([], [], 0)
        key_data[i].hist = temp
    
    for i in range(len(gest_data)):
        temp = gest_data[i]
        gest_data[i] = reaction([], [], 0)
        gest_data[i].hist = temp

def write_survey_plot_data(name):
    ofs = open(name, "w")
    
    labels = ["calibrate", "comfort", "precision", "dependable", "confine", "speed", "style", "overall"]
    
    mea = []
    std = []
    err = []
    
    for l in labels:
        data = []
        for d in surv_data:
            data.append(d[l])
        mea.append(np.mean(data))
        std.append(np.std(data))
        err.append(np.std(data)/np.sqrt(len(surv_data)))
        ofs.write("{0},{1:.2f},{2:.2f},{3:.2f}\n".format(l, mea[-1], std[-1], err[-1]))
    
    ofs.close()
    
    #for plot
    fig, ax = pylab.subplots()
    fig.set_size_inches(8.6, 5.2)
    
    N = 8
    width = .6
    side_space = 0.5
    ind = np.arange(N)
    
    ax.bar(ind+side_space, mea, width, color='r', yerr=err, ecolor = 'k')
    pylab.xlim([0, N + 2*side_space - (1-width)])
    
    ax.set_xticks(ind+width/2+side_space)
    ax.set_xticklabels(labels)
    
    ax.set_yticks([0, 2, 4])
    ax.set_yticklabels(["bad", "neutral", "good"])
    
    ax.set_xlabel("Question", fontsize = 12)
    ax.set_ylabel("Rating", fontsize = 12, rotation = "horizontal", horizontalalignment = "left")
    ax.yaxis.set_label_coords(x = 0, y = 1.03)
    ax.set_title("Survey Data", fontsize = 18, horizontalalignment = "left", y = 1.06, x = 0)
    pylab.savefig(name.split(".txt")[0]+".tiff")
    #end plot

def write_mean_plot_data(name):
    ofs = open(name, "w")
    
    kb_mean = []
    dg_mean = []
    
    dg = [[x["react"] for x in r.valid_result] for r in gest_data]
    kb = [[x["react"] for x in r.valid_result] for r in key_data]
    
    for d in kb:
        kb_mean.append(np.mean(d))
    for d in dg:
        dg_mean.append(np.mean(d))
    
    mea = [np.mean(kb_mean), np.mean(dg_mean)]
    std = [np.std(kb_mean), np.std(dg_mean)]
    err = [np.std(kb_mean)/np.sqrt(len(kb_mean)), np.std(dg_mean)/np.sqrt(len(dg_mean))]
    
    ofs.write("Keyboard,{0:.2f},{1:.2f},{2:.2f}\n".format(mea[0], std[0], err[0]))
    ofs.write("Data Glove,{0:.2f},{1:.2f},{2:.2f}\n".format(mea[1], std[1], err[1]))
    
    ofs.close()
    
    #for plot
    fig, ax = pylab.subplots()
    fig.set_size_inches(3, 5.2)
    
    N = 2
    width = .6
    side_space = 0.5
    ind = np.arange(N)
    pylab.xlim([0, N + 2*side_space - (1-width)])
    pylab.ylim(glob_ylim)
    
    ax.bar(ind+side_space, mea, width, color='r', yerr=err, ecolor = 'k')
    
    ax.set_xticks(ind+width/2+side_space)
    ax.set_xticklabels(['Keyboard', 'Dataglove'])
    
    ax.set_xlabel("Device", fontsize = 12)
    ax.set_ylabel("Reactiontime [ms]", fontsize = 12, rotation = "horizontal", horizontalalignment = "left")
    ax.yaxis.set_label_coords(x = 0, y = 1.03)
    ax.set_title("Mean Reaction", fontsize = 18, horizontalalignment = "left", y = 1.06, x = 0)
    pylab.savefig(name.split(".txt")[0]+".tiff")
    #end plot

def write_key_plot_data(name):
    ofs = open(name, "w")
    
    keys = ["z", "u", "i", "o", "p"]
    labels = ["Key Z", "Key U", "Key I", "Key O", "Key P"]
    mean = [[],[],[],[],[]]
    
    for user in key_data:
        for msm in user.valid_result:
            mean[keys.index(msm["key"])].append(msm["react"])
    
    L = float(len(mean[0]) + len(mean[1]) + len(mean[2]) + len(mean[3]) + len(mean[4]))
    
    mea = []
    std = []
    err = []
    
    for l, m in zip(labels, mean):
        mea.append(np.mean(m))
        std.append(np.std(m))
        err.append(np.std(m) / np.sqrt(len(m)))
        ofs.write(l+",{0:.2f},{1:.2f},{2:.2f},{3:.2f}\n".format(mea[-1]
                                                             , std[-1]
                                                             , err[-1]
                                                             , len(m) / L))
    ofs.close()
    
    #for plot
    fig, ax = pylab.subplots()
    fig.set_size_inches(3.6, 5.2)
    
    N = 5
    width = .6
    side_space = 0.5
    ind = np.arange(N)
    pylab.xlim([0, N + 2*side_space - (1-width)])
    pylab.ylim(glob_ylim)
    
    ax.bar(ind+side_space, mea, width, color='r', yerr=err, ecolor = 'k')
    
    ax.set_xticks(ind+width/2+side_space)
    ax.set_xticklabels(keys)
    
    ax.set_xlabel("Key", fontsize = 12)
    ax.set_ylabel("Reactiontime [ms]", fontsize = 12, rotation = "horizontal", horizontalalignment = "left")
    ax.yaxis.set_label_coords(x = 0, y = 1.03)
    ax.set_title("Mean Reaction Keyboard", fontsize = 18, horizontalalignment = "left", y = 1.06, x = 0)
    pylab.savefig(name.split(".txt")[0]+".tiff")
    #end plot
    
def write_gest_plot_data(name):
    ofs = open(name, "w")
    
    keys = ["z", "u", "i", "o", "p"]
    labels = ["Gesture 1", "Gesture 2", "Gesture 3", "Gesture 4", "Gesture 5"]
    mean = [[],[],[],[],[]]
    
    for user in gest_data:
        for msm in user.valid_result:
            mean[keys.index(msm["key"])].append(msm["react"])
    
    L = float(len(mean[0]) + len(mean[1]) + len(mean[2]) + len(mean[3]) + len(mean[4]))
    
    mea = []
    std = []
    err = []
    
    for l, m in zip(labels, mean):
        mea.append(np.mean(m))
        std.append(np.std(m))
        err.append(np.std(m) / np.sqrt(len(m)))
        ofs.write(l+",{0:.2f},{1:.2f},{2:.2f},{3:.2f}\n".format(mea[-1]
                                                             , std[-1]
                                                             , err[-1]
                                                             , len(m) / L))
    ofs.close()
    
    #for plot
    fig, ax = pylab.subplots()
    fig.set_size_inches(3.6, 5.2)
    
    N = 5
    width = .6
    side_space = 0.5
    ind = np.arange(N)
    pylab.xlim([0, N + 2*side_space - (1-width)])
    pylab.ylim(glob_ylim)
    
    ax.bar(ind+side_space, mea, width, color='r', yerr=err, ecolor = 'k')
    
    ax.set_xticks(ind+width/2+side_space)
    ax.set_xticklabels(["1", "2", "3", "4", "5"])
    
    ax.set_xlabel("Gesture", fontsize = 12)
    ax.set_ylabel("Reactiontime [ms]", fontsize = 12, rotation = "horizontal", horizontalalignment = "left")
    ax.yaxis.set_label_coords(x = 0, y = 1.03)
    ax.set_title("Mean Reaction Dataglove", fontsize = 18, horizontalalignment = "left", y = 1.06, x = 0)
    pylab.savefig(name.split(".txt")[0]+".tiff")
    #end plot

def write_key_delay_plot_data(name):
    ofs = open(name, "w")
    
    delay = [999, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    labels = ["1.0 s", "1.5 s", "2.0 s", "2.5 s", "3.0 s", "3.5 s", "4.0 s", "4.5 s"]
    
    mean = [[] for i in labels]
    
    for user in key_data:
        for msm in user.valid_result:
            mean[delay.index([n for n in delay if n<msm["delay"]][-1])].append(msm["react"])
    
    L = float(0)
    
    for m in mean:
        L += len(m);
    
    mea = []
    std = []
    err = []
    
    for l, m in zip(labels, mean):
        mea.append(np.mean(m))
        std.append(np.std(m))
        err.append(np.std(m) / np.sqrt(len(m)))
        ofs.write(l+",{0:.2f},{1:.2f},{2:.2f},{3:.2f}\n".format(np.mean(m)
                                                             , np.std(m)
                                                             , np.std(m) / np.sqrt(len(m))
                                                             , len(m) / L))
    ofs.close()
    
    #for plot
    fig, ax = pylab.subplots()
    fig.set_size_inches(5.6, 5.2)
    
    N = 8
    width = .6
    side_space = 0.5
    ind = np.arange(N)
    pylab.xlim([0, N + 2*side_space - (1-width)])
    pylab.ylim(glob_ylim)
    
    ax.bar(ind+side_space, mea, width, color='r', yerr=err, ecolor = 'k')
    
    ax.set_xticks(ind+width/2+side_space)
    ax.set_xticklabels([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5])
    
    ax.set_xlabel("Delay [s]", fontsize = 12)
    ax.set_ylabel("Reactiontime [ms]", fontsize = 12, rotation = "horizontal", horizontalalignment = "left")
    ax.yaxis.set_label_coords(x = 0, y = 1.03)
    ax.set_title("Delay-Reaction Keyboard", fontsize = 18, horizontalalignment = "left", y = 1.06, x = 0)
    pylab.savefig(name.split(".txt")[0]+".tiff")
    #end plot
    
def write_gest_delay_plot_data(name):
    ofs = open(name, "w")
    
    delay = [999, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    labels = ["1.0 s", "1.5 s", "2.0 s", "2.5 s", "3.0 s", "3.5 s", "4.0 s", "4.5 s"]
    
    mean = [[] for i in labels]
    
    for user in gest_data:
        for msm in user.valid_result:
            mean[delay.index([n for n in delay if n<msm["delay"]][-1])].append(msm["react"])
    
    L = float(0)
    
    for m in mean:
        L += len(m);
    
    mea = []
    std = []
    err = []
    
    for l, m in zip(labels, mean):
        mea.append(np.mean(m))
        std.append(np.std(m))
        err.append(np.std(m) / np.sqrt(len(m)))
        ofs.write(l+",{0:.2f},{1:.2f},{2:.2f},{3:.2f}\n".format(np.mean(m)
                                                             , np.std(m)
                                                             , np.std(m) / np.sqrt(len(m))
                                                             , len(m) / L))
    ofs.close()
    
    #for plot
    fig, ax = pylab.subplots()
    fig.set_size_inches(5.6, 5.2)
    
    N = 8
    width = .6
    side_space = 0.5
    ind = np.arange(N)
    pylab.xlim([0, N + 2*side_space - (1-width)])
    pylab.ylim(glob_ylim)
    
    ax.bar(ind+side_space, mea, width, color='r', yerr=err, ecolor = 'k')
    
    ax.set_xticks(ind+width/2+side_space)
    ax.set_xticklabels([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5])
    
    ax.set_xlabel("Delay [s]", fontsize = 12)
    ax.set_ylabel("Reactiontime [ms]", fontsize = 12, rotation = "horizontal", horizontalalignment = "left")
    ax.yaxis.set_label_coords(x = 0, y = 1.03)
    ax.set_title("Delay-Reaction Dataglove", fontsize = 18, horizontalalignment = "left", y = 1.06, x = 0)
    pylab.savefig(name.split(".txt")[0]+".tiff")
    #end plot

def write_n_t_plot_data(name):
    ofs = open(name, "w")
    
    
    labels = range(0, 30, 1)
    
    mean = [[] for i in labels]
    
    for user in gest_data:
        for msm, msm_i in zipi(user.valid_result):
            mean[msm_i].append(msm["react"])
    for user in key_data:
        for msm, msm_i in zipi(user.valid_result):
            mean[msm_i].append(msm["react"])
    
    L = float(0)
    L += len(mean[0]);
    
    mea = []
    std = []
    err = []
    
    for l, m in zip(labels, mean):
        mea.append(np.mean(m))
        std.append(np.std(m))
        err.append(np.std(m) / np.sqrt(len(m)))
        ofs.write(str(l+1)+",{0:.2f},{1:.2f},{2:.2f}\n".format(mea[-1]
                                                             , std[-1]
                                                             , err[-1]
                                                             ))
    ofs.close()
    
    #for plot
    fig, ax = pylab.subplots()
    fig.set_size_inches(8.6, 5.2)
    
    N = 30
    width = .6
    side_space = 0.5
    ind = np.arange(N)
    pylab.xlim([0, N + 2*side_space - (1-width)])
    pylab.ylim(glob_ylim)
    
    ax.bar(ind+side_space, mea, width, color='r', yerr=err, ecolor = 'k')
    
    ax.set_xticks(ind+width/2+side_space)
    ax.set_xticklabels(range(1, 31))
    
    ax.set_xlabel("Measurement Step", fontsize = 12)
    ax.set_ylabel("Reactiontime [ms]", fontsize = 12, rotation = "horizontal", horizontalalignment = "left")
    ax.yaxis.set_label_coords(x = 0, y = 1.03)
    ax.set_title("Duration-Reaction", fontsize = 18, horizontalalignment = "left", y = 1.06, x = 0)
    pylab.savefig(name.split(".txt")[0]+".tiff")
    #end plot

def write_fail_plot_data(name):
    ofs = open(name, "w")
    
    
    labels = ["wrong key", "wrong gest", "late key", "late gest"]
    
    mean = [[] for i in labels]
    
    late_gest = []
    fail_gest = []
    
    for user in gest_data:
        late_gest.append(len(user.late_result))
        fail_gest.append(len(user.wrong_result))
    
    late_key = []
    fail_key = []
    
    for user in key_data:
        late_key.append(len(user.late_result))
        fail_key.append(len(user.wrong_result))
    
    mean = []
    mean.append(fail_key)
    mean.append(fail_gest)
    mean.append(late_key)
    mean.append(late_gest)
    
    L = float(len(mean[-1]))
    
    mea = []
    std = []
    err = []
    per = []
    pererr = []
    
    for l, m in zip(labels, mean):
        mea.append(np.mean(m))
        std.append(np.std(m))
        err.append(np.std(m) / np.sqrt(len(m)))
        per.append(100*np.mean(m) / 30)
        pererr.append(100*np.std(m) / np.sqrt(len(m)) / 30)
        ofs.write(str(l)+",{0:.2f},{1:.2f},{2:.2f},{3:.2f}\n".format(mea[-1]
                                                             , std[-1]
                                                             , err[-1]
                                                             , per[-1]/100
                                                             ))
    ofs.close()
    
    mea = per
    err = pererr
    
    #for plot
    fig, ax = pylab.subplots()
    fig.set_size_inches(5.6, 5.2)
    
    N = 4
    width = .6
    side_space = 0.5
    ind = np.arange(N)
    pylab.xlim([0, N + 2*side_space - (1-width)])
    
    ax.bar(ind+side_space, mea, width, color='r', yerr=err, ecolor = 'k')
    
    ax.set_xticks(ind+width/2+side_space)
    ax.set_xticklabels(labels)
    
    ax.set_xlabel("Device", fontsize = 12)
    ax.set_ylabel("Percent [\%]", fontsize = 12, rotation = "horizontal", horizontalalignment = "left")
    ax.yaxis.set_label_coords(x = 0, y = 1.03)
    ax.set_title("Late/Wrong Input", fontsize = 18, horizontalalignment = "left", y = 1.06, x = 0)
    pylab.savefig(name.split(".txt")[0]+".tiff")
    #end plot

def convert_old(name):
    f = open(name, "r")
    d = f.read().splitlines() 
    f.close()
    
    user = name.split("/")[-1].split(".")[0]
    
    #=================== handle key ===================
    res = []
    
    delay = [int(nr) for nr in d[2].split(",")]
    keys = [k for k in d[3].split(", ")]
    react = [int(nr) for nr in d[4].split(",")]
    err = [eval(x) for x in d[5].split(";")]
    for dl, k, r in zip(delay, keys, react):
        res.append({'delay': dl, 'key': k, 'time': dl+r, 'pressed': k, 'react': r})
    
    for e in err:
        idx = e[0]
        dl = delay[idx]
        k = keys[idx]
        r = e[1]
        p = e[2]
        if r >= 0 and k == p:
            print("error, valid result detected {}".format(e))
        else:
            res.append({'delay': dl, 'key': k, 'time': dl+r, 'pressed': p, 'react': r})
        
    f = open(user + "_key-00.pickle", "wb")
    pickle.dump(res, f)
    f.close()
    
    #=================== handle gest ===================
    res = []
    
    delay = [int(nr) for nr in d[9].split(",")]
    keys = [k for k in d[10].split(", ")]
    react = [int(nr) for nr in d[11].split(",")]
    err = [eval(x) for x in d[12].split(";")]
    
    for dl, k, r in zip(delay, keys, react):
        res.append({'delay': dl, 'key': k, 'time': dl+r, 'pressed': k, 'react': r})
    
    for e in err:
        idx = e[0]
        dl = delay[idx]
        k = keys[idx]
        r = e[1]
        p = e[2]
        
        if r >= 0 and k == p:
            print("error, valid result detected {}".format(e))
        else:
            res.append({'delay': dl, 'key': k, 'time': dl+r, 'pressed': p, 'react': r})
    
    f = open(user + "_gest-00.pickle", "wb")
    pickle.dump(res, f)
    f.close()
    
    #=================== handle surv ===================
    surv = {}
    surv['precision'] = int(d[18][11:])-1
    surv['comment'] = d[17][12:]
    surv['confine'] = int(d[21][15:])-1
    surv['style']   = int(d[15][7:])-1
    surv['comfort'] = int(d[16][9:])-1
    surv['speed']   = int(d[22][25:])-1
    surv['overall'] = int(d[19][9:])-1
    surv['calibrate'] = int(d[23][11:])-1
    surv['dependable'] = int(d[20][17:])-1
    
    f = open(user + "_surv-00.pickle", "wb")
    pickle.dump(surv, f)
    f.close()
    

if __name__ == "__main__":
    print("generate_csv.py")
    #~ convert_old("../../Data_Glove/challange/data/kevin.dat")
    #~ convert_old("../../Data_Glove/challange/data/ricarda.dat")
    #~ convert_old("../../Data_Glove/challange/data/afrutig.dat")
    
    
    load_files()
    #~ path = abspath(__file__) + "/../data_out/"
    path = "/home/msk/Dropbox/sync/2014_data_glove/fig/"
    ending = ".txt"
    write_mean_plot_data(path + "fig_mean" + ending)
    write_survey_plot_data(path + "fig_survey" + ending)
    write_key_plot_data(path + "fig_key" + ending)
    write_gest_plot_data(path + "fig_gest" + ending)
    
    write_key_delay_plot_data(path + "fig_key_delay" + ending)
    write_gest_delay_plot_data(path + "fig_gest_delay" + ending)
    write_n_t_plot_data(path + "fig_n_t" + ending)
    write_fail_plot_data(path + "fig_fail" + ending)
