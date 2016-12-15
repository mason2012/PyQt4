#-*- coding:utf-8 -*-
import sys, os
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
  def __init__(self,parent=None):
    super(Icon,self).__init__(parent)
    self.run()
  def run(self):
    self.resize(400,500)
    self.setWindowTitle('Icon')
    self.setWindowIcon(QtGui.QIcon('img/film.png'))
    self.show()
    
app = QtGui.QApplication(sys.argv)
icon = Icon()
sys.exit(app.exec_())