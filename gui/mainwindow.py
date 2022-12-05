# This Python file uses the following encoding: utf-8
import copy
import json
import sys
from datetime import timedelta

#from PyQt6.QtCore import QAbstractTableModel, Qt

from PySide6.QtCore import QRect
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStyledItemDelegate, QLineEdit
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from src.optimization import Optimization
from src.parameters import Parameters
from src.utils import parse_resources, load_files
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
import ui_cult_type_tab
import ui_cult_type_stage
import ui_field_type_tab
import ui_result

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):

            editor.setValidator(QIntValidator())
        return editor

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


class Result(QWidget):
    def __init__(self, df, df_resources, parent=None):
        super().__init__(parent)
        self.ui = ui_result.Ui_Form()
        self.ui.setupUi(self)
        self.table = QtWidgets.QTableView()
        df = df.values.tolist()
        self.model = TableModel(df)
        self.table.setModel(self.model)
        self.ui.topSpot.addWidget(self.table)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        #sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        #print(df_resources)
        df_resources.plot(ax=sc.axes, kind="bar")

        #sc.axes.bar(langs, students)
        self.ui.bottomSpot.addWidget(sc)


class FieldTypeTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_field_type_tab.Ui_Form()
        self.ui.setupUi(self)
        self.ui.addCoef.clicked.connect(self.add_coef)
        self.ui.removeCoef.clicked.connect(self.remove_coef)
        delegate = NumericDelegate(self.ui.coefficients)
        self.ui.coefficients.setItemDelegateForColumn(1, delegate)


    def add_coef(self):
        table = self.ui.coefficients
        table.insertRow(table.rowCount())

    def remove_coef(self):
        table = self.ui.coefficients
        table.removeRow(table.rowCount()-1)

class CultTypeStage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_cult_type_stage.Ui_Form()
        self.ui.setupUi(self)
        self.ui.addResources.clicked.connect(self.add_daily_resource)
        self.ui.removeResources.clicked.connect(self.remove_daily_resource)

        delegate = NumericDelegate(self.ui.resources)
        self.ui.resources.setItemDelegateForColumn(1, delegate)

    def add_daily_resource(self):
        table = self.ui.resources
        table.insertRow(table.rowCount())

    def remove_daily_resource(self):
        table = self.ui.resources
        table.removeRow(table.rowCount()-1)

class CultTypeTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_cult_type_tab.Ui_widget()
        self.ui.setupUi(self)
        self.ui.addPeriodResources.clicked.connect(self.add_period_resource)
        self.ui.removePeriodResources.clicked.connect(self.remove_period_resource)
        self.ui.tabWidgetStages.addTab(CultTypeStage(), "sds")
        self.ui.addStage.clicked.connect(self.add_stage)
        #self.ui.removeStage.clicked.connect(self.remove_stage)
        self.ui.tabWidgetStages.tabCloseRequested.connect(self.ui.tabWidgetStages.removeTab)

        delegate = NumericDelegate(self.ui.periodResources)
        self.ui.periodResources.setItemDelegateForColumn(1, delegate)
        self.ui.tabWidgetStages.widget(0).ui.duration.valueChanged.connect(self.sum_duration)



    def sum_duration(self):
        sum = 0
        for i in range(self.ui.tabWidgetStages.count()):
            tab_stages = self.ui.tabWidgetStages.widget(i).ui
            sum += tab_stages.duration.value()
        self.ui.duration.setText(str(sum))

    def add_period_resource(self):
        table = self.ui.periodResources
        table.insertRow(table.rowCount())

    def remove_period_resource(self):
        table = self.ui.periodResources
        table.removeRow(table.rowCount()-1)

    def add_stage(self):
        stage = CultTypeStage()
        self.ui.tabWidgetStages.addTab(stage, "sds")
        for i in range(self.ui.tabWidgetStages.count()):
            tab_stages = self.ui.tabWidgetStages.widget(i).ui
            tab_stages.duration.valueChanged.connect(self.sum_duration)
        return stage

    def remove_stage(self):
        index = self.ui.tabWidgetStages.currentIndex()
        self.ui.tabWidgetStages.removeTab(index)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        resources, fields, cultivation_types = load_files()

        self.ui.tabWidgetCultTypes.addTab(CultTypeTab(), "sds")
        self.ui.tabWidgetFields.addTab(FieldTypeTab(), "sds")


        self.optimization = Optimization(resources, fields, cultivation_types)
        self.ui.runButton.clicked.connect(self.run_optimization)

        self.ui.addCultType.clicked.connect(self.add_new_cult_type)
        #self.ui.removeCultType.clicked.connect(self.remove_cult_type)
        self.ui.addField.clicked.connect(self.add_field)
        #self.ui.removeField.clicked.connect(self.remove_field)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        #self.sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        # self.setCentralWidget(sc)
        self.ui.verticalLayout_3.addWidget(self.sc)
        self.result = None
        self.ui.tabWidgetCultTypes.tabCloseRequested.connect(self.ui.tabWidgetCultTypes.removeTab)
        self.ui.tabWidgetFields.tabCloseRequested.connect(self.ui.tabWidgetFields.removeTab)

        delegate = NumericDelegate(self.ui.dailyResources)
        self.ui.dailyResources.setItemDelegateForColumn(1, delegate)
        delegate = NumericDelegate(self.ui.periodResources)
        self.ui.periodResources.setItemDelegateForColumn(1, delegate)

    def plot(self, best_results):
        self.sc.axes.plot(best_results)
        # self.setCentralWidget(sc)
        self.ui.verticalLayout_3.addWidget(self.sc)

    def get_parameters(self):
        max_iter = self.ui.maxIter.value()
        par = Parameters(max_iter)
        return par

    def run_optimization(self):
        par = self.get_parameters()
        self.save_data()
        self.load_data()
        df, df_resources, best_results = self.optimization.evolution_algorithm(par)
        self.result = Result(df, df_resources)
        self.result.setGeometry(QRect(100, 100, 800, 800))
        self.result.show()
        self.plot(best_results)

    def save_data(self):
        self.save_fields()
        self.save_resources()
        self.save_cultivation_types()

    def load_data(self):
        self.load_cultivation_types()

    def load_cultivation_types(self):
        f = open('sample.json')
        data = json.load(f)
        self.ui.tabWidgetCultTypes.removeTab(0)
        for i in data:
            tab = self.add_new_cult_type()
            tab.ui.name.setText(i["name"])
            tab.ui.profit.setValue(i["profit"])
            table = tab.ui.periodResources
            table.removeRow(0)
            for row in i["entire_period_resources"]:
                table.insertRow(table.rowCount())
                resource = QtWidgets.QTableWidgetItem(row)
                quantity = QtWidgets.QTableWidgetItem(str(i["entire_period_resources"][row]))
                table.setItem(table.rowCount() - 1, 0, resource)
                table.setItem(table.rowCount() - 1, 1, quantity)

            tab.ui.tabWidgetStages.removeTab(0)
            for stage in i["daily_resources"]:
                new_stage = tab.add_stage()
                new_stage.ui.name.setText(stage["name"])
                new_stage.ui.duration.setValue(stage["duration"])
                table = new_stage.ui.resources
                table.removeRow(0)
                for row in stage["values"]:
                    table.insertRow(table.rowCount())
                    resource = QtWidgets.QTableWidgetItem(row)
                    quantity = QtWidgets.QTableWidgetItem(str(stage["values"][row]))
                    table.setItem(table.rowCount() - 1, 0, resource)
                    table.setItem(table.rowCount() - 1, 1, quantity)


        f.close()

    def save_cultivation_types(self):
        cultivation_types = []
        for i in range(self.ui.tabWidgetCultTypes.count()):
            tab = self.ui.tabWidgetCultTypes.widget(i).ui
            entire_period_resources = {}
            for k in range(tab.periodResources.rowCount()):
                if tab.periodResources.item(k, 0) is not None and tab.periodResources.item(k, 1) is not None:
                    resource = tab.periodResources.item(k, 0).text()
                    quantity = int(tab.periodResources.item(k, 1).text())
                    entire_period_resources[resource] = quantity
            #print(entire_period_resources)
            daily_resources = []

            for k in range(tab.tabWidgetStages.count()):
                tab_stages = tab.tabWidgetStages.widget(k).ui
                name = tab_stages.name.text()
                duration = tab_stages.duration.value()

                values = {}
                for j in range(tab_stages.resources.rowCount()):
                    if tab_stages.resources.item(j, 0) is not None and tab_stages.resources.item(j, 1) is not None:
                        resource = tab_stages.resources.item(j, 0).text()
                        quantity = int(tab_stages.resources.item(j, 1).text())
                        values[resource] = quantity

                resources = {"name": name,
                             "duration": duration,
                             "values": values}
                daily_resources.append(resources)

            #start_date_raw = tab.startDate.date().toPython() - timedelta(days=tab.plusMinus.value())
            start_date_raw = tab.startDate.date().toPython()
            start_date = {
                "year": start_date_raw.year,
                "month": start_date_raw.month,
                "day": start_date_raw.day,
                "plus_minus_days": tab.plusMinus.value()
            }
            new_type = {"name": tab.name.text(),
                        "profit": tab.profit.value(),
                        "duration": int(tab.duration.text()),
                        "start_date": start_date,
                        "entire_period_resources": entire_period_resources,
                        "daily_resources": daily_resources}
            #print(new_type)
            cultivation_types.append(new_type)

        json_object = json.dumps(cultivation_types, indent=2)
        with open("../data/cultivation_types.json", "w") as outfile:
            outfile.write(json_object)

    def save_fields(self):
        fields = []
        for i in range(self.ui.tabWidgetFields.count()):
            tab = self.ui.tabWidgetFields.widget(i).ui
            coefficients = {}
            for k in range(tab.coefficients.rowCount()):
                if tab.coefficients.item(k, 0) is not None and tab.coefficients.item(k, 1) is not None:
                    resource = tab.coefficients.item(k, 0).text()
                    value = int(tab.coefficients.item(k, 1).text())
                    coefficients[resource] = value

            new_type = {"name": tab.name.text(),
                        "area": tab.area.value(),
                        "coefficients": coefficients}

            fields.append(new_type)

        json_object = json.dumps(fields, indent=2)
        with open("../data/fields.json", "w") as outfile:
            outfile.write(json_object)

    def save_resources(self):
        daily_resources = {}
        entire_period_resources = {}

        for k in range(self.ui.dailyResources.rowCount()):
            resources = self.ui.dailyResources
            if resources.item(k, 0) is not None and resources.item(k, 1) is not None:
                resource = resources.item(k, 0).text()
                value = int(resources.item(k, 1).text())
                daily_resources[resource] = value

        for k in range(self.ui.periodResources.rowCount()):
            resources = self.ui.periodResources
            if resources.item(k, 0) is not None and resources.item(k, 1) is not None:
                resource = resources.item(k, 0).text()
                value = int(resources.item(k, 1).text())
                entire_period_resources[resource] = value

        resources = {"daily_resources": daily_resources,
                    "entire_period_resources": entire_period_resources}

        json_object = json.dumps(resources, indent=2)
        with open("../data/resources.json", "w") as outfile:
            outfile.write(json_object)



    def add_new_cult_type(self):
        tab = CultTypeTab()
        self.ui.tabWidgetCultTypes.addTab(tab, "sds")
        return tab

    def remove_cult_type(self):
        index = self.ui.tabWidgetCultTypes.currentIndex()
        self.ui.tabWidgetCultTypes.removeTab(index)

    def add_field(self):
        self.ui.tabWidgetFields.addTab(FieldTypeTab(), "sds")

    def remove_field(self):
        index = self.ui.tabWidgetFields.currentIndex()
        self.ui.tabWidgetFields.removeTab(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
