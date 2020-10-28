from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import QEvent

import qtcalc
import aboutqt
import aboutapp

try:
    from __init__ import __version__
except:
    from . import __version__

import sys


def optimize(number):
    if int(number) == float(number):
        return int(number)
    else:
        return float(number)


class QtCalc(QtWidgets.QMainWindow, qtcalc.Ui_MainWindow):
    def __init__(self):
        super(QtCalc, self).__init__()
        self.setupUi(self)

        self.actionAbout_QT.triggered.connect(self.about_qt)
        self.actionAbout_QtCalc.triggered.connect(self.about_app)

        for num in range(10):
            num = str(num)
            btn = self.__dict__[f"pushButton_{num}"]
            btn.clicked.connect(lambda checked=None, x=num: self.enter_number(x))

        self.pushButton_div.clicked.connect(lambda: self.enter_symbol("/"))
        self.pushButton_mul.clicked.connect(lambda: self.enter_symbol("*"))
        self.pushButton_min.clicked.connect(lambda: self.enter_symbol("-"))
        self.pushButton_sum.clicked.connect(lambda: self.enter_symbol("+"))
        self.pushButton_dot.clicked.connect(lambda: self.enter_symbol("."))

        self.pushButton_proc.clicked.connect(self.proc)
        self.pushButton_eval.clicked.connect(self.eval_)
        self.pushButton_clear.clicked.connect(self.clear)

    def keyPressEvent(self, event):
        for num in range(10):
            if event.key() == QtCore.Qt.__dict__[f"Key_{num}"]:
                self.__dict__[f"pushButton_{num}"].click()

        if event.key() == QtCore.Qt.Key_Percent:
            self.pushButton_proc.click()

        elif event.key() == QtCore.Qt.Key_Plus:
            self.pushButton_sum.click()

        elif event.key() == QtCore.Qt.Key_Return or \
             event.key() == QtCore.Qt.Key_Enter:
            self.pushButton_eval.click()

        elif event.key() == QtCore.Qt.Key_Plus:
            self.pushButton_sum.click()

        elif event.key() == 47:
            self.pushButton_div.click()

        elif event.key() == QtCore.Qt.Key_Minus:
            self.pushButton_min.click()

        elif event.key() == 42:
            self.pushButton_mul.click()

    def about_qt(self):
        modal = AboutQt()
        modal.exec_()

    def about_app(self):
        modal = AboutApp()
        modal.exec_()

    def proc(self):
        try:
            proc = 100 / float(self.lineEdit.text())
            self.lineEdit.setText(str(round(optimize(proc), 3)))
        except:
            self.lineEdit.setText("Error")

    def enter_symbol(self, symbol):
        if self.lineEdit.text() == "Error":
            self.lineEdit.setText("0")
        else:
            self.lineEdit.setText(self.lineEdit.text() + symbol)

    def enter_number(self, number):
        if self.lineEdit.text() == "0":
            self.lineEdit.setText("")

        if self.lineEdit.text() == "Error":
            self.lineEdit.setText("")

        self.lineEdit.setText(self.lineEdit.text() + number)

    def eval_(self):
        try:
            number = eval(self.lineEdit.text())
            self.lineEdit.setText(str(round(optimize(number), 3)))
        except:
            self.lineEdit.setText("Error")

    def clear(self):
        self.lineEdit.setText("0")


class AboutApp(QtWidgets.QDialog, aboutapp.Ui_Dialog):
    def __init__(self):
        super(AboutApp, self).__init__()
        self.setupUi(self)

        self.label_2.setText(f'<span style="font-size:24pt; font-weight:496;"><span style="color:#41cd52">Qt</span>Calc</span> <span style="font-size:18pt; font-weight:400;">{__version__}</span>')
        self.pushButton.clicked.connect(self.close)

    def keyPressEvent(self, event):
        if event.key() == 16777220:       # key =
            self.close()


class AboutQt(QtWidgets.QDialog, aboutqt.Ui_Dialog):
    def __init__(self):
        super(AboutQt, self).__init__()
        self.setupUi(self)

        try:
            import pkg_resources
            qt_version = pkg_resources.get_distribution("PyQt5").version
        except:
            qt_version = "5"

        self.label_2.setText(f'<span style="font-size:24pt; font-weight:400;"><span style="color:#41cd52;">Qt</span> {qt_version}')
        self.pushButton.clicked.connect(self.close)

    def keyPressEvent(self, event):
        if event.key() == 16777220:       # key =
            self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtCalc()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
