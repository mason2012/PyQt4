#-*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui

'''
#面向过程方式
app = QtGui.QApplication(sys.argv) 
widget = QtGui.QWidget()
widget.resize(200,250)
widget.setWindowTitle('simple example')
widget.show()

sys.exit(app.exec_())
'''
'''
#面向对象方式
class Simple(QtGui.QWidget):
  def __init__(self,parent=None):
    super(Simple,self).__init__(parent)
    self.widget = QtGui.QWidget()
    self.run()
  def run(self):
    self.widget.resize(200,300)
    self.widget.setWindowTitle('Simple Example')

app = QtGui.QApplication(sys.argv)
sim = Simple()
sim.show()
sys.exit(app.exec_())
'''

