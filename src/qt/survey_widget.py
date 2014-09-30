#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    13.08.2014 19:21:43 CEST
# File:    survey_widget.py

import qt.language as lg

from src.addon import *
from src.addon.qt5 import *
from src.survey import *

class Q2survey(QWidget):
    done = pyqtSignal()
    def __init__(self, parent = None):
        """
        Constructor generates a default surey class.
        """
        super(Q2survey, self).__init__(parent)
        self.survey = survey()
        self.label = self.survey.label
        self.user = "mrx"
        self.init_ui()
    
    #=================== special dynamic method creator ===================
    def add_fct(self, i_l):
        l = self.label[i_l]
        quali = eval("lg.survey_quali_" + l)
        quali.insert(1, lg.survey_hedger + quali[0])
        quali.insert(-1, lg.survey_hedger + quali[-1])
        setattr(Q2survey, "f_" + l, lambda self, x: self.quali[i_l].setText(eval("lg.survey_quali_" + l)[x]))
        
    def init_ui(self):
        """
        Initializes all widgets and sets up the layout.
        """
        #=================== widgets ===================
        
        self.slider = [QSlider(self) for l in self.label]
        self.qlabel = [QLabel(self) for l in self.label]
        self.quali = [QLabel(self) for l in self.label]
        self.done_btn = QPushButton(lg.user_done, self)
        self.comment = QTextEdit(self)
        
        
        #=================== properties ===================
        for l, i_l in zipi(self.label):
            self.slider[i_l].setOrientation(Qt.Horizontal)
            self.slider[i_l].setTickInterval(1)
            self.slider[i_l].setRange(0, 4)
            self.qlabel[i_l].setText(eval("lg.survey_" + l))
            self.quali[ i_l].setText(eval("lg.survey_quali_" + l + "[0]"))
            self.qlabel[i_l].setToolTip(eval("lg.survey_desc_" + l))
        
        self.comment.setPlaceholderText(lg.survey_comment)
        
        #=================== connects ===================
        self.done_btn.pressed.connect(self.done_handler)
        for l, i_l in zipi(self.label):
            self.add_fct(i_l)
            self.slider[i_l].valueChanged.connect(eval("self.f_" + l))
        
        #=================== layout ===================
        grid = QGridLayout()
        
        for l, i_l in zipi(self.label):
            grid.addWidget(self.qlabel[i_l],     i_l + 1, 1, 1, 1)
            grid.addWidget(self.slider[i_l],     i_l + 1, 2, 1, 1)
            grid.addWidget(self.quali[i_l],      i_l + 1, 3, 1, 1)
        
        grid.addWidget(self.comment,    len(self.label) + 1, 1, 1, 3)
        grid.addWidget(self.done_btn,   len(self.label) + 2, 3, 1, 1)
        
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(4, 1)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(len(self.label) + 3, 1)
        
        self.setLayout(grid)
        #=================== finish ===================
        self.show()
    
    def done_handler(self):
        d = {}
        
        for l, i_l in zipi(self.label):
            d[l] = self.slider[i_l].value()
        
        d["comment"] = self.comment.toPlainText()
        self.survey.set_data(**d)
        self.survey.write(self.user + "_surv")
        print("Q2survey done")
        self.done.emit()
