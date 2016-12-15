#-*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
  def __init__(self,parent=None):
    super(Icon,self).__init__(parent)
    self.widget = QtGui.QWidget()
    self.run()
  def run(self):
    self.widget.resize(100,300)
    self.widget.setWindowTitle('Icon')
    self.widget.setWindowIcon('img/Aniscree.ico')
    self.show()
    
app = QtGui.QApplicatioin(sys.argv)
icon = Icon()
sys.exit(app.exec_)