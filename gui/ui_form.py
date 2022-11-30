# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

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
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(200)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(25)
        sizePolicy2.setVerticalStretch(200)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 0, 2, 1, 1)

        self.runButton = QPushButton(self.tab)
        self.runButton.setObjectName(u"runButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.runButton, 0, 3, 1, 1)

        self.spinBox = QSpinBox(self.tab)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy3.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.spinBox, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.gridLayout_2.addLayout(self.verticalLayout_3, 3, 0, 1, 4)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 2, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.types = QWidget()
        self.types.setObjectName(u"types")
        self.gridLayout_3 = QGridLayout(self.types)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidgetCultTypes = QTabWidget(self.types)
        self.tabWidgetCultTypes.setObjectName(u"tabWidgetCultTypes")

        self.gridLayout_3.addWidget(self.tabWidgetCultTypes, 2, 0, 1, 1)

        self.frame_3 = QFrame(self.types)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addCultType = QPushButton(self.frame_3)
        self.addCultType.setObjectName(u"addCultType")
        sizePolicy3.setHeightForWidth(self.addCultType.sizePolicy().hasHeightForWidth())
        self.addCultType.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.addCultType)

        self.removeCultType = QPushButton(self.frame_3)
        self.removeCultType.setObjectName(u"removeCultType")
        sizePolicy3.setHeightForWidth(self.removeCultType.sizePolicy().hasHeightForWidth())
        self.removeCultType.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.removeCultType)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 2, 1)

        self.tabWidget.addTab(self.types, "")
        self.fields = QWidget()
        self.fields.setObjectName(u"fields")
        self.verticalLayout_8 = QVBoxLayout(self.fields)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_4 = QFrame(self.fields)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.addField = QPushButton(self.frame_4)
        self.addField.setObjectName(u"addField")
        sizePolicy3.setHeightForWidth(self.addField.sizePolicy().hasHeightForWidth())
        self.addField.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.addField)

        self.removeField = QPushButton(self.frame_4)
        self.removeField.setObjectName(u"removeField")
        sizePolicy3.setHeightForWidth(self.removeField.sizePolicy().hasHeightForWidth())
        self.removeField.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.removeField)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.tabWidgetFields = QTabWidget(self.fields)
        self.tabWidgetFields.setObjectName(u"tabWidgetFields")

        self.verticalLayout_8.addWidget(self.tabWidgetFields)

        self.tabWidget.addTab(self.fields, "")
        self.resources = QWidget()
        self.resources.setObjectName(u"resources")
        self.gridLayout_6 = QGridLayout(self.resources)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_8 = QFrame(self.resources)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.cultTypesPeriodResources_7 = QTableWidget(self.frame_8)
        if (self.cultTypesPeriodResources_7.columnCount() < 2):
            self.cultTypesPeriodResources_7.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.cultTypesPeriodResources_7.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cultTypesPeriodResources_7.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.cultTypesPeriodResources_7.rowCount() < 1):
            self.cultTypesPeriodResources_7.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.cultTypesPeriodResources_7.setVerticalHeaderItem(0, __qtablewidgetitem2)
        self.cultTypesPeriodResources_7.setObjectName(u"cultTypesPeriodResources_7")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.cultTypesPeriodResources_7.sizePolicy().hasHeightForWidth())
        self.cultTypesPeriodResources_7.setSizePolicy(sizePolicy7)

        self.gridLayout_5.addWidget(self.cultTypesPeriodResources_7, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy7.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy7)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_8 = QPushButton(self.frame_7)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_7)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_2.addWidget(self.pushButton_9)


        self.gridLayout_5.addWidget(self.frame_7, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_8, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.resources)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.cultTypesPeriodResources_8 = QTableWidget(self.frame_9)
        if (self.cultTypesPeriodResources_8.columnCount() < 2):
            self.cultTypesPeriodResources_8.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.cultTypesPeriodResources_8.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.cultTypesPeriodResources_8.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        if (self.cultTypesPeriodResources_8.rowCount() < 1):
            self.cultTypesPeriodResources_8.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.cultTypesPeriodResources_8.setVerticalHeaderItem(0, __qtablewidgetitem5)
        self.cultTypesPeriodResources_8.setObjectName(u"cultTypesPeriodResources_8")
        sizePolicy7.setHeightForWidth(self.cultTypesPeriodResources_8.sizePolicy().hasHeightForWidth())
        self.cultTypesPeriodResources_8.setSizePolicy(sizePolicy7)

        self.gridLayout_7.addWidget(self.cultTypesPeriodResources_8, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_10 = QPushButton(self.frame_11)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_4.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_11)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_4.addWidget(self.pushButton_11)


        self.gridLayout_7.addWidget(self.frame_11, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_9, 0, 1, 1, 1)

        self.tabWidget.addTab(self.resources, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1078, 32))
        self.menuinfo = QMenu(self.menubar)
        self.menuinfo.setObjectName(u"menuinfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuinfo.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)
        self.tabWidgetCultTypes.setCurrentIndex(-1)
        self.tabWidgetFields.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of iterations", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Control", None))
        self.addCultType.setText(QCoreApplication.translate("MainWindow", u"Add new", None))
        self.removeCultType.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.types), QCoreApplication.translate("MainWindow", u"Cultivation types", None))
        self.addField.setText(QCoreApplication.translate("MainWindow", u"Add new", None))
        self.removeField.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fields), QCoreApplication.translate("MainWindow", u"Fields", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Daily resources", None))
        ___qtablewidgetitem = self.cultTypesPeriodResources_7.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Resource name", None));
        ___qtablewidgetitem1 = self.cultTypesPeriodResources_7.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem2 = self.cultTypesPeriodResources_7.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Lp. 1", None));
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Entire period resources", None))
        ___qtablewidgetitem3 = self.cultTypesPeriodResources_8.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Resource name", None));
        ___qtablewidgetitem4 = self.cultTypesPeriodResources_8.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem5 = self.cultTypesPeriodResources_8.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Lp. 1", None));
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resources), QCoreApplication.translate("MainWindow", u"Resources", None))
        self.menuinfo.setTitle(QCoreApplication.translate("MainWindow", u"info", None))
    # retranslateUi

