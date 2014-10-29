#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    13.08.2014 15:31:38 CEST
# File:    reaction_widget.py

import qt.language as lg

from src.reaction import *

from src.addon import *
from src.addon.qt5 import *


class Q2reaction(QWidget):
    done = pyqtSignal()
    def __init__(self, parent = None):
        """
        Constructor generates a default reaction class.
        """
        super(Q2reaction, self).__init__(parent)
        
        self.set_react("mrx", "key", ['z'], [.5], 2, 3)
        self.trial_text = lg.react_trial
        self.msm_text = lg.react_measurement
        self.done_text = lg.react_done
        self.init_ui()
    
    def init_ui(self):
        """
        Initializes all widgets and sets up the layout.
        """
        #=================== widgets ===================
        self.lbl = QLabel(self)
        self.progress = QProgressBar(self)
        self.start_btn = QPushButton(self.trial_text, self)
        self.done_btn = QPushButton("ok", self)
        
        self.timer = QTimer(self)
        
        #=================== properties ===================
        self.setup()
        self.timer.setSingleShot(True)
        
        #=================== connects ===================
        self.start_btn.clicked.connect(self.start_msm)
        self.timer.timeout.connect(self.timer_timeout)
        self.done_btn.pressed.connect(self.done_handler)
        
        #=================== layout ===================
        grid = QGridLayout()
        grid.addWidget(self.lbl      , 1,1,1,2)
        grid.addWidget(self.progress , 2,1,1,2)
        grid.addWidget(self.start_btn, 3,1,1,1)
        grid.addWidget(self.done_btn   , 3,2,1,1)
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(3, 1)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(4, 1)
        
        self.setLayout(grid)
        
        #=================== finish ===================
        self.show()
    
    def setup(self):
        self.start_btn.setEnabled(True)
        self.done_btn.setEnabled(False)
        self.set_label("default.png")
        self.progress.setValue(0)
    
    def set_react(self, user, modus, key, delay, n_trial, n_msm):
        self.user = user
        self.modus = modus #"key" or "gest"
        self.key = key
        self.delay = delay
        self.n_trial = n_trial
        self.n_msm = n_msm
    
    def set_label(self, name):
        png_dir = abspath(__file__) + "/../png/"
        self.lbl.setPixmap(QPixmap(png_dir + name).scaled(200,200,Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.lbl.repaint()
        QApplication.processEvents()
    
    def start_msm(self):
        self.setFocus()
        self.start_btn.setEnabled(False)
        if self.start_btn.text() == self.trial_text:
            self.react = reaction(self.key, self.delay, self.n_trial)
        elif self.start_btn.text() == self.msm_text:
            self.react = reaction(self.key, self.delay, self.n_msm)
        
        self.take_sample()
    
    def take_sample(self):
        print("take sample {} of {}".format(self.react.current_msm + 1, self.react.n_msm))
        p = self.react.current_msm * 100.0 / self.react.n_msm
        self.progress.setValue(p)
        
        self.cur_key, delay = self.react.start()
        self.timer.start(delay)
        self.set_label("wait.png")
        
    def timer_timeout(self):
        self.set_label(self.cur_key + "_" + self.modus + ".png")
        
    def keyPressEvent(self, e):
        if self.start_btn.isEnabled() == True:
            return
        
        state = self.react.stop(e.text())
        if state != "valid":
            self.set_label("fail.png")
            time.sleep(1.5)
        
        if not self.react.done:
            self.take_sample()
        else:
            self.progress.setValue(100)
            print(self.react.evaluate)
            self.set_label("done.png")
            self.done_btn.setEnabled(True)
    
    def done_handler(self):
        if self.start_btn.text() == self.trial_text:
            self.start_btn.setText(self.msm_text)
            self.setup()
            return
        elif self.start_btn.text() == self.msm_text:
            self.start_btn.setText(self.done_text)
            self.react.write(self.user + "_" + self.modus)
        
        print("Q2reaction done")
        self.done.emit()
