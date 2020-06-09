# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide2.QtWidgets import *
from variables import variables

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"Image filter")
        form_height = variables.IMAGE_SIZE + 60
        form_width = variables.IMAGE_SIZE * 2 + 40
        MainWindow.resize(form_width, form_height)
        MainWindow.setMinimumSize(QSize(form_width, form_height))
        MainWindow.setMaximumSize(QSize(form_width, form_height))

        self.centralwidget = QWidget(MainWindow)

        self.b_open = QPushButton(self.centralwidget)
        self.b_open.setGeometry(QRect(10, 10, 200, 30))
        self.b_open.setText("Открыть изображение")

        self.cb_filter = QComboBox(self.centralwidget)
        self.cb_filter.setGeometry(QRect(form_width - 400, 11, 200, 28))
        for i in range(len(variables.FILTERS)):
            self.cb_filter.addItem(variables.FILTERS[i].name)

        self.b_filter = QPushButton(self.centralwidget)
        self.b_filter.setGeometry(QRect(form_width - 190, 10, 180, 30))
        self.b_filter.setText("Применить фильтр")

        self.label1 = QLabel(MainWindow)
        self.label1.setGeometry(QRect(10, 50, variables.IMAGE_SIZE, variables.IMAGE_SIZE))

        self.label2 = QLabel(MainWindow)
        self.label2.setGeometry(QRect(variables.IMAGE_SIZE + 20, 50, variables.IMAGE_SIZE, variables.IMAGE_SIZE))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
    # retranslateUi

