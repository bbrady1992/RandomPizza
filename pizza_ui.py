# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pizza_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 490)
        Form.setMinimumSize(QtCore.QSize(380, 490))
        Form.setMaximumSize(QtCore.QSize(380, 490))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-pizza-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 124, 16)")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 353, 477))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.optionsLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.optionsLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.optionsLineEdit.setReadOnly(True)
        self.optionsLineEdit.setObjectName("optionsLineEdit")
        self.horizontalLayout.addWidget(self.optionsLineEdit)
        self.browseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.browseButton.setStyleSheet("background-color: rgb(255, 171, 102);\n"
"color: rgb(255, 255, 255)")
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.maxToppingsLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.maxToppingsLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.maxToppingsLineEdit.setReadOnly(True)
        self.maxToppingsLineEdit.setObjectName("maxToppingsLineEdit")
        self.horizontalLayout_3.addWidget(self.maxToppingsLineEdit)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.toppingNumSelect = QtWidgets.QSpinBox(self.layoutWidget)
        self.toppingNumSelect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.toppingNumSelect.setObjectName("toppingNumSelect")
        self.horizontalLayout_2.addWidget(self.toppingNumSelect)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.crustLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.crustLineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.crustLineEdit.setReadOnly(True)
        self.crustLineEdit.setObjectName("crustLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.crustLineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cheeseLevelLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.cheeseLevelLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cheeseLevelLineEdit.setReadOnly(True)
        self.cheeseLevelLineEdit.setObjectName("cheeseLevelLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cheeseLevelLineEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.sauceLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.sauceLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.sauceLineEdit.setReadOnly(True)
        self.sauceLineEdit.setObjectName("sauceLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sauceLineEdit)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.sauceLevelLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.sauceLevelLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.sauceLevelLineEdit.setReadOnly(True)
        self.sauceLevelLineEdit.setObjectName("sauceLevelLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.sauceLevelLineEdit)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.toppingsListWidget = QtWidgets.QListWidget(self.layoutWidget)
        self.toppingsListWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.toppingsListWidget.setAlternatingRowColors(False)
        self.toppingsListWidget.setObjectName("toppingsListWidget")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.toppingsListWidget)
        self.randomizeButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.randomizeButton.setFont(font)
        self.randomizeButton.setStyleSheet("background-color: rgb(255, 171, 102);\n"
"color: rgb(255, 255, 255)\n"
"")
        self.randomizeButton.setObjectName("randomizeButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.randomizeButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Random Pizza Generator"))
        self.label_6.setText(_translate("Form", "Options File"))
        self.browseButton.setText(_translate("Form", "Browse..."))
        self.label_8.setText(_translate("Form", "Max Toppings Available"))
        self.label_7.setText(_translate("Form", "Number of Toppings"))
        self.label.setText(_translate("Form", "Crust"))
        self.label_2.setText(_translate("Form", "Cheese Level"))
        self.label_3.setText(_translate("Form", "Sauce"))
        self.label_4.setText(_translate("Form", "Sauce Level"))
        self.label_5.setText(_translate("Form", "Toppings"))
        self.randomizeButton.setText(_translate("Form", "Randomize"))

