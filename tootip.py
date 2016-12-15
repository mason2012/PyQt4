#-*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class Tooltip(QtGui.QWidget):
  def __init__(self,parent=None):
    super(Tooltip,self).__init__(parent)
    self.resize(400,300)
    self.setWindowTitle('ToolTip')
    self.setWindowIcon(QtGui.QIcon('img/film.png'))
    self.setToolTip('This is <b>Tool Tip</b>')
    QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish',10))
    self.show()    
    
app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
sys.exit(app.exec_())