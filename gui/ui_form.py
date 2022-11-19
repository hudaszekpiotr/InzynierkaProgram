# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1078, 722)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(200)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(25)
        sizePolicy2.setVerticalStretch(200)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spinBox = QSpinBox(self.tab)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.spinBox, 0, 1, 1, 1)

        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 2, 0, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.runButton = QPushButton(self.tab)
        self.runButton.setObjectName(u"runButton")
        sizePolicy3.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.runButton, 0, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.gridLayout_2.addLayout(self.verticalLayout_3, 3, 0, 1, 4)

        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 0, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.types = QWidget()
        self.types.setObjectName(u"types")
        self.gridLayout_3 = QGridLayout(self.types)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidgetCultTypes = QTabWidget(self.types)
        self.tabWidgetCultTypes.setObjectName(u"tabWidgetCultTypes")
        self.type_tab_1 = QWidget()
        self.type_tab_1.setObjectName(u"type_tab_1")
        self.verticalLayout = QVBoxLayout(self.type_tab_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(self.type_tab_1)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy5)
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

        self.label_3 = QLabel(self.type_tab_1)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.label_3)

        self.frame_2 = QFrame(self.type_tab_1)
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
        sizePolicy4.setHeightForWidth(self.cultTypesPeriodResources.sizePolicy().hasHeightForWidth())
        self.cultTypesPeriodResources.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.cultTypesPeriodResources)

        self.cultTypesPeriodResourcesAddRow = QPushButton(self.frame_2)
        self.cultTypesPeriodResourcesAddRow.setObjectName(u"cultTypesPeriodResourcesAddRow")
        sizePolicy3.setHeightForWidth(self.cultTypesPeriodResourcesAddRow.sizePolicy().hasHeightForWidth())
        self.cultTypesPeriodResourcesAddRow.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.cultTypesPeriodResourcesAddRow)


        self.verticalLayout.addWidget(self.frame_2)

        self.label_4 = QLabel(self.type_tab_1)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)

        self.verticalLayout.addWidget(self.label_4)

        self.frame_6 = QFrame(self.type_tab_1)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy6)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cultTypesAddNewStage = QPushButton(self.frame_6)
        self.cultTypesAddNewStage.setObjectName(u"cultTypesAddNewStage")
        sizePolicy3.setHeightForWidth(self.cultTypesAddNewStage.sizePolicy().hasHeightForWidth())
        self.cultTypesAddNewStage.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.cultTypesAddNewStage)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy3.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.verticalLayout.addWidget(self.frame_6)

        self.stages = QTabWidget(self.type_tab_1)
        self.stages.setObjectName(u"stages")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.stages.sizePolicy().hasHeightForWidth())
        self.stages.setSizePolicy(sizePolicy7)
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

        self.tabWidgetCultTypes.addTab(self.type_tab_1, "")

        self.gridLayout_3.addWidget(self.tabWidgetCultTypes, 2, 0, 1, 1)

        self.frame_3 = QFrame(self.types)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy8)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addType = QPushButton(self.frame_3)
        self.addType.setObjectName(u"addType")
        sizePolicy3.setHeightForWidth(self.addType.sizePolicy().hasHeightForWidth())
        self.addType.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.addType)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 2, 1)

        self.tabWidget.addTab(self.types, "")
        self.fields = QWidget()
        self.fields.setObjectName(u"fields")
        self.gridLayout = QGridLayout(self.fields)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.fields)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.pushButton_7 = QPushButton(self.frame_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy3.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.pushButton_7)


        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        self.tabWidget_2 = QTabWidget(self.fields)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tabWidget_2.addTab(self.tab_8, "")

        self.gridLayout.addWidget(self.tabWidget_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.fields, "")
        self.resources = QWidget()
        self.resources.setObjectName(u"resources")
        self.cultTypesPeriodResources_2 = QTableWidget(self.resources)
        if (self.cultTypesPeriodResources_2.columnCount() < 2):
            self.cultTypesPeriodResources_2.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.cultTypesPeriodResources_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.cultTypesPeriodResources_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        if (self.cultTypesPeriodResources_2.rowCount() < 1):
            self.cultTypesPeriodResources_2.setRowCount(1)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.cultTypesPeriodResources_2.setVerticalHeaderItem(0, __qtablewidgetitem8)
        self.cultTypesPeriodResources_2.setObjectName(u"cultTypesPeriodResources_2")
        self.cultTypesPeriodResources_2.setGeometry(QRect(60, 100, 241, 251))
        sizePolicy4.setHeightForWidth(self.cultTypesPeriodResources_2.sizePolicy().hasHeightForWidth())
        self.cultTypesPeriodResources_2.setSizePolicy(sizePolicy4)
        self.tabWidget.addTab(self.resources, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1078, 22))
        self.menuinfo = QMenu(self.menubar)
        self.menuinfo.setObjectName(u"menuinfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuinfo.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidgetCultTypes.setCurrentIndex(0)
        self.stages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of iterations", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Control", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"dsdsds", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"entire period resources", None))
        ___qtablewidgetitem = self.cultTypesPeriodResources.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Resource name", None));
        ___qtablewidgetitem1 = self.cultTypesPeriodResources.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem2 = self.cultTypesPeriodResources.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Lp. 1", None));
        self.cultTypesPeriodResourcesAddRow.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"daily period resources", None))
        self.cultTypesAddNewStage.setText(QCoreApplication.translate("MainWindow", u"add new stage", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"name:", None))
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Resource name", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem5 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Lp. 1", None));
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"duration", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.stages.setTabText(self.stages.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidgetCultTypes.setTabText(self.tabWidgetCultTypes.indexOf(self.type_tab_1), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.addType.setText(QCoreApplication.translate("MainWindow", u"add new", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.types), QCoreApplication.translate("MainWindow", u"Cultivation types", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fields), QCoreApplication.translate("MainWindow", u"Fields", None))
        ___qtablewidgetitem6 = self.cultTypesPeriodResources_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Resource name", None));
        ___qtablewidgetitem7 = self.cultTypesPeriodResources_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem8 = self.cultTypesPeriodResources_2.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Lp. 1", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resources), QCoreApplication.translate("MainWindow", u"Resources", None))
        self.menuinfo.setTitle(QCoreApplication.translate("MainWindow", u"info", None))
    # retranslateUi

