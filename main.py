import Algebra
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

NATURAL = 0
INTEGER = 1
RATIONAL = 2
POLYNOM = 3

INPUT_ERROR = 0

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.currentIndex = NATURAL

        self.setObjectName("self")
        self.resize(500, 600)
        self.setMinimumSize(QtCore.QSize(500, 600))
        self.setMaximumSize(QtCore.QSize(500, 700))

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -1, 500, 580))
        self.stackedWidget.setMinimumSize(QtCore.QSize(500, 580))
        self.stackedWidget.setMaximumSize(QtCore.QSize(500, 580))
        self.stackedWidget.setObjectName("stackedWidget")

        self.createNaturalPage()
        self.createIntegerPage()
        self.createRationalPage()
        self.createPolynomPage()
        self.currentLineEdit = self.n_input

        self.createMenuBar()

        self.setActions()

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(self.currentIndex)
        QtCore.QMetaObject.connectSlotsByName(self)

    def createNaturalPage(self):
        self.Natural = QtWidgets.QWidget()
        self.Natural.setObjectName("Natural")

        bold_font = QtGui.QFont()
        bold_font.setPointSize(11)
        bold_font.setBold(True)
        bold_font.setWeight(75)

        label_font = QtGui.QFont()
        label_font.setPointSize(14)
        label_font.setBold(False)
        label_font.setWeight(50)
        label_font.setStrikeOut(False)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.n_input = QtWidgets.QLineEdit(self.Natural)
        self.n_input.setGeometry(QtCore.QRect(50, 30, 400, 81))
        self.n_input.setObjectName("n_input")
        self.n_label = QtWidgets.QLabel(self.Natural)
        self.n_label.setGeometry(QtCore.QRect(50, 120, 211, 21))
        self.n_label.setFont(label_font)
        self.n_label.setObjectName("n_label")
        self.n_add = QtWidgets.QPushButton(self.Natural)
        self.n_add.setGeometry(QtCore.QRect(50, 160, 50, 40))
        self.n_add.setFont(bold_font)
        self.n_add.setObjectName("n_add")
        self.n_incr = QtWidgets.QPushButton(self.Natural)
        self.n_incr.setGeometry(QtCore.QRect(350, 240, 100, 45))
        self.n_incr.setObjectName("n_incr")
        self.sub = QtWidgets.QPushButton(self.Natural)
        self.sub.setGeometry(QtCore.QRect(140, 160, 50, 40))
        self.sub.setFont(bold_font)
        self.sub.setObjectName("sub")
        self.n_cmp = QtWidgets.QPushButton(self.Natural)
        self.n_cmp.setGeometry(QtCore.QRect(50, 240, 100, 45))
        self.n_cmp.setObjectName("n_cmp")
        self.n_is_zero = QtWidgets.QPushButton(self.Natural)
        self.n_is_zero.setGeometry(QtCore.QRect(200, 240, 100, 45))
        self.n_is_zero.setObjectName("n_is_zero")
        self.n_mul_d = QtWidgets.QPushButton(self.Natural)
        self.n_mul_d.setGeometry(QtCore.QRect(200, 320, 100, 45))
        self.n_mul_d.setObjectName("n_mul_d")
        self.n_mod = QtWidgets.QPushButton(self.Natural)
        self.n_mod.setGeometry(QtCore.QRect(400, 160, 50, 40))
        self.n_mod.setFont(font)
        self.n_mod.setObjectName("n_mod")
        self.sub_dn = QtWidgets.QPushButton(self.Natural)
        self.sub_dn.setGeometry(QtCore.QRect(350, 320, 100, 45))
        self.sub_dn.setObjectName("sub_dn")
        self.n_mul_k = QtWidgets.QPushButton(self.Natural)
        self.n_mul_k.setGeometry(QtCore.QRect(50, 320, 100, 45))
        self.n_mul_k.setObjectName("n_mul_k")
        self.n_div_dk = QtWidgets.QPushButton(self.Natural)
        self.n_div_dk.setGeometry(QtCore.QRect(50, 400, 100, 45))
        self.n_div_dk.setObjectName("n_div_dk")
        self.n_mul = QtWidgets.QPushButton(self.Natural)
        self.n_mul.setGeometry(QtCore.QRect(226, 160, 50, 40))
        self.n_mul.setFont(bold_font)
        self.n_mul.setObjectName("n_mul")
        self.n_div = QtWidgets.QPushButton(self.Natural)
        self.n_div.setGeometry(QtCore.QRect(314, 160, 50, 40))
        self.n_div.setFont(font)
        self.n_div.setObjectName("n_div")
        self.n_gcf = QtWidgets.QPushButton(self.Natural)
        self.n_gcf.setGeometry(QtCore.QRect(200, 400, 100, 45))
        self.n_gcf.setObjectName("n_gcf")
        self.n_lcm = QtWidgets.QPushButton(self.Natural)
        self.n_lcm.setGeometry(QtCore.QRect(350, 400, 100, 45))
        self.n_lcm.setObjectName("n_lcm")
        self.z_ntoz = QtWidgets.QPushButton(self.Natural)
        self.z_ntoz.setGeometry(QtCore.QRect(50, 480, 100, 45))
        self.z_ntoz.setObjectName("z_ntoz")
        self.stackedWidget.addWidget(self.Natural)

    def createIntegerPage(self):
        self.Integer = QtWidgets.QWidget()
        self.Integer.setObjectName("Integer")

        bold_font = QtGui.QFont()
        bold_font.setPointSize(11)
        bold_font.setBold(True)
        bold_font.setWeight(75)

        label_font = QtGui.QFont()
        label_font.setPointSize(14)
        label_font.setBold(False)
        label_font.setWeight(50)
        label_font.setStrikeOut(False)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.z_input = QtWidgets.QLineEdit(self.Integer)
        self.z_input.setGeometry(QtCore.QRect(50, 30, 400, 81))
        self.z_input.setObjectName("z_input")
        self.z_label = QtWidgets.QLabel(self.Integer)
        self.z_label.setGeometry(QtCore.QRect(50, 120, 151, 21))
        self.z_label.setFont(label_font)
        self.z_label.setObjectName("z_label")
        self.z_zton = QtWidgets.QPushButton(self.Integer)
        self.z_zton.setGeometry(QtCore.QRect(50, 320, 100, 45))
        self.z_zton.setObjectName("z_zton")
        self.z_change_sign = QtWidgets.QPushButton(self.Integer)
        self.z_change_sign.setGeometry(QtCore.QRect(350, 240, 100, 45))
        self.z_change_sign.setObjectName("z_change_sign")
        self.z_div = QtWidgets.QPushButton(self.Integer)
        self.z_div.setGeometry(QtCore.QRect(314, 160, 50, 40))
        self.z_div.setFont(font)
        self.z_div.setObjectName("z_div")
        self.z_mod = QtWidgets.QPushButton(self.Integer)
        self.z_mod.setGeometry(QtCore.QRect(400, 160, 50, 40))
        self.z_mod.setFont(font)
        self.z_mod.setObjectName("z_mod")
        self.z_add = QtWidgets.QPushButton(self.Integer)
        self.z_add.setGeometry(QtCore.QRect(50, 160, 50, 40))
        self.z_add.setFont(bold_font)
        self.z_add.setObjectName("z_add")
        self.z_mul = QtWidgets.QPushButton(self.Integer)
        self.z_mul.setGeometry(QtCore.QRect(226, 160, 50, 40))
        self.z_mul.setFont(bold_font)
        self.z_mul.setObjectName("z_mul")
        self.z_abs = QtWidgets.QPushButton(self.Integer)
        self.z_abs.setGeometry(QtCore.QRect(50, 240, 100, 45))
        self.z_abs.setObjectName("z_abs")
        self.z_sub = QtWidgets.QPushButton(self.Integer)
        self.z_sub.setGeometry(QtCore.QRect(140, 160, 50, 40))
        self.z_sub.setFont(bold_font)
        self.z_sub.setObjectName("z_sub")
        self.z_sign = QtWidgets.QPushButton(self.Integer)
        self.z_sign.setGeometry(QtCore.QRect(200, 240, 100, 45))
        self.z_sign.setObjectName("z_sign")
        self.r_to_rational = QtWidgets.QPushButton(self.Integer)
        self.r_to_rational.setGeometry(QtCore.QRect(200, 320, 100, 45))
        self.r_to_rational.setObjectName("r_to_rational")
        self.stackedWidget.addWidget(self.Integer)

    def createRationalPage(self):
        self.Rational = QtWidgets.QWidget()
        self.Rational.setObjectName("Rational")

        bold_font = QtGui.QFont()
        bold_font.setPointSize(11)
        bold_font.setBold(True)
        bold_font.setWeight(75)

        label_font = QtGui.QFont()
        label_font.setPointSize(14)
        label_font.setBold(False)
        label_font.setWeight(50)
        label_font.setStrikeOut(False)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.r_input = QtWidgets.QLineEdit(self.Rational)
        self.r_input.setGeometry(QtCore.QRect(50, 30, 400, 81))
        self.r_input.setObjectName("r_input")
        self.r_label = QtWidgets.QLabel(self.Rational)
        self.r_label.setGeometry(QtCore.QRect(50, 120, 171, 21))
        self.r_label.setFont(label_font)
        self.r_label.setObjectName("r_label")
        self.r_mul = QtWidgets.QPushButton(self.Rational)
        self.r_mul.setGeometry(QtCore.QRect(285, 160, 50, 40))
        self.r_mul.setFont(bold_font)
        self.r_mul.setObjectName("r_mul")
        self.r_to_int = QtWidgets.QPushButton(self.Rational)
        self.r_to_int.setGeometry(QtCore.QRect(350, 240, 100, 45))
        self.r_to_int.setObjectName("r_to_int")
        self.r_add = QtWidgets.QPushButton(self.Rational)
        self.r_add.setGeometry(QtCore.QRect(50, 160, 50, 40))
        self.r_add.setFont(bold_font)
        self.r_add.setObjectName("r_add")
        self.r_reduce = QtWidgets.QPushButton(self.Rational)
        self.r_reduce.setGeometry(QtCore.QRect(50, 240, 100, 45))
        self.r_reduce.setObjectName("r_reduce")
        self.r_sub = QtWidgets.QPushButton(self.Rational)
        self.r_sub.setGeometry(QtCore.QRect(165, 160, 50, 40))
        self.r_sub.setFont(bold_font)
        self.r_sub.setObjectName("r_sub")
        self.r_is_int = QtWidgets.QPushButton(self.Rational)
        self.r_is_int.setGeometry(QtCore.QRect(200, 240, 100, 45))
        self.r_is_int.setObjectName("r_is_int")
        self.r_div = QtWidgets.QPushButton(self.Rational)
        self.r_div.setGeometry(QtCore.QRect(400, 160, 50, 40))
        self.r_div.setFont(font)
        self.r_div.setObjectName("r_div")
        self.stackedWidget.addWidget(self.Rational)

    def createPolynomPage(self):
        self.Polynom = QtWidgets.QWidget()
        self.Polynom.setObjectName("Polynom")

        bold_font = QtGui.QFont()
        bold_font.setPointSize(11)
        bold_font.setBold(True)
        bold_font.setWeight(75)

        label_font = QtGui.QFont()
        label_font.setPointSize(14)
        label_font.setBold(False)
        label_font.setWeight(50)
        label_font.setStrikeOut(False)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.p_input = QtWidgets.QLineEdit(self.Polynom)
        self.p_input.setGeometry(QtCore.QRect(50, 30, 400, 81))
        self.p_input.setObjectName("p_input")
        self.p_label = QtWidgets.QLabel(self.Polynom)
        self.p_label.setGeometry(QtCore.QRect(50, 120, 221, 21))
        self.p_label.setFont(label_font)
        self.p_label.setObjectName("p_label")
        self.p_add = QtWidgets.QPushButton(self.Polynom)
        self.p_add.setGeometry(QtCore.QRect(50, 160, 50, 40))
        self.p_add.setFont(bold_font)
        self.p_add.setObjectName("p_add")
        self.p_mul_q = QtWidgets.QPushButton(self.Polynom)
        self.p_mul_q.setGeometry(QtCore.QRect(50, 240, 100, 45))
        self.p_mul_q.setObjectName("p_mul_q")
        self.p_sub = QtWidgets.QPushButton(self.Polynom)
        self.p_sub.setGeometry(QtCore.QRect(140, 160, 50, 40))
        self.p_sub.setFont(bold_font)
        self.p_sub.setObjectName("p_sub")
        self.p_div = QtWidgets.QPushButton(self.Polynom)
        self.p_div.setGeometry(QtCore.QRect(314, 160, 50, 40))
        self.p_div.setFont(font)
        self.p_div.setObjectName("p_div")
        self.p_high_c = QtWidgets.QPushButton(self.Polynom)
        self.p_high_c.setGeometry(QtCore.QRect(350, 240, 100, 45))
        self.p_high_c.setObjectName("p_high_c")
        self.p_mul_xk = QtWidgets.QPushButton(self.Polynom)
        self.p_mul_xk.setGeometry(QtCore.QRect(200, 240, 100, 45))
        self.p_mul_xk.setObjectName("p_mul_xk")
        self.p_mul = QtWidgets.QPushButton(self.Polynom)
        self.p_mul.setGeometry(QtCore.QRect(226, 160, 50, 40))
        self.p_mul.setFont(bold_font)
        self.p_mul.setObjectName("p_mul")
        self.p_power = QtWidgets.QPushButton(self.Polynom)
        self.p_power.setGeometry(QtCore.QRect(50, 320, 100, 45))
        self.p_power.setObjectName("p_power")
        self.p_nmr = QtWidgets.QPushButton(self.Polynom)
        self.p_nmr.setGeometry(QtCore.QRect(200, 400, 100, 45))
        self.p_nmr.setObjectName("p_nmr")
        self.p_mod = QtWidgets.QPushButton(self.Polynom)
        self.p_mod.setGeometry(QtCore.QRect(400, 160, 50, 40))
        self.p_mod.setFont(font)
        self.p_mod.setObjectName("p_mod")
        self.p_fac = QtWidgets.QPushButton(self.Polynom)
        self.p_fac.setGeometry(QtCore.QRect(350, 320, 100, 45))
        self.p_fac.setObjectName("p_fac")
        self.p_derivative = QtWidgets.QPushButton(self.Polynom)
        self.p_derivative.setGeometry(QtCore.QRect(50, 400, 100, 45))
        self.p_derivative.setObjectName("p_derivative")
        self.p_gcf = QtWidgets.QPushButton(self.Polynom)
        self.p_gcf.setGeometry(QtCore.QRect(200, 320, 100, 45))
        self.p_gcf.setObjectName("p_gcf")
        self.stackedWidget.addWidget(self.Polynom)
        self.setCentralWidget(self.centralwidget)

    def createMenuBar(self):
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.about = QtWidgets.QMenu(self.menu_bar)
        self.help = QtWidgets.QMenu(self.menu_bar)
        self.classes = QtWidgets.QMenu(self.menu_bar)
        self.setMenuBar(self.menu_bar)

    def setActions(self):
        try:
            # MENU BAR ACTIONS
            self.to_wNatural = QtWidgets.QAction(self)
            self.to_wNatural.triggered.connect(lambda: self.changePage(NATURAL))
            self.to_wInteger = QtWidgets.QAction(self)
            self.to_wInteger.triggered.connect(lambda: self.changePage(INTEGER))
            self.to_wRational = QtWidgets.QAction(self)
            self.to_wRational.triggered.connect(lambda: self.changePage(RATIONAL))
            self.to_wPolynom = QtWidgets.QAction(self)
            self.to_wPolynom.triggered.connect(lambda: self.changePage(POLYNOM))
            # TO DO: add "help" and "about" triggers
            self.classes.addAction(self.to_wNatural)
            self.classes.addAction(self.to_wInteger)
            self.classes.addAction(self.to_wRational)
            self.classes.addAction(self.to_wPolynom)
            self.menu_bar.addAction(self.classes.menuAction())
            self.menu_bar.addAction(self.help.menuAction())
            self.menu_bar.addAction(self.about.menuAction())

            # NATURAL BUTTONS ACTIONS
            self.n_incr.clicked.connect(lambda: self.useUnaryOperation(self.getNumber().increment))
        # Зачем?
        except:
            self.currentLineEdit.clear()

    def getNumber(self):
        text = str(self.currentLineEdit.text())
        try:
            if self.currentIndex == NATURAL:
                return Algebra.Natural(text)
            elif self.currentIndex == INTEGER:
                return Algebra.Integer(text)
            elif self.currentIndex == RATIONAL:
                return Algebra.Rational(text)
            else:
                return Algebra.Polynom(text)
        except Exception as exc:
            self.errorHandle(INPUT_ERROR, repr(exc))
            if self.currentIndex == NATURAL:
                return Algebra.Natural()
            elif self.currentIndex == INTEGER:
                return Algebra.Integer()
            elif self.currentIndex == RATIONAL:
                return Algebra.Rational()
            else:
                return Algebra.Polynom()

    def errorHandle(self, code, errorText):
        self.currentLineEdit.clear()
        error = QtWidgets.QMessageBox()

        error.setWindowTitle("Ошибка")
        if code is INPUT_ERROR:
            error.setText("Ошибка при вводе числа.")
        else:
            error.setText("Ошибка.")

        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.setStandardButtons(QtWidgets.QMessageBox.Ok)

        error.setDetailedText(errorText)

        error.exec_()

    def changePage(self, index):
        self.stackedWidget.setCurrentIndex(index)
        self.currentIndex = index
        if index == NATURAL:
            self.currentLineEdit = self.n_input
        elif index == INTEGER:
            self.currentLineEdit = self.z_input
        elif index == RATIONAL:
            self.currentLineEdit = self.r_input
        else:
            self.currentLineEdit = self.p_input

    def useUnaryOperation(self, unary_operator):
        output = str(unary_operator())
        self.currentLineEdit.setText(output)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Algebra-CLQM"))
        self.n_label.setText(_translate("self", "Натуральные числа (n)"))
        self.n_add.setText(_translate("self", "+"))
        self.n_incr.setText(_translate("self", "+1"))
        self.sub.setText(_translate("self", "-"))
        self.n_cmp.setText(_translate("self", ">, <, ="))
        self.n_is_zero.setText(_translate("self", "= 0"))
        self.n_mul_d.setText(_translate("self", "*d"))
        self.n_mod.setText(_translate("self", "%"))
        self.sub_dn.setText(_translate("self", "- (n * d)"))
        self.n_mul_k.setText(_translate("self", "*10^k"))
        self.n_div_dk.setText(_translate("self", "- (n * 10^k)"))
        self.n_mul.setText(_translate("self", "*"))
        self.n_div.setText(_translate("self", "/"))
        self.n_gcf.setText(_translate("self", "НОД"))
        self.n_lcm.setText(_translate("self", "НОК"))
        self.z_ntoz.setText(_translate("self", "К целому"))
        self.z_label.setText(_translate("self", "Целые числа (z)"))
        self.z_zton.setText(_translate("self", "К натуральному"))
        self.z_change_sign.setText(_translate("self", "* (-1)"))
        self.z_div.setText(_translate("self", "/"))
        self.z_mod.setText(_translate("self", "%"))
        self.z_add.setText(_translate("self", "+"))
        self.z_mul.setText(_translate("self", "*"))
        self.z_abs.setText(_translate("self", "abs"))
        self.z_sub.setText(_translate("self", "-"))
        self.z_sign.setText(_translate("self", "+, -, 0"))
        self.r_to_rational.setText(_translate("self", "К рациональному"))
        self.r_label.setText(_translate("self", "Рационалые числа"))
        self.r_mul.setText(_translate("self", "*"))
        self.r_to_int.setText(_translate("self", "К целому"))
        self.r_add.setText(_translate("self", "+"))
        self.r_reduce.setText(_translate("self", "Сократить"))
        self.r_sub.setText(_translate("self", "-"))
        self.r_is_int.setText(_translate("self", "Целое?"))
        self.r_div.setText(_translate("self", "/"))
        self.p_label.setText(_translate("self", "Многочлены (полиномы)"))
        self.p_add.setText(_translate("self", "+"))
        self.p_mul_q.setText(_translate("self", "* q"))
        self.p_sub.setText(_translate("self", "-"))
        self.p_div.setText(_translate("self", "/"))
        self.p_high_c.setText(_translate("self", "Ст. коэффициент"))
        self.p_mul_xk.setText(_translate("self", "* x^k"))
        self.p_mul.setText(_translate("self", "*"))
        self.p_power.setText(_translate("self", "Степень"))
        self.p_nmr.setText(_translate("self", "Кр. корни\n"
                                              "в простые"))
        self.p_mod.setText(_translate("self", "%"))
        self.p_fac.setText(_translate("self", "НОД / НОК"))
        self.p_derivative.setText(_translate("self", "Производная"))
        self.p_gcf.setText(_translate("self", "НОД"))
        self.about.setTitle(_translate("self", "О проекте"))
        self.help.setTitle(_translate("self", "Помощь"))
        self.classes.setTitle(_translate("self", "Классы"))

        # ВОЗМОЖНО стоит убрать action_2...? Нигде не используется
        # (вроде привязаны к label)

        self.to_wNatural.setText(_translate("self", "Натуральные числа"))
        self.to_wInteger.setText(_translate("self", "Целые числа"))
        self.to_wRational.setText(_translate("self", "Рациональные числа"))
        self.to_wPolynom.setText(_translate("self", "Полиномы (многочлены)"))


def application():
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()