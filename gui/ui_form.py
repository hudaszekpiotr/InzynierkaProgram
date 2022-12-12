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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1110, 551)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.actionlast_used = QAction(MainWindow)
        self.actionlast_used.setObjectName(u"actionlast_used")
        self.actionset1 = QAction(MainWindow)
        self.actionset1.setObjectName(u"actionset1")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
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
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.tab.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.gridLayout_2.addLayout(self.verticalLayout_3, 3, 0, 1, 9)

        self.runButton = QPushButton(self.tab)
        self.runButton.setObjectName(u"runButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.runButton, 0, 8, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_9 = QGridLayout(self.groupBox_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

        self.gridLayout_9.addWidget(self.label_4, 1, 0, 1, 2)

        self.crossoverType = QComboBox(self.groupBox_3)
        self.crossoverType.addItem("")
        self.crossoverType.addItem("")
        self.crossoverType.setObjectName(u"crossoverType")

        self.gridLayout_9.addWidget(self.crossoverType, 1, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)

        self.gridLayout_9.addWidget(self.label_10, 0, 0, 1, 1)

        self.mutationProbability = QDoubleSpinBox(self.groupBox_3)
        self.mutationProbability.setObjectName(u"mutationProbability")
        self.mutationProbability.setMaximum(1.000000000000000)
        self.mutationProbability.setValue(0.100000000000000)

        self.gridLayout_9.addWidget(self.mutationProbability, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 0, 3, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_10 = QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_10.addWidget(self.label_14, 0, 0, 1, 1)

        self.initialPopulationType = QComboBox(self.groupBox_4)
        self.initialPopulationType.addItem("")
        self.initialPopulationType.addItem("")
        self.initialPopulationType.setObjectName(u"initialPopulationType")

        self.gridLayout_10.addWidget(self.initialPopulationType, 0, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.label_11, 1, 0, 1, 1)

        self.populationSize = QSpinBox(self.groupBox_4)
        self.populationSize.setObjectName(u"populationSize")
        sizePolicy3.setHeightForWidth(self.populationSize.sizePolicy().hasHeightForWidth())
        self.populationSize.setSizePolicy(sizePolicy3)
        self.populationSize.setMinimum(10)
        self.populationSize.setMaximum(999999)
        self.populationSize.setValue(10)

        self.gridLayout_10.addWidget(self.populationSize, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 1, 2, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)

        self.startDate = QDateEdit(self.groupBox_2)
        self.startDate.setObjectName(u"startDate")
        self.startDate.setDate(QDate(2022, 5, 1))

        self.gridLayout_8.addWidget(self.startDate, 0, 1, 1, 1)

        self.numDays = QSpinBox(self.groupBox_2)
        self.numDays.setObjectName(u"numDays")
        self.numDays.setMaximum(999)
        self.numDays.setValue(30)

        self.gridLayout_8.addWidget(self.numDays, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.label_9, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 7, 1, 1)

        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.gridLayout_11 = QGridLayout(self.groupBox_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_11.addWidget(self.label_15, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.gridLayout_11.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_11.addWidget(self.label_16, 4, 0, 1, 1)

        self.eliteSize = QSpinBox(self.groupBox_5)
        self.eliteSize.setObjectName(u"eliteSize")

        self.gridLayout_11.addWidget(self.eliteSize, 4, 1, 1, 1)

        self.matingPoolSize = QSpinBox(self.groupBox_5)
        self.matingPoolSize.setObjectName(u"matingPoolSize")
        self.matingPoolSize.setMinimum(1)
        self.matingPoolSize.setValue(50)

        self.gridLayout_11.addWidget(self.matingPoolSize, 2, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_11.addWidget(self.label_18, 4, 2, 1, 1)

        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_11.addWidget(self.label_19, 2, 2, 1, 1)

        self.selectionType = QComboBox(self.groupBox_5)
        self.selectionType.addItem("")
        self.selectionType.addItem("")
        self.selectionType.addItem("")
        self.selectionType.setObjectName(u"selectionType")

        self.gridLayout_11.addWidget(self.selectionType, 1, 1, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox_5, 0, 5, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.maxIter = QSpinBox(self.groupBox)
        self.maxIter.setObjectName(u"maxIter")
        sizePolicy4.setHeightForWidth(self.maxIter.sizePolicy().hasHeightForWidth())
        self.maxIter.setSizePolicy(sizePolicy4)
        self.maxIter.setMinimum(1)
        self.maxIter.setMaximum(9999999)
        self.maxIter.setValue(20)

        self.gridLayout.addWidget(self.maxIter, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.maxIterNoProgress = QSpinBox(self.groupBox)
        self.maxIterNoProgress.setObjectName(u"maxIterNoProgress")
        self.maxIterNoProgress.setMinimum(1)
        self.maxIterNoProgress.setMaximum(99999)
        self.maxIterNoProgress.setValue(100)

        self.gridLayout.addWidget(self.maxIterNoProgress, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 1, 3, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_12 = QGridLayout(self.groupBox_6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.unacceptableFixType = QComboBox(self.groupBox_6)
        self.unacceptableFixType.addItem("")
        self.unacceptableFixType.addItem("")
        self.unacceptableFixType.setObjectName(u"unacceptableFixType")

        self.gridLayout_12.addWidget(self.unacceptableFixType, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_6)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_12.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_6, 1, 5, 1, 1)

        self.tournamentBox = QGroupBox(self.tab)
        self.tournamentBox.setObjectName(u"tournamentBox")
        self.horizontalLayout_2 = QHBoxLayout(self.tournamentBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_17 = QLabel(self.tournamentBox)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_2.addWidget(self.label_17)

        self.tournamentSize = QSpinBox(self.tournamentBox)
        self.tournamentSize.setObjectName(u"tournamentSize")
        self.tournamentSize.setMinimum(2)

        self.horizontalLayout_2.addWidget(self.tournamentSize)


        self.gridLayout_2.addWidget(self.tournamentBox, 0, 6, 1, 1)

        self.penaltyBox = QGroupBox(self.tab)
        self.penaltyBox.setObjectName(u"penaltyBox")
        self.gridLayout_13 = QGridLayout(self.penaltyBox)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.penaltyMultiplierLast = QDoubleSpinBox(self.penaltyBox)
        self.penaltyMultiplierLast.setObjectName(u"penaltyMultiplierLast")
        self.penaltyMultiplierLast.setValue(1.000000000000000)

        self.gridLayout_13.addWidget(self.penaltyMultiplierLast, 2, 1, 1, 1)

        self.penaltyMultiplierFirst = QDoubleSpinBox(self.penaltyBox)
        self.penaltyMultiplierFirst.setObjectName(u"penaltyMultiplierFirst")
        self.penaltyMultiplierFirst.setValue(1.000000000000000)

        self.gridLayout_13.addWidget(self.penaltyMultiplierFirst, 1, 1, 1, 1)

        self.label_12 = QLabel(self.penaltyBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_13.addWidget(self.label_12, 1, 0, 1, 1)

        self.multiplierLastLabel = QLabel(self.penaltyBox)
        self.multiplierLastLabel.setObjectName(u"multiplierLastLabel")

        self.gridLayout_13.addWidget(self.multiplierLastLabel, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.penaltyBox, 1, 6, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.types = QWidget()
        self.types.setObjectName(u"types")
        self.types.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.types)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidgetCultTypes = QTabWidget(self.types)
        self.tabWidgetCultTypes.setObjectName(u"tabWidgetCultTypes")
        self.tabWidgetCultTypes.setTabShape(QTabWidget.Triangular)
        self.tabWidgetCultTypes.setTabsClosable(True)

        self.gridLayout_3.addWidget(self.tabWidgetCultTypes, 2, 0, 1, 1)

        self.frame_3 = QFrame(self.types)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy6)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addCultType = QPushButton(self.frame_3)
        self.addCultType.setObjectName(u"addCultType")
        sizePolicy4.setHeightForWidth(self.addCultType.sizePolicy().hasHeightForWidth())
        self.addCultType.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.addCultType)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 2, 1)

        self.tabWidget.addTab(self.types, "")
        self.fields = QWidget()
        self.fields.setObjectName(u"fields")
        self.fields.setFont(font1)
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
        sizePolicy4.setHeightForWidth(self.addField.sizePolicy().hasHeightForWidth())
        self.addField.setSizePolicy(sizePolicy4)

        self.horizontalLayout_6.addWidget(self.addField)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.tabWidgetFields = QTabWidget(self.fields)
        self.tabWidgetFields.setObjectName(u"tabWidgetFields")
        self.tabWidgetFields.setTabShape(QTabWidget.Triangular)
        self.tabWidgetFields.setTabsClosable(True)

        self.verticalLayout_8.addWidget(self.tabWidgetFields)

        self.tabWidget.addTab(self.fields, "")
        self.resources = QWidget()
        self.resources.setObjectName(u"resources")
        self.resources.setFont(font1)
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
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.dailyResources = QTableWidget(self.frame_8)
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
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.dailyResources.sizePolicy().hasHeightForWidth())
        self.dailyResources.setSizePolicy(sizePolicy7)
        self.dailyResources.horizontalHeader().setMinimumSectionSize(150)
        self.dailyResources.horizontalHeader().setStretchLastSection(True)
        self.dailyResources.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.dailyResources, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy5.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy5)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.addDailyResources = QPushButton(self.frame_7)
        self.addDailyResources.setObjectName(u"addDailyResources")

        self.verticalLayout_2.addWidget(self.addDailyResources)

        self.removeDailyResources = QPushButton(self.frame_7)
        self.removeDailyResources.setObjectName(u"removeDailyResources")

        self.verticalLayout_2.addWidget(self.removeDailyResources)


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
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.periodResources = QTableWidget(self.frame_9)
        if (self.periodResources.columnCount() < 2):
            self.periodResources.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.periodResources.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.periodResources.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        if (self.periodResources.rowCount() < 1):
            self.periodResources.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.periodResources.setVerticalHeaderItem(0, __qtablewidgetitem5)
        self.periodResources.setObjectName(u"periodResources")
        sizePolicy7.setHeightForWidth(self.periodResources.sizePolicy().hasHeightForWidth())
        self.periodResources.setSizePolicy(sizePolicy7)
        self.periodResources.horizontalHeader().setMinimumSectionSize(150)
        self.periodResources.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_7.addWidget(self.periodResources, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy5.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy5)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.addPeriodResources = QPushButton(self.frame_11)
        self.addPeriodResources.setObjectName(u"addPeriodResources")

        self.verticalLayout_4.addWidget(self.addPeriodResources)

        self.removePeriodResources = QPushButton(self.frame_11)
        self.removePeriodResources.setObjectName(u"removePeriodResources")

        self.verticalLayout_4.addWidget(self.removePeriodResources)


        self.gridLayout_7.addWidget(self.frame_11, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_9, 0, 1, 1, 1)

        self.tabWidget.addTab(self.resources, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1110, 22))
        self.menuinfo = QMenu(self.menubar)
        self.menuinfo.setObjectName(u"menuinfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuinfo.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidgetCultTypes.setCurrentIndex(-1)
        self.tabWidgetFields.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionlast_used.setText(QCoreApplication.translate("MainWindow", u"last used", None))
        self.actionset1.setText(QCoreApplication.translate("MainWindow", u"set1", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Mutation and crossover", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Crossover type", None))
        self.crossoverType.setItemText(0, QCoreApplication.translate("MainWindow", u"fields", None))
        self.crossoverType.setItemText(1, QCoreApplication.translate("MainWindow", u"days", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Mutation probability", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Initial population", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.initialPopulationType.setItemText(0, QCoreApplication.translate("MainWindow", u"empty solutions", None))
        self.initialPopulationType.setItemText(1, QCoreApplication.translate("MainWindow", u"partially filled solutions", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Population size", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Start date", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Days to optimize", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Selection", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Mating pool size", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Selection type", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Elite size", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"% of all", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"% of all", None))
        self.selectionType.setItemText(0, QCoreApplication.translate("MainWindow", u"roulette wheel", None))
        self.selectionType.setItemText(1, QCoreApplication.translate("MainWindow", u"tournament", None))
        self.selectionType.setItemText(2, QCoreApplication.translate("MainWindow", u"ranking", None))

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Stop conditions", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Max number of iterations", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max iterations no progress", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Dealing with unacceptable solutions", None))
        self.unacceptableFixType.setItemText(0, QCoreApplication.translate("MainWindow", u"penalty", None))
        self.unacceptableFixType.setItemText(1, QCoreApplication.translate("MainWindow", u"fixup", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.tournamentBox.setTitle(QCoreApplication.translate("MainWindow", u"Tournament", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Tournament size", None))
        self.penaltyBox.setTitle(QCoreApplication.translate("MainWindow", u"Penalty ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"multiplier at first iteration", None))
        self.multiplierLastLabel.setText(QCoreApplication.translate("MainWindow", u"multiplier at _ iteration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Control", None))
        self.addCultType.setText(QCoreApplication.translate("MainWindow", u"Add new cultivation type", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.types), QCoreApplication.translate("MainWindow", u"Cultivation types", None))
        self.addField.setText(QCoreApplication.translate("MainWindow", u"Add new field", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fields), QCoreApplication.translate("MainWindow", u"Fields", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Daily resources", None))
        ___qtablewidgetitem = self.dailyResources.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Resource name", None));
        ___qtablewidgetitem1 = self.dailyResources.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem2 = self.dailyResources.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.addDailyResources.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeDailyResources.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Entire period resources", None))
        ___qtablewidgetitem3 = self.periodResources.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Resource name", None));
        ___qtablewidgetitem4 = self.periodResources.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem5 = self.periodResources.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.addPeriodResources.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removePeriodResources.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resources), QCoreApplication.translate("MainWindow", u"Resources", None))
        self.menuinfo.setTitle(QCoreApplication.translate("MainWindow", u"info", None))
    # retranslateUi

