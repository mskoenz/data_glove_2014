#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    16.10.2014 09:23:50 CEST
# File:    drop_button_widget.py


from src.addon import *
from src.addon.qt5 import *
from .style import *

class Q2DropButtonWidget(QPushButton):
    def __init__(self, parent = None):
        super(Q2DropButtonWidget, self).__init__(parent)
        #=================== logic ===================
        self.id_ = 0
        self.init_ui()
    
    def init_ui(self):
        #=================== widgets ==================
        
        #=================== properties ===============
        
        #=================== connects =================
        
        #=================== layout ===================
        self.resize(btn_size, btn_size)
        
        #=================== finish ===================
        self.show()
    
    def mousePressEvent(self, e):
        pass
        
    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            return
        
        drag = QDrag(self)
        mimeData = QMimeData()
        
        itemData = QByteArray()
        dStr = QDataStream(itemData, QIODevice.WriteOnly)
        dStr << e.pos()
        dStr.writeInt32(self.id_/4)
        dStr.writeInt32(self.id_%4)
        
        mimeData.setData("point", itemData)
        drag.setMimeData(mimeData)
        dropAction = drag.exec_()
        
    def set_id(self, id):
        self.id_ = id
        
    def set_new_id(self, old_id, new_id):
        self.id_ = self.id_ - 4*old_id + 4*new_id;
