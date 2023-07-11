# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFrame,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 600)
        MainWindow.setMinimumSize(QSize(550, 600))
        MainWindow.setMaximumSize(QSize(550, 600))
        MainWindow.setStyleSheet(u"color: #F2F3F5;\n"
"font-weight: 400;\n"
"background-color: #242428;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_appid = QLineEdit(self.centralwidget)
        self.input_appid.setObjectName(u"input_appid")
        self.input_appid.setGeometry(QRect(40, 50, 221, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.input_appid.setFont(font)
        self.input_appid.setStyleSheet(u"background-color:  #4E5058;\n"
"border: none;\n"
"border-radius: 7px;\n"
"padding: 0 7px;\n"
"margin-top: 2px;")
        self.lb_appid = QLabel(self.centralwidget)
        self.lb_appid.setObjectName(u"lb_appid")
        self.lb_appid.setGeometry(QRect(40, 30, 221, 20))
        self.lb_appid.setFont(font)
        self.lb_appid.setStyleSheet(u"background-color: transparent;")
        self.select_presets = QComboBox(self.centralwidget)
        self.select_presets.addItem("")
        self.select_presets.addItem("")
        self.select_presets.addItem("")
        self.select_presets.setObjectName(u"select_presets")
        self.select_presets.setGeometry(QRect(280, 50, 231, 31))
        self.select_presets.setStyleSheet(u"background-color:  #4E5058;\n"
"border: none;\n"
"border-radius: 7px;\n"
"padding: 0 7px;\n"
"margin-top: 2px;")
        self.lb_presets = QLabel(self.centralwidget)
        self.lb_presets.setObjectName(u"lb_presets")
        self.lb_presets.setGeometry(QRect(280, 30, 231, 16))
        self.lb_presets.setFont(font)
        self.lb_presets.setStyleSheet(u"background-color: transparent;")
        self.lb_details = QLabel(self.centralwidget)
        self.lb_details.setObjectName(u"lb_details")
        self.lb_details.setGeometry(QRect(40, 100, 211, 20))
        self.lb_details.setFont(font)
        self.lb_details.setStyleSheet(u"background-color: transparent;")
        self.input_details = QLineEdit(self.centralwidget)
        self.input_details.setObjectName(u"input_details")
        self.input_details.setGeometry(QRect(40, 120, 471, 31))
        self.input_details.setFont(font)
        self.input_details.setStyleSheet(u"background-color:  #4E5058;\n"
"border: none;\n"
"border-radius: 7px;\n"
"padding: 0 7px;\n"
"margin-top: 2px;")
        self.lb_state = QLabel(self.centralwidget)
        self.lb_state.setObjectName(u"lb_state")
        self.lb_state.setGeometry(QRect(40, 170, 221, 20))
        self.lb_state.setFont(font)
        self.lb_state.setStyleSheet(u"background-color: transparent;")
        self.input_state = QLineEdit(self.centralwidget)
        self.input_state.setObjectName(u"input_state")
        self.input_state.setGeometry(QRect(40, 190, 221, 31))
        self.input_state.setFont(font)
        self.input_state.setStyleSheet(u"background-color:  #4E5058;\n"
"border: none;\n"
"border-radius: 7px;\n"
"padding: 0 7px;\n"
"margin-top: 2px;")
        self.lb_party = QLabel(self.centralwidget)
        self.lb_party.setObjectName(u"lb_party")
        self.lb_party.setGeometry(QRect(280, 170, 261, 16))
        self.lb_party.setFont(font)
        self.lb_party.setStyleSheet(u"background-color: transparent;")
        self.number_partyMin = QSpinBox(self.centralwidget)
        self.number_partyMin.setObjectName(u"number_partyMin")
        self.number_partyMin.setGeometry(QRect(280, 191, 71, 31))
        self.number_partyMin.setFont(font)
        self.number_partyMin.setStyleSheet(u"background-color:  #4E5058;\n"
"border: none;\n"
"border-radius: 7px;\n"
"padding: 0 7px;\n"
"margin-top: 2px;")
        self.number_partyMin.setMinimum(-1)
        self.number_partyMin.setValue(-1)
        self.number_partyMax = QSpinBox(self.centralwidget)
        self.number_partyMax.setObjectName(u"number_partyMax")
        self.number_partyMax.setGeometry(QRect(380, 190, 71, 31))
        self.number_partyMax.setFont(font)
        self.number_partyMax.setStyleSheet(u"background-color:  #4E5058;\n"
"border: none;\n"
"border-radius: 7px;\n"
"padding: 0 7px;\n"
"margin-top: 2px;")
        self.number_partyMax.setMinimum(-1)
        self.number_partyMax.setValue(-1)
        self.divider = QLabel(self.centralwidget)
        self.divider.setObjectName(u"divider")
        self.divider.setGeometry(QRect(360, 190, 20, 31))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        self.divider.setFont(font1)
        self.divider.setStyleSheet(u"background-color: transparent;")
        self.lb_timestamp = QLabel(self.centralwidget)
        self.lb_timestamp.setObjectName(u"lb_timestamp")
        self.lb_timestamp.setGeometry(QRect(40, 240, 231, 20))
        self.lb_timestamp.setFont(font)
        self.lb_timestamp.setStyleSheet(u"background-color: transparent;")
        self.timestampBtns = QGroupBox(self.centralwidget)
        self.timestampBtns.setObjectName(u"timestampBtns")
        self.timestampBtns.setGeometry(QRect(40, 260, 221, 101))
        self.timestampBtns.setStyleSheet(u"background-color:  #4E5058;\n"
"border: none;\n"
"border-radius: 7px;\n"
"margin-top: 2px;\n"
"border: none;")
        self.radio_none = QRadioButton(self.timestampBtns)
        self.radio_none.setObjectName(u"radio_none")
        self.radio_none.setEnabled(True)
        self.radio_none.setGeometry(QRect(10, 10, 231, 17))
        self.radio_none.setFont(font)
        self.radio_none.setStyleSheet(u"background-color: none;")
        self.radio_none.setChecked(True)
        self.radio_localtime = QRadioButton(self.timestampBtns)
        self.radio_localtime.setObjectName(u"radio_localtime")
        self.radio_localtime.setGeometry(QRect(10, 30, 231, 17))
        self.radio_localtime.setFont(font)
        self.radio_localtime.setStyleSheet(u"background-color: none;")
        self.radio_appstart = QRadioButton(self.timestampBtns)
        self.radio_appstart.setObjectName(u"radio_appstart")
        self.radio_appstart.setGeometry(QRect(10, 50, 231, 17))
        self.radio_appstart.setFont(font)
        self.radio_appstart.setStyleSheet(u"background-color: none;")
        self.radio_custom = QRadioButton(self.timestampBtns)
        self.radio_custom.setObjectName(u"radio_custom")
        self.radio_custom.setGeometry(QRect(10, 70, 231, 17))
        self.radio_custom.setFont(font)
        self.radio_custom.setStyleSheet(u"background-color: none;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 511, 561))
        self.frame.setStyleSheet(u"background-color: #111214;\n"
"border-radius: 12px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.button_save = QPushButton(self.frame)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(20, 500, 211, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.button_save.setFont(font2)
        self.button_save.setStyleSheet(u"background-color: #4E5058;\n"
"font-weight: 500;")
        self.date_customtimestamp = QDateTimeEdit(self.frame)
        self.date_customtimestamp.setObjectName(u"date_customtimestamp")
        self.date_customtimestamp.setEnabled(False)
        self.date_customtimestamp.setGeometry(QRect(20, 350, 221, 31))
        self.date_customtimestamp.setFont(font)
        self.date_customtimestamp.setStyleSheet(u"background-color:  #4E5058;\n"
"border: none;\n"
"border-radius: 7px;\n"
"padding: 0 7px;\n"
"margin-top: 2px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.input_appid.raise_()
        self.input_details.raise_()
        self.input_state.raise_()
        self.lb_appid.raise_()
        self.lb_details.raise_()
        self.lb_party.raise_()
        self.lb_presets.raise_()
        self.lb_state.raise_()
        self.lb_timestamp.raise_()
        self.number_partyMax.raise_()
        self.number_partyMin.raise_()
        self.select_presets.raise_()
        self.timestampBtns.raise_()
        self.divider.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Discord Custom RP", None))
        self.input_appid.setText(QCoreApplication.translate("MainWindow", u"awdswadsdwas", None))
        self.lb_appid.setText(QCoreApplication.translate("MainWindow", u"Application ID", None))
        self.select_presets.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.select_presets.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.select_presets.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 2", None))

        self.lb_presets.setText(QCoreApplication.translate("MainWindow", u"Preset", None))
        self.lb_details.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.input_details.setText(QCoreApplication.translate("MainWindow", u"My very nice details!", None))
        self.lb_state.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.input_state.setText(QCoreApplication.translate("MainWindow", u"A very nice custom State!", None))
        self.lb_party.setText(QCoreApplication.translate("MainWindow", u"Party", None))
        self.divider.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.lb_timestamp.setText(QCoreApplication.translate("MainWindow", u"Timestamp", None))
        self.timestampBtns.setTitle("")
        self.radio_none.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.radio_localtime.setText(QCoreApplication.translate("MainWindow", u"My local time", None))
        self.radio_appstart.setText(QCoreApplication.translate("MainWindow", u"Since app started", None))
        self.radio_custom.setText(QCoreApplication.translate("MainWindow", u"Custom timestamp", None))
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

