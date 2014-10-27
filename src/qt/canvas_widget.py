#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    13.10.2014 15:29:12 CEST
# File:    canvas_widget.py

from src.addon import *
from src.addon.qt5 import *
from .style import *

from .selector_widget import *

class Q2CanvasWidget(QWidget):
    selectionChanged = pyqtSignal(int)
    
    def __init__(self, parent = None):
        super(Q2CanvasWidget, self).__init__(parent)
        #=================== logic ===================
        self.sel_ = {}
        self.sen_ = []
        
        self.init_ui()
    
    def init_ui(self):
        #=================== widgets ==================
        self.l = [[10], [100], [10], [100]]
        self.l2 = [[100], [200], [100], [200]]
        
        self.add_gesture(0, *self.l)
        self.add_gesture(0, *self.l2)
        #=================== properties ===============
        self.setAcceptDrops(True)
        self.setWindowTitle("canvas")
        
        #=================== connects =================
        
        #=================== layout ===================
        self.setGeometry(100, 100, 300, 300)
        self.setMinimumSize(256, 256)
        self.setMaximumSize(256, 256)
        
        pal = self.palette()
        pal.setColor(QPalette.Background, QColor(canvas_background))
        self.setAutoFillBackground(True);
        self.setPalette(pal);
        
        #=================== finish ===================
        self.show()
        
    def add_gesture(self, id, x_low, x_high, y_low, y_high):
        self.sel_[id] = Q2SelectorWidget(id, self)
        self.sel_[id].set_geometry(x_low, x_high, y_low, y_high)
        
        self.sel_[id].selected.connect(self.emitSelectionChanged)
    
        self.sel_[id].raise_()
        
    def set_sensor(sen):
        self.sen_ = sen
        
    def update_sensor(self):
        self.repaint()
        
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("point"):
            e.acceptProposedAction()
            
    def dropEvent(self, e):
        pos = e.pos()
        dif = QPoint()
        sel_id = 0
        btn_id = 0
    
        itemData = e.mimeData().data("point");
        dStr = QDataStream(itemData, QIODevice.ReadOnly)
        dStr >> dif
        sel_id = dStr.readInt32()
        btn_id = dStr.readInt32()
        
        self.sel_[sel_id].drop_handler(btn_id, pos)
        self.repaint()
        
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QColor(canvas_line))
        painter.setBrush(QBrush(canvas_brush))
        #~ painter.drawPolyline(sen_->data(), sen_->size());
        #~ painter.drawEllipse(sen_->front(), 2, 2);
        
    def swap(self, i1, i2):
        # swap color
        temp = self.sel_[i1].palette()
        self.sel_[i1].setPalette(self.sel_[i2].palette())
        self.sel_[i2].setPalette(temp)
        
        # swap only ids
        for b in self.sel_[i1]:
            b.set_new_id(sel_[i1].id_, sel_[i2].id_)

        for b in self.sel_[i2]:
            b.set_new_id(sel_[i2].id_, sel_[i1].id_)
            
        temp2 = self.sel_[i1].id_
        self.sel_[i1].id_ = self.sel_[i2].id_
        self.sel_[i2].id_ = temp2
        
        sel_[i1].swap(sel_[i2])
        self.update()
    
    def hide_gesture(self, id):
        self.sel_[id].hide()
    def show_gesture(self, id):
        self.sel_[id].show()
    def remove_gesture(self, id):
        del self.sel_[id]
    def update_gesture(self, id):
        self.sel_[id].update()
    def raise_gesture(self, id):
        if id != -1:
            self.sel_[id].raise_()
    
    def emitSelectionChanged(self, id):
        self.selectionChanged.emit(id)
