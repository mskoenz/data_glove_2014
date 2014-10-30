#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    30.10.2014 11:06:19 CET
# File:    ranking_widget.py

from src.ranking import *

from src.addon import *
from src.addon.qt5 import *

class Q2ranking(QWidget):
    def __init__(self, parent = None):
        super(Q2ranking, self).__init__(parent)
        #=================== logic ===================
        self.ranking = generate_ranking()
        self.user_name = "nobody"
        #~ self.init_ui()
        
    def init_ui(self):
        #=================== widgets ==================
        self.kb_table = QTableWidget(len(self.ranking[0]), 2, self)
        self.dg_table = QTableWidget(len(self.ranking[1]), 2, self)
        #=================== properties ===============
        self.kb_table.setHorizontalHeaderLabels(["user", "keyboard"])
        self.dg_table.setHorizontalHeaderLabels(["user", "data glove"])
        
        for u, u_i in zipi(self.ranking[0]):
            name = QTableWidgetItem(u[0])
            mean = QTableWidgetItem("{:.1f} ms".format(u[1]))
            
            if u[0] == self.user_name:
                name.setForeground(QBrush(Qt.red))
                mean.setForeground(QBrush(Qt.red))
            
            self.kb_table.setItem(u_i, 0, name)
            self.kb_table.setItem(u_i, 1, mean)
        
        for u, u_i in zipi(self.ranking[1]):
            name = QTableWidgetItem(u[0])
            mean = QTableWidgetItem("{:.1f} ms".format(u[1]))
            
            if u[0] == self.user_name:
                name.setForeground(QBrush(Qt.red))
                mean.setForeground(QBrush(Qt.red))
            
            self.dg_table.setItem(u_i, 0, name)
            self.dg_table.setItem(u_i, 1, mean)
        #=================== connects =================
        
        #=================== layout ===================
        grid = QGridLayout()
        grid.addWidget(self.kb_table , 1, 1, 1, 1)
        grid.addWidget(self.dg_table , 1, 2, 1, 1)
        self.setLayout(grid)
        
        #=================== finish ===================
        self.show()
    
    def set_current_user(self, name, kb_react, dg_react):
        self.user_name = name
        
        kb = kb_react.evaluate["mean"]
        dg = dg_react.evaluate["mean"]
        
        self.ranking[0].append([name, kb])
        self.ranking[1].append([name, dg])
        
        self.ranking = sorted(self.ranking[0], key = lambda x: x[1]), sorted(self.ranking[1], key = lambda x: x[1])
        self.init_ui()
