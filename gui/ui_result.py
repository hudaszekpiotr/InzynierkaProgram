# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QScrollArea, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1133, 500)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(1000, 500))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bottomSpot = QVBoxLayout()
        self.bottomSpot.setObjectName(u"bottomSpot")

        self.gridLayout.addLayout(self.bottomSpot, 3, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_2)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.topSpot = QVBoxLayout()
        self.topSpot.setObjectName(u"topSpot")

        self.gridLayout.addLayout(self.topSpot, 1, 1, 1, 1)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 5)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 69, 132))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.selectResourcesArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.selectResourcesArea, 3, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.periodSpot = QVBoxLayout()
        self.periodSpot.setObjectName(u"periodSpot")

        self.gridLayout.addLayout(self.periodSpot, 3, 4, 1, 1)

        self.legend = QTableWidget(Form)
        if (self.legend.columnCount() < 2):
            self.legend.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.legend.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.legend.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.legend.setObjectName(u"legend")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.legend.sizePolicy().hasHeightForWidth())
        self.legend.setSizePolicy(sizePolicy3)
        self.legend.horizontalHeader().setDefaultSectionSize(200)
        self.legend.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.legend, 1, 2, 1, 3)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 3, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Fields", None))
        self.label.setText(QCoreApplication.translate("Form", u"Days", None))
        ___qtablewidgetitem = self.legend.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"num", None));
        ___qtablewidgetitem1 = self.legend.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Cultivation type", None));
    # retranslateUi

