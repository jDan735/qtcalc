from PyQt5 import QtWidgets
import qtcalc
#from aboutqt import aboutqt
#from aboutapp import aboutapp
#from __init__ import __version__

import sys


class QtCalc(QtWidgets.QMainWindow, qtcalc.Ui_MainWindow):
    def __init__(self):
        super(QtCalc, self).__init__()
        self.setupUi(self)

#     def about_qt(self):
#         modal = AboutQt()
#         modal.exec_()

#     def about_app(self):
#         modal = AboutApp()
#         modal.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtCalc()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
