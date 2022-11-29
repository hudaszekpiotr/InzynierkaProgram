# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cult_type_tab.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(766, 563)
        self.verticalLayout = QVBoxLayout(widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(widget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.name = QLineEdit(self.frame_5)
        self.name.setObjectName(u"name")

        self.horizontalLayout_3.addWidget(self.name)


        self.verticalLayout.addWidget(self.frame_5)

        self.label_3 = QLabel(widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_3)

        self.frame_2 = QFrame(widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.periodResources = QTableWidget(self.frame_2)
        if (self.periodResources.columnCount() < 2):
            self.periodResources.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.periodResources.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.periodResources.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.periodResources.rowCount() < 1):
            self.periodResources.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.periodResources.setVerticalHeaderItem(0, __qtablewidgetitem2)
        self.periodResources.setObjectName(u"periodResources")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.periodResources.sizePolicy().hasHeightForWidth())
        self.periodResources.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.periodResources, 0, 0, 1, 1)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.addPeriodResources = QPushButton(self.frame)
        self.addPeriodResources.setObjectName(u"addPeriodResources")
        sizePolicy1.setHeightForWidth(self.addPeriodResources.sizePolicy().hasHeightForWidth())
        self.addPeriodResources.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.addPeriodResources)

        self.removePeriodResources = QPushButton(self.frame)
        self.removePeriodResources.setObjectName(u"removePeriodResources")
        sizePolicy1.setHeightForWidth(self.removePeriodResources.sizePolicy().hasHeightForWidth())
        self.removePeriodResources.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.removePeriodResources)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.label_4 = QLabel(widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_4)

        self.frame_6 = QFrame(widget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy4)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.addStage = QPushButton(self.frame_6)
        self.addStage.setObjectName(u"addStage")
        sizePolicy1.setHeightForWidth(self.addStage.sizePolicy().hasHeightForWidth())
        self.addStage.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.addStage)

        self.removeStage = QPushButton(self.frame_6)
        self.removeStage.setObjectName(u"removeStage")
        sizePolicy1.setHeightForWidth(self.removeStage.sizePolicy().hasHeightForWidth())
        self.removeStage.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.removeStage)


        self.verticalLayout.addWidget(self.frame_6)

        self.tabWidgetStages = QTabWidget(widget)
        self.tabWidgetStages.setObjectName(u"tabWidgetStages")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tabWidgetStages.sizePolicy().hasHeightForWidth())
        self.tabWidgetStages.setSizePolicy(sizePolicy5)

        self.verticalLayout.addWidget(self.tabWidgetStages)


        self.retranslateUi(widget)

        self.tabWidgetStages.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("widget", u"Name", None))
        self.name.setText("")
        self.label_3.setText(QCoreApplication.translate("widget", u"entire period resources", None))
        ___qtablewidgetitem = self.periodResources.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("widget", u"Resource name", None));
        ___qtablewidgetitem1 = self.periodResources.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("widget", u"Quantity", None));
        ___qtablewidgetitem2 = self.periodResources.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("widget", u"Lp. 1", None));
        self.addPeriodResources.setText(QCoreApplication.translate("widget", u"Add", None))
        self.removePeriodResources.setText(QCoreApplication.translate("widget", u"Remove", None))
        self.label_4.setText(QCoreApplication.translate("widget", u"daily period resources", None))
        self.addStage.setText(QCoreApplication.translate("widget", u"Add new stage", None))
        self.removeStage.setText(QCoreApplication.translate("widget", u"Remove selected stage", None))
    # retranslateUi

