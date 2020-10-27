from PyQt5 import QtWidgets

import qtcalc
import aboutqt
import aboutapp
from __init__ import __version__

import sys


def optimize(number):
    if int(number) == float(number):
        return number


class QtCalc(QtWidgets.QMainWindow, qtcalc.Ui_MainWindow):
    def __init__(self):
        super(QtCalc, self).__init__()
        self.setupUi(self)

        self.actionAbout_QT.triggered.connect(self.about_qt)
        self.actionAbout_QtCalc.triggered.connect(self.about_app)

        self.pushButton_0.clicked.connect(lambda: self.enter_number("0"))
        self.pushButton_1.clicked.connect(lambda: self.enter_number("1"))
        self.pushButton_2.clicked.connect(lambda: self.enter_number("2"))
        self.pushButton_3.clicked.connect(lambda: self.enter_number("3"))
        self.pushButton_4.clicked.connect(lambda: self.enter_number("4"))
        self.pushButton_5.clicked.connect(lambda: self.enter_number("5"))
        self.pushButton_6.clicked.connect(lambda: self.enter_number("6"))
        self.pushButton_7.clicked.connect(lambda: self.enter_number("7"))
        self.pushButton_8.clicked.connect(lambda: self.enter_number("8"))
        self.pushButton_9.clicked.connect(lambda: self.enter_number("9"))

        self.pushButton_div.clicked.connect(lambda: self.enter_symbol("/"))
        self.pushButton_mul.clicked.connect(lambda: self.enter_symbol("*"))
        self.pushButton_min.clicked.connect(lambda: self.enter_symbol("-"))
        self.pushButton_sum.clicked.connect(lambda: self.enter_symbol("+"))
        self.pushButton_dot.clicked.connect(lambda: self.enter_symbol("."))

        self.pushButton_proc.clicked.connect(self.proc)
        self.pushButton_eval.clicked.connect(self.eval_)
        self.pushButton_clear.clicked.connect(self.clear)

    def about_qt(self):
        modal = AboutQt()
        modal.exec_()

    def about_app(self):
        modal = AboutApp()
        modal.exec_()

    def proc(self):
        try:
            proc = 100 / float(self.lineEdit.text())
            self.lineEdit.setText(str(optimize(proc)))
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
            self.lineEdit.setText(str(optimize(number)))
        except:
            self.lineEdit.setText("Error")

    def clear(self):
        self.lineEdit.setText("0")


class AboutApp(QtWidgets.QDialog, aboutapp.Ui_Dialog):
    def __init__(self):
        super(AboutApp, self).__init__()
        self.setupUi(self)

        self.label_2.setText(f'<span style="font-size:24pt; font-weight:496;"><span style="color:#41cd52">Qt</span>SCP</span> <span style="font-size:18pt; font-weight:400;">{__version__}</span>')
        self.pushButton.clicked.connect(self.close)


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


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtCalc()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
