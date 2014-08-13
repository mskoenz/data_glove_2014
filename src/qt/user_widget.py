#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    13.08.2014 18:32:52 CEST
# File:    user_widget.py

import qt.language as lg

from src.addon import *
from src.addon.qt5 import *
from src.userbase import *

class Q2user(QWidget):
    done = pyqtSignal()
    def __init__(self, parent = None):
        """
        Constructor generates a default user class.
        """
        super(Q2user, self).__init__(parent)
        
        self.gender_list = lg.user_gender
        self.label = lg.user_label
        self.userbase = userbase()
        self.ub_name = "main"
        self.userbase.load(self.ub_name)
        
        self.init_ui()
    
    def init_ui(self):
        """
        Initializes all widgets and sets up the layout.
        """
        #=================== widgets ===================
        self.fname = QLineEdit(self)
        self.lname = QLineEdit(self)
        self.gender = QComboBox(self)
        self.tag = QLineEdit(self)
        self.study = QLineEdit(self)
        self.age = QLineEdit(self)
        self.load_btn = QPushButton(lg.user_load, self)
        self.done_btn = QPushButton(lg.user_done, self)
        #=================== properties ===================
        self.gender.addItems(self.gender_list)
        self.age.setInputMask("99")
        
        #=================== connects ===================
        self.done_btn.pressed.connect(self.done_handler)
        self.load_btn.pressed.connect(self.load)
        
        #=================== layout ===================
        grid = QGridLayout()
        
        for l, i_l in zipi(self.label):
            lbl = QLabel(l, self)
            grid.addWidget(lbl, i_l + 1, 1, 1, 1)
        
        grid.addWidget(self.fname,  1, 2, 1, 1)
        grid.addWidget(self.lname, 2, 2, 1, 1)
        grid.addWidget(self.gender,     3, 2, 1, 1)
        grid.addWidget(self.tag,        4, 2, 1, 1)
        grid.addWidget(self.study,      5, 2, 1, 1)
        grid.addWidget(self.age,        6, 2, 1, 1)
        grid.addWidget(self.load_btn,   7, 1, 1, 1)
        grid.addWidget(self.done_btn,   7, 2, 1, 1)
        
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(3, 1)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(8, 1)
        
        self.setLayout(grid)
        #=================== finish ===================
        self.show()
    
    def load(self):
        tag = str(self.tag.text())
        if tag in self.userbase.all_user:
            user = self.userbase[tag]
            self.fname.setText(user["fname"])
            self.lname.setText(user["lname"])
            self.gender.setCurrentIndex(self.gender_list.index(user["gender"]))
            self.study.setText(user["study"])
            self.age.setText(user["age"])
        else:
            self.fname.setText("")
            self.lname.setText("")
            self.gender.setCurrentIndex(0)
            self.study.setText("")
            self.age.setText("")
        
    def done_handler(self):
        if self.fname.text() == "" or self.lname.text() == "" or self.tag.text() == "" or self.study.text() == "" or self.age.text() == "":
            m = QMessageBox()
            m.setText(lg.user_answer_all)
            m.exec_()
            return
        
        d = {}
        d["fname"] =  str(self.fname.text())
        d["lname"] =  str(self.lname.text())
        d["tag"] =    str(self.tag.text())
        d["study"] =  str(self.study.text())
        d["age"] =    str(self.age.text())
        d["gender"] = str(self.gender.currentText())
        
        self.userbase.add_user(**d)
        self.userbase.write(self.ub_name)
        
        print("Q2user done")
        self.done.emit()
