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

class Ui_widget(object):
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

        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)


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
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cultTypesPeriodResources = QTableWidget(self.frame_2)
        if (self.cultTypesPeriodResources.columnCount() < 2):
            self.cultTypesPeriodResources.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.cultTypesPeriodResources.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cultTypesPeriodResources.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.cultTypesPeriodResources.rowCount() < 1):
            self.cultTypesPeriodResources.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.cultTypesPeriodResources.setVerticalHeaderItem(0, __qtablewidgetitem2)
        self.cultTypesPeriodResources.setObjectName(u"cultTypesPeriodResources")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cultTypesPeriodResources.sizePolicy().hasHeightForWidth())
        self.cultTypesPeriodResources.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.cultTypesPeriodResources)

        self.cultTypesPeriodResourcesAddRow = QPushButton(self.frame_2)
        self.cultTypesPeriodResourcesAddRow.setObjectName(u"cultTypesPeriodResourcesAddRow")
        sizePolicy1.setHeightForWidth(self.cultTypesPeriodResourcesAddRow.sizePolicy().hasHeightForWidth())
        self.cultTypesPeriodResourcesAddRow.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.cultTypesPeriodResourcesAddRow)


        self.verticalLayout.addWidget(self.frame_2)

        self.label_4 = QLabel(widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_4)

        self.frame_6 = QFrame(widget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cultTypesAddNewStage = QPushButton(self.frame_6)
        self.cultTypesAddNewStage.setObjectName(u"cultTypesAddNewStage")
        sizePolicy1.setHeightForWidth(self.cultTypesAddNewStage.sizePolicy().hasHeightForWidth())
        self.cultTypesAddNewStage.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.cultTypesAddNewStage)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.verticalLayout.addWidget(self.frame_6)

        self.stages = QTabWidget(widget)
        self.stages.setObjectName(u"stages")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stages.sizePolicy().hasHeightForWidth())
        self.stages.setSizePolicy(sizePolicy4)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.tab_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_4.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.tableWidget_2 = QTableWidget(self.tab_4)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        if (self.tableWidget_2.rowCount() < 1):
            self.tableWidget_2.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_4.addWidget(self.tableWidget_2, 0, 2, 2, 1, Qt.AlignVCenter)

        self.pushButton_5 = QPushButton(self.tab_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_4.addWidget(self.pushButton_5, 0, 3, 1, 1)

        self.label_6 = QLabel(self.tab_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.tab_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_4.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.tab_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_4.addWidget(self.pushButton_6, 1, 3, 1, 1)

        self.stages.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.stages)


        self.retranslateUi(widget)

        self.stages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("widget", u"name", None))
        self.lineEdit.setText(QCoreApplication.translate("widget", u"dsdsds", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"entire period resources", None))
        ___qtablewidgetitem = self.cultTypesPeriodResources.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("widget", u"Resource name", None));
        ___qtablewidgetitem1 = self.cultTypesPeriodResources.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("widget", u"Quantity", None));
        ___qtablewidgetitem2 = self.cultTypesPeriodResources.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("widget", u"Lp. 1", None));
        self.cultTypesPeriodResourcesAddRow.setText(QCoreApplication.translate("widget", u"add", None))
        self.label_4.setText(QCoreApplication.translate("widget", u"daily period resources", None))
        self.cultTypesAddNewStage.setText(QCoreApplication.translate("widget", u"add new stage", None))
        self.pushButton_4.setText(QCoreApplication.translate("widget", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("widget", u"name:", None))
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("widget", u"Resource name", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("widget", u"Quantity", None));
        ___qtablewidgetitem5 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("widget", u"Lp. 1", None));
        self.pushButton_5.setText(QCoreApplication.translate("widget", u"+", None))
        self.label_6.setText(QCoreApplication.translate("widget", u"duration", None))
        self.pushButton_6.setText(QCoreApplication.translate("widget", u"-", None))
        self.stages.setTabText(self.stages.indexOf(self.tab_4), QCoreApplication.translate("widget", u"Tab 1", None))
    # retranslateUi

