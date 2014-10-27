#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    16.10.2014 09:59:00 CEST
# File:    selector_widget.py

from src.addon import *
from src.addon.qt5 import *
from .style import *

from .drop_button_widget import *

class Q2SelectorWidget(QWidget):
    count = 0
    id = 0
    selected = pyqtSignal(int)
    def __init__(self, id, parent = None):
        super(Q2SelectorWidget, self).__init__(parent)
        #=================== logic ===================
        self.id_ = id
        self.init_ui(parent)
        
    def init_ui(self, parent):
        #=================== widgets ==================
        self.btn_ = [Q2DropButtonWidget(parent)
                   , Q2DropButtonWidget(parent)
                   , Q2DropButtonWidget(parent)
                   , Q2DropButtonWidget(parent)]
        #=================== properties ===============
        for b in self.btn_:
            b.set_id(4*__class__.id + __class__.count % 4)
            __class__.count += 1
        
        __class__.id += 1
            
        self.setMouseTracking(True)
        
        #=================== connects =================
        
        #=================== layout ===================
        
        #=================== finish ===================
        self.show()

    def drop_handler(self, id, p):
        self.selected.emit(self.id_)
        self.btn_[id].move(max(0, p.x()) - btn_size / 2, max(0, p.y()) - btn_size / 2)
    
        if id % 2 == 0:
            self.btn_[id + 1].move(self.btn_[id + 1].x(), self.btn_[id].y())
            self.btn_[(id + 4 - 1) % 4].move(self.btn_[id].x(), self.btn_[(id + 4 - 1) % 4].y())
        else:
            self.btn_[(id + 1) % 4].move(self.btn_[id].x(), self.btn_[(id + 1) % 4].y())
            self.btn_[id - 1].move(self.btn_[id - 1].x(), self.btn_[id].y())
        
        self.x_high_[0] = 0
        self.y_high_[0] = 0
        self.x_low_[0] = 255
        self.y_low_[0] = 255
        
        for b in self.btn_:
            self.x_high_[0] = max(self.x_high_[0], b.x())
            self.y_high_[0] = max(self.y_high_[0], b.y())
            self.x_low_[0] = min(self.x_low_[0], b.x())
            self.y_low_[0] = min(self.y_low_[0], b.y())
        
        self.x_high_[0] += btn_size;
        self.y_high_[0] += btn_size;
        
        self.setGeometry(self.x_low_[0], self.y_low_[0], self.x_high_[0] - self.x_low_[0], self.y_high_[0] - self.y_low_[0]);
        
    def set_geometry(self, x_low, x_high, y_low, y_high):
        self.x_low_ = x_low;
        self.x_high_ = x_high;
        self.y_low_ = y_low;
        self.y_high_ = y_high;
        
        self.update()
        
        def get_color(i):
            return "#FF0000"
        
        color = QColor(get_color(self.id_));
        color.setAlphaF(.2);
        
        pal = self.palette()
        pal.setColor(QPalette.Background, color)
        self.setAutoFillBackground(True)
        self.setPalette(pal);
        
    def raise_(self):
        super(Q2SelectorWidget, self).raise_();
        for b in self.btn_:
            b.raise_()
        
    def lower_(self):
        super(Q2SelectorWidget, self).lower_();
        for b in self.btn_:
            b.lower_()
            
    def hide(self):
        super(Q2SelectorWidget, self).hide();
        for b in self.btn_:
            b.hide()
        
    def show(self):
        super(Q2SelectorWidget, self).show();
        for b in self.btn_:
            b.show()
        
    def update(self):
        self.btn_[0].move(self.x_low_[0] , self.y_low_[0]);
        self.btn_[1].move(self.x_high_[0] - btn_size, self.y_low_[0]);
        self.btn_[2].move(self.x_high_[0] - btn_size, self.y_high_[0] - btn_size);
        self.btn_[3].move(self.x_low_[0], self.y_high_[0] - btn_size);
        self.setGeometry(self.x_low_[0], self.y_low_[0], self.x_high_[0] - self.x_low_[0], self.y_high_[0] - self.y_low_[0])
        
    def mousePressEvent(self, e):
        if e.buttons() == Qt.RightButton:
            self.lower()
    
        if(e.buttons() == Qt.LeftButton):
            self.raise_()
            self.selected.emit(self.id_)
        
    def enterEvent(self, e):
        pass
