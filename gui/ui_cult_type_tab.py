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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(766, 563)
        self.gridLayout = QGridLayout(widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(widget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.name = QLineEdit(self.frame_4)
        self.name.setObjectName(u"name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.name)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_7 = QFrame(widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.frame_3 = QFrame(self.frame_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.profit = QSpinBox(self.frame_3)
        self.profit.setObjectName(u"profit")
        self.profit.setMaximum(9999)

        self.horizontalLayout_2.addWidget(self.profit)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.duration = QLabel(self.frame_8)
        self.duration.setObjectName(u"duration")
        self.duration.setFrameShape(QFrame.Box)

        self.horizontalLayout_7.addWidget(self.duration)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.startDate = QDateEdit(self.frame_9)
        self.startDate.setObjectName(u"startDate")

        self.horizontalLayout_6.addWidget(self.startDate)

        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.plusMinus = QSpinBox(self.frame_9)
        self.plusMinus.setObjectName(u"plusMinus")

        self.horizontalLayout_6.addWidget(self.plusMinus)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.frame_7, 1, 0, 1, 1)

        self.label_3 = QLabel(widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.frame_2 = QFrame(widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setMinimumSize(QSize(100, 10))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.periodResources.sizePolicy().hasHeightForWidth())
        self.periodResources.setSizePolicy(sizePolicy5)
        self.periodResources.setMinimumSize(QSize(300, 100))
        self.periodResources.horizontalHeader().setDefaultSectionSize(200)
        self.periodResources.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_8.addWidget(self.periodResources)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.addPeriodResources = QPushButton(self.frame)
        self.addPeriodResources.setObjectName(u"addPeriodResources")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.addPeriodResources.sizePolicy().hasHeightForWidth())
        self.addPeriodResources.setSizePolicy(sizePolicy7)

        self.verticalLayout_2.addWidget(self.addPeriodResources)

        self.removePeriodResources = QPushButton(self.frame)
        self.removePeriodResources.setObjectName(u"removePeriodResources")
        sizePolicy7.setHeightForWidth(self.removePeriodResources.sizePolicy().hasHeightForWidth())
        self.removePeriodResources.setSizePolicy(sizePolicy7)

        self.verticalLayout_2.addWidget(self.removePeriodResources)


        self.horizontalLayout_8.addWidget(self.frame)


        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1)

        self.frame_6 = QFrame(widget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy8)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        sizePolicy7.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy7)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.addStage = QPushButton(self.frame_6)
        self.addStage.setObjectName(u"addStage")
        sizePolicy7.setHeightForWidth(self.addStage.sizePolicy().hasHeightForWidth())
        self.addStage.setSizePolicy(sizePolicy7)

        self.horizontalLayout_5.addWidget(self.addStage)


        self.gridLayout.addWidget(self.frame_6, 5, 0, 1, 1)

        self.tabWidgetStages = QTabWidget(widget)
        self.tabWidgetStages.setObjectName(u"tabWidgetStages")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.tabWidgetStages.sizePolicy().hasHeightForWidth())
        self.tabWidgetStages.setSizePolicy(sizePolicy9)
        self.tabWidgetStages.setTabShape(QTabWidget.Triangular)
        self.tabWidgetStages.setTabsClosable(True)
        self.tabWidgetStages.setMovable(True)

        self.gridLayout.addWidget(self.tabWidgetStages, 6, 0, 1, 1)


        self.retranslateUi(widget)

        self.tabWidgetStages.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("widget", u"Name", None))
        self.name.setText("")
        self.label_2.setText(QCoreApplication.translate("widget", u"Profit", None))
        self.label_5.setText(QCoreApplication.translate("widget", u"Duration", None))
        self.duration.setText(QCoreApplication.translate("widget", u"0", None))
        self.label_6.setText(QCoreApplication.translate("widget", u"Start date", None))
        self.startDate.setDisplayFormat(QCoreApplication.translate("widget", u"dd.MMMM", None))
        self.label_7.setText(QCoreApplication.translate("widget", u"\u00b1", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"entire period resources", None))
        ___qtablewidgetitem = self.periodResources.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("widget", u"Resource name", None));
        ___qtablewidgetitem1 = self.periodResources.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("widget", u"Quantity", None));
        ___qtablewidgetitem2 = self.periodResources.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("widget", u"1", None));
        self.addPeriodResources.setText(QCoreApplication.translate("widget", u"Add", None))
        self.removePeriodResources.setText(QCoreApplication.translate("widget", u"Remove", None))
        self.label_4.setText(QCoreApplication.translate("widget", u"daily period resources", None))
        self.addStage.setText(QCoreApplication.translate("widget", u"Add new cultivation stage", None))
    # retranslateUi

