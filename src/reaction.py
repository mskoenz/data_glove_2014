#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    13.08.2014 11:44:44 CEST
# File:    reaction.py

from src_import import *

class reaction(object):
    def __init__ (self, key, delay, n_msm):
        """
        Constructor of the reaction class. key is a list of keys (e.g. ["a", "b", "c"]) and delay a list of delays (e.g. [1.0, 2.0, 3.5]). N_msm specifies how many valid measurements need to be taken.
        """
        self.key = key
        self.delay = delay
        self.n_msm = n_msm
        self.clear()
        
    def start(self):
        """
        A function that returns a random key from self.key and a random delay in self.delay and appends the pair in self.hist. It also starts the clock.
        """
        key = random.choice(self.key)
        delay = int(random.choice(self.delay) * 1000)
        self.hist.append({"key": key, "delay": delay})
        self.begin = time.time()
        return key, delay
    
    def wait(self):
        """
        Lets the cpu sleep for the chosen random delay.
        """
        time.sleep(self.hist[-1]["delay"]/1000.0 - (time.time() - self.begin))
    
    def stop(self, pressed):
        """
        Stops the clock and registers the pressed key (pressed), as well as the reaction time (react) and time since start (time)
        """
        self.end = time.time()
        rt = int((self.end-self.begin) * 1000)
        
        key = self.hist[-1]["key"]
        delay = self.hist[-1]["delay"]
        
        if rt < delay:
            WARNING("key {} was pressed {} ms to early".format(pressed, delay - rt))
        elif pressed != key:
            WARNING("key {} was pressed instead of key {}".format(pressed, key))
        
        self.hist[-1]["time"] = rt
        self.hist[-1]["react"] = rt - delay
        self.hist[-1]["pressed"] = pressed
        
        if self.hist[-1] in self.wrong_result:
            return "wrong"
        if self.hist[-1] in self.early_result:
            return "early"
        
        self.current_msm += 1
        return "valid"
        
    @property
    def result(self):
        """
        Just returns all the measurement results.
        """
        return self.hist
    
    @property
    def valid_result(self):
        """
        Just returns all the valid measurement results.
        """
        return [msm for msm in self.hist if msm["pressed"] == msm["key"] and msm["react"] >= 0]
    
    @property
    def early_result(self):
        """
        Just returns all the late measurement results.
        """
        return [msm for msm in self.hist if msm["react"] < 0]
    
    @property
    def late_result(self):
        """
        Just returns all the late correct measurement results.
        """
        return [msm for msm in self.hist if msm["pressed"] == msm["key"] and msm["react"] >= 1500]
    
    @property
    def wrong_result(self):
        """
        Just returns all the wrong measurement results.
        """
        return [msm for msm in self.hist if msm["pressed"] != msm["key"] and msm["react"] >= 0]
    
    @property
    def done(self):
        """
        Returns True if the count of n_msm is reached.
        """
        if self.n_msm <= self.current_msm:
            return True
        return False
    
    @property
    def evaluate(self):
        """
        Returns a dictionary with the most important data.
        """
        res = {}
        delay = [msm["react"] for msm in self.valid_result]
        
        res["mean"] = np.mean(delay)
        res["max"] = np.max(delay)
        res["min"] = np.min(delay)
        res["valid"] = len(self.valid_result)
        res["early"] = len(self.early_result)
        res["late"] = len(self.late_result)
        res["wrong"] = len(self.wrong_result)
        
        return res
    
    def write(self, name):
        """
        Pickles the results into a file called name.pickle in the folder ./../data.
        This function never overwrites other files.
        """
        path = abspath(__file__) + "/../data/"
        
        nr = 0
        while readable(path + name + "-{:0>2}.pickle".format(nr)):
            nr += 1
        
        GREEN("written react-data to " + name + "-{:0>2}.pickle".format(nr))
        
        f = open(path + name + "-{:0>2}.pickle".format(nr), "wb")
        pickle.dump(self.result, f)
        f.close()
    
    def clear(self):
        """
        Resets the class and removes all measurements.
        """
        self.hist = []
        self.current_msm = 0
    
