#-*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(200,250)
widget.setWindowTitle('simple example')
widget.show()

sys.exit(app.exec_())