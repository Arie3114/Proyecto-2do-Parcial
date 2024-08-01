# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(800, 600)
        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.text_cedula = QLineEdit(self.centralwidget)
        self.text_cedula.setObjectName(u"text_cedula")
        self.text_cedula.setGeometry(QRect(310, 170, 113, 20))
        self.text_cedula.setMaxLength(10)
        self.text_nombre = QLineEdit(self.centralwidget)
        self.text_nombre.setObjectName(u"text_nombre")
        self.text_nombre.setGeometry(QRect(310, 230, 221, 20))
        self.text_apellido = QLineEdit(self.centralwidget)
        self.text_apellido.setObjectName(u"text_apellido")
        self.text_apellido.setGeometry(QRect(310, 290, 221, 20))
        self.lbl_cedula = QLabel(self.centralwidget)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(230, 170, 47, 13))
        self.lbl_nombre = QLabel(self.centralwidget)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(230, 230, 47, 13))
        self.lbl_apellido = QLabel(self.centralwidget)
        self.lbl_apellido.setObjectName(u"lbl_apellido")
        self.lbl_apellido.setGeometry(QRect(230, 290, 47, 13))
        self.btn_guardar = QPushButton(self.centralwidget)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(290, 440, 75, 23))
        self.btn_cancelar = QPushButton(self.centralwidget)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(450, 440, 75, 23))
        self.text_correo = QLineEdit(self.centralwidget)
        self.text_correo.setObjectName(u"text_correo")
        self.text_correo.setGeometry(QRect(310, 340, 221, 20))
        self.lbl_correo = QLabel(self.centralwidget)
        self.lbl_correo.setObjectName(u"lbl_correo")
        self.lbl_correo.setGeometry(QRect(230, 340, 47, 13))
        self.lbl_edad = QLabel(self.centralwidget)
        self.lbl_edad.setObjectName(u"lbl_edad")
        self.lbl_edad.setGeometry(QRect(230, 390, 47, 13))
        self.text_edad = QLineEdit(self.centralwidget)
        self.text_edad.setObjectName(u"text_edad")
        self.text_edad.setGeometry(QRect(310, 390, 101, 20))
        vtn_principal.setCentralWidget(self.centralwidget)
        self.mnu_menu = QMenuBar(vtn_principal)
        self.mnu_menu.setObjectName(u"mnu_menu")
        self.mnu_menu.setGeometry(QRect(0, 0, 800, 33))
        vtn_principal.setMenuBar(self.mnu_menu)
        self.stb_estado = QStatusBar(vtn_principal)
        self.stb_estado.setObjectName(u"stb_estado")
        vtn_principal.setStatusBar(self.stb_estado)
        QWidget.setTabOrder(self.text_cedula, self.text_nombre)
        QWidget.setTabOrder(self.text_nombre, self.text_apellido)
        QWidget.setTabOrder(self.text_apellido, self.text_correo)
        QWidget.setTabOrder(self.text_correo, self.text_edad)
        QWidget.setTabOrder(self.text_edad, self.btn_guardar)
        QWidget.setTabOrder(self.btn_guardar, self.btn_cancelar)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"MainWindow", None))
        self.lbl_cedula.setText(QCoreApplication.translate("vtn_principal", u"Cedula:", None))
        self.lbl_nombre.setText(QCoreApplication.translate("vtn_principal", u"Nombre:", None))
        self.lbl_apellido.setText(QCoreApplication.translate("vtn_principal", u"Apellido:", None))
        self.btn_guardar.setText(QCoreApplication.translate("vtn_principal", u"Guardar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("vtn_principal", u"Cancelar", None))
        self.lbl_correo.setText(QCoreApplication.translate("vtn_principal", u"Correo:", None))
        self.lbl_edad.setText(QCoreApplication.translate("vtn_principal", u"Edad:", None))
    # retranslateUi

