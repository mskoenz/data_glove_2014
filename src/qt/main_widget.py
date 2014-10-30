#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    13.08.2014 17:38:40 CEST
# File:    main_widget.py

import qt.language as lg

from .reaction_widget import *
from .user_widget import *
from .survey_widget import *
from .calibrate_widget import *
from .ranking_widget import *

from src.addon import *
from src.addon.qt5 import *


class Q2main(QMainWindow):
    def center_widget(self, w):
        grid = QGridLayout()
        grid.addWidget(w, 1, 1, 1, 1)
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(2, 1)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(2, 1)
        temp = QWidget(self)
        temp.setLayout(grid)
        return temp
    
    def __init__(self, parent = None):
        super(Q2main, self).__init__(parent)
        #=================== logic ===================
        self.key = ["z", "u", "i", "o", "p"]
        self.delay = drange(1000, 5000, 100)
        self.n_trial = 5
        self.n_msm = 30
        
        #~ self.key = ["z", "p"]
        #~ self.delay = drange(500, 1500, 100)
        #~ self.n_trial = 2
        #~ self.n_msm = 5
        
        self.user_name = "mrx"
        self.init_ui()
        
        self.stage_user()
    
    def init_ui(self):
        #=================== widgets ==================
        self.tab = QTabWidget(self)
        self.user = Q2user(self)
        self.cali = Q2calibrate(self)
        self.key_msm = Q2reaction(self)
        self.gest_msm = Q2reaction(self)
        self.survey = Q2survey(self)
        #~ self.ranking = Q2ranking(self)
        #~ self.end = QLabel("", self)
        self.end = Q2ranking(self)
        #=================== properties ===============
        #~ self.end.setPixmap(QPixmap(abspath(__file__) + "/../png/cookie.png").scaled(200,200,Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        
        #=================== connects =================
        self.user.done.connect(self.stage_keyboard)
        self.key_msm.done.connect(self.stage_calibrate)
        self.cali.done.connect(self.stage_glove)
        self.gest_msm.done.connect(self.stage_survey)
        self.survey.done.connect(self.stage_done)
        self.tab.currentChanged.connect(self.tab_change)
        
        #=================== layout ===================
        self.tab.addTab(self.user, lg.main_user)
        self.tab.addTab(self.key_msm, lg.main_keyboard)
        self.tab.addTab(self.cali, lg.main_calibrate)
        self.tab.addTab(self.gest_msm, lg.main_glove)
        self.tab.addTab(self.survey, lg.main_survey)
        self.tab.addTab(self.center_widget(self.end), lg.main_done)
        
        #=================== finish ===================
        self.setCentralWidget(self.tab)
        self.setGeometry(10, 10, 600, 200)
        self.show()
    
    def stage_user(self):
        CYAN("user stage")
        self.tab.setCurrentIndex(0)
        
    def stage_keyboard(self):
        CYAN("keyboard stage")
        self.user_name = self.user.tag.text()
        self.key_msm.set_react(self.user_name, "key", self.key, self.delay, self.n_trial, self.n_msm)
        
        self.tab.setCurrentIndex(1)
    
    def stage_calibrate(self):
        CYAN("calibrate stage")
        self.tab.setCurrentIndex(2)
        
    def stage_glove(self):
        CYAN("glove stage")
        self.gest_msm.set_react(self.user_name, "gest", self.key, self.delay, self.n_trial, self.n_msm)
        self.tab.setCurrentIndex(3)
        
    def stage_survey(self):
        CYAN("survey stage")
        self.survey.user = self.user_name
        self.tab.setCurrentIndex(4)
        
    def stage_done(self):
        CYAN("done stage")
        self.tab.setCurrentIndex(5)
    
    def tab_change(self, i):
        if i == 2:
            self.cali.enter_handle()
        else:
            self.cali.timer.stop()
            if i == 5:
                self.end.set_current_user(self.user_name, self.key_msm.react, self.gest_msm.react)
        
