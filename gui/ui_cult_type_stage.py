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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Widget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(564, 372)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
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
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dailyResources.sizePolicy().hasHeightForWidth())
        self.dailyResources.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.dailyResources, 0, 2, 2, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.removeResources = QPushButton(Form)
        self.removeResources.setObjectName(u"removeResources")
        sizePolicy1.setHeightForWidth(self.removeResources.sizePolicy().hasHeightForWidth())
        self.removeResources.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.removeResources, 1, 3, 1, 1)

        self.addResources = QPushButton(Form)
        self.addResources.setObjectName(u"addResources")
        sizePolicy1.setHeightForWidth(self.addResources.sizePolicy().hasHeightForWidth())
        self.addResources.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.addResources, 0, 3, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.dailyResources.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Resource name", None));
        ___qtablewidgetitem1 = self.dailyResources.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Quantity", None));
        ___qtablewidgetitem2 = self.dailyResources.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Lp. 1", None));
        self.label_2.setText(QCoreApplication.translate("Form", u"Duration", None))
        self.removeResources.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.addResources.setText(QCoreApplication.translate("Form", u"Add", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
    # retranslateUi

