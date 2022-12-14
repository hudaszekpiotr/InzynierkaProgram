# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QScrollArea, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(787, 479)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_2)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.topSpot = QVBoxLayout()
        self.topSpot.setObjectName(u"topSpot")

        self.gridLayout.addLayout(self.topSpot, 1, 1, 1, 1)

        self.legend = QTableWidget(Form)
        if (self.legend.columnCount() < 2):
            self.legend.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.legend.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.legend.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.legend.setObjectName(u"legend")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.legend.sizePolicy().hasHeightForWidth())
        self.legend.setSizePolicy(sizePolicy1)
        self.legend.horizontalHeader().setDefaultSectionSize(200)
        self.legend.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.legend, 1, 2, 1, 1)

        self.selectResourcesArea = QScrollArea(Form)
        self.selectResourcesArea.setObjectName(u"selectResourcesArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.selectResourcesArea.sizePolicy().hasHeightForWidth())
        self.selectResourcesArea.setSizePolicy(sizePolicy2)
        self.selectResourcesArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 73, 123))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.selectResourcesArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.selectResourcesArea, 2, 0, 1, 1)

        self.bottomSpot = QVBoxLayout()
        self.bottomSpot.setObjectName(u"bottomSpot")

        self.gridLayout.addLayout(self.bottomSpot, 2, 1, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Days", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Fields", None))
        ___qtablewidgetitem = self.legend.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"num", None));
        ___qtablewidgetitem1 = self.legend.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Cultivation type", None));
    # retranslateUi

