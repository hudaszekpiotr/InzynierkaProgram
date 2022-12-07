# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'field_type_tab.ui'
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
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(628, 281)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.coefficients = QTableWidget(Form)
        if (self.coefficients.columnCount() < 2):
            self.coefficients.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.coefficients.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.coefficients.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.coefficients.rowCount() < 1):
            self.coefficients.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.coefficients.setVerticalHeaderItem(0, __qtablewidgetitem2)
        self.coefficients.setObjectName(u"coefficients")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coefficients.sizePolicy().hasHeightForWidth())
        self.coefficients.setSizePolicy(sizePolicy)
        self.coefficients.horizontalHeader().setDefaultSectionSize(200)
        self.coefficients.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.coefficients, 2, 1, 2, 1)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addCoef = QPushButton(self.frame_4)
        self.addCoef.setObjectName(u"addCoef")
        sizePolicy1.setHeightForWidth(self.addCoef.sizePolicy().hasHeightForWidth())
        self.addCoef.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.addCoef)

        self.removeCoef = QPushButton(self.frame_4)
        self.removeCoef.setObjectName(u"removeCoef")
        sizePolicy1.setHeightForWidth(self.removeCoef.sizePolicy().hasHeightForWidth())
        self.removeCoef.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.removeCoef)


        self.gridLayout.addWidget(self.frame_4, 2, 2, 2, 1)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.label)

        self.name = QLineEdit(self.frame_2)
        self.name.setObjectName(u"name")
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 2)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.area = QSpinBox(self.frame_3)
        self.area.setObjectName(u"area")
        sizePolicy1.setHeightForWidth(self.area.sizePolicy().hasHeightForWidth())
        self.area.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.area)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.coefficients.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Cultivation type", None));
        ___qtablewidgetitem1 = self.coefficients.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Coefficient", None));
        ___qtablewidgetitem2 = self.coefficients.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Lp. 1", None));
        self.addCoef.setText(QCoreApplication.translate("Form", u"Add", None))
        self.removeCoef.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Area", None))
    # retranslateUi

