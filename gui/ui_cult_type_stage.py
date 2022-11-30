# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cult_type_stage.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(687, 380)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.dailyResources = QTableWidget(Form)
        if (self.dailyResources.columnCount() < 2):
            self.dailyResources.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.dailyResources.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dailyResources.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.dailyResources.rowCount() < 1):
            self.dailyResources.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dailyResources.setVerticalHeaderItem(0, __qtablewidgetitem2)
        self.dailyResources.setObjectName(u"dailyResources")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dailyResources.sizePolicy().hasHeightForWidth())
        self.dailyResources.setSizePolicy(sizePolicy1)
        self.dailyResources.setMinimumSize(QSize(0, 100))
        self.dailyResources.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.dailyResources, 0, 2, 2, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addResources = QPushButton(self.frame)
        self.addResources.setObjectName(u"addResources")
        sizePolicy.setHeightForWidth(self.addResources.sizePolicy().hasHeightForWidth())
        self.addResources.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.addResources)

        self.removeResources = QPushButton(self.frame)
        self.removeResources.setObjectName(u"removeResources")
        sizePolicy.setHeightForWidth(self.removeResources.sizePolicy().hasHeightForWidth())
        self.removeResources.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.removeResources)


        self.gridLayout.addWidget(self.frame, 0, 3, 2, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
        ___qtablewidgetitem = self.dailyResources.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Resource name", None));
        ___qtablewidgetitem1 = self.dailyResources.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Quantity", None));
        ___qtablewidgetitem2 = self.dailyResources.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Lp. 1", None));
        self.addResources.setText(QCoreApplication.translate("Form", u"Add", None))
        self.removeResources.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Duration", None))
    # retranslateUi

