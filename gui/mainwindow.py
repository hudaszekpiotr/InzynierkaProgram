# This Python file uses the following encoding: utf-8
import copy
import json
import os
import sys
from datetime import timedelta
from distinctipy import distinctipy

#from PyQt6.QtCore import QAbstractTableModel, Qt

from PySide6.QtCore import QRect, QDate, QModelIndex
from PySide6.QtGui import QIntValidator, QAction, QBrush, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStyledItemDelegate, QLineEdit, QDialog, \
    QDialogButtonBox, QVBoxLayout, QLabel, QFileDialog, QCheckBox
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
import ui_save_files

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
        self.colors = dict()

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]
        if role == Qt.BackgroundRole:
            color = self.colors.get((index.row(), index.column()))
            if color is not None:
                return color

    def rowCount(self, parent=QtCore.QModelIndex()):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, parent=QtCore.QModelIndex()):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def change_color(self, row, column, color):
        ix = self.index(row, column)
        self.colors[(row, column)] = color
        self.dataChanged.emit(ix, ix, (Qt.BackgroundRole,))


class Result(QWidget):
    def __init__(self, df, df_resources, cultivation_types, parent=None):
        super().__init__(parent)
        self.ui = ui_result.Ui_Form()
        self.ui.setupUi(self)
        self.table = QtWidgets.QTableView()
        self.df = df
        self.cultivation_types = cultivation_types
        self.df_resources = df_resources
        self.check_boxes = []
        #print(df)
        df = df.values.tolist()
        self.model = TableModel(df)
        self.table.setModel(self.model)
        self.table.resizeColumnsToContents()
        #self.model.change_color(1,1,QBrush(QColor(0, 0, 255, 127)))
        #print(self.table.rowAt(0))
        self.ui.topSpot.addWidget(self.table)

        self.sc = MplCanvas(self, width=5, height=4, dpi=100)

        #df_resources = df_resources[["water", "machine_1"]]
        print(df_resources)
        df_resources.plot(ax=self.sc.axes, kind="bar")

        #sc.axes.bar(langs, students)
        self.ui.bottomSpot.addWidget(self.sc)
        self.color_table()
        self.add_check_boxes()
        self.add_legend()

    def replot_resources(self):
        names = []
        for box in self.check_boxes:
            if box.isChecked():
                names.append(box.text())
        df_resources = self.df_resources[names]
        self.sc.axes.cla()
        df_resources.plot(ax=self.sc.axes, kind="bar")
        self.sc.draw()

    def add_check_boxes(self):
        for name in list(self.df_resources.columns):
            checkbox = QCheckBox(name, self.ui.scrollAreaWidgetContents)
            checkbox.setChecked(True)
            checkbox.stateChanged.connect(self.replot_resources)
            self.check_boxes.append(checkbox)
            self.ui.verticalLayout_2.addWidget(checkbox)

    def get_unique_types_list(self):
        values_list = []
        for index, row in self.df.iterrows():
            for col_index, i in enumerate(row):
                if i is not None and i != '' and i != ' ' and i not in values_list:
                    values_list.append(i)
        return values_list

    def add_legend(self):
        values_list = self.get_unique_types_list()
        table = self.ui.legend
        for value in values_list:
            table.insertRow(table.rowCount())
            item1 = QtWidgets.QTableWidgetItem(value)
            item2 = QtWidgets.QTableWidgetItem(self.cultivation_types[int(value)-1]["name"])
            table.setItem(table.rowCount() - 1, 0, item1)
            table.setItem(table.rowCount() - 1, 1, item2)

    def color_table(self):
        values_list = self.get_unique_types_list()
        num_colors= len(values_list)

        colors = distinctipy.get_colors(num_colors)

        for index, row in self.df.iterrows():
            for col_index, i in enumerate(row):
                if i is not None and i !='' and i != ' ':
                    color = colors[values_list.index(i)]
                    color = [int(c*255) for c in color]
                    self.model.change_color(index, col_index, QBrush(QColor(*color, 127)))


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

        self.ui.tabWidgetCultTypes.addTab(CultTypeTab(), "sds")
        self.ui.tabWidgetFields.addTab(FieldTypeTab(), "sds")
        self.ui.runButton.clicked.connect(self.run_optimization)
        self.ui.addCultType.clicked.connect(self.add_new_cult_type)
        self.ui.addField.clicked.connect(self.add_field)
        self.ui.addDailyResources.clicked.connect(self.add_daily_resources)
        self.ui.removeDailyResources.clicked.connect(self.remove_daily_resources)
        self.ui.addPeriodResources.clicked.connect(self.add_period_resources)
        self.ui.removePeriodResources.clicked.connect(self.remove_period_resources)
        # self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc = MplCanvas(self, width=4, height=3, dpi=80)
        #self.sc.axes.plot([0, 1, 2, 3, 4])

        self.ui.verticalLayout_3.addWidget(self.sc)

        self.result = None
        self.ui.tabWidgetCultTypes.tabCloseRequested.connect(self.ui.tabWidgetCultTypes.removeTab)
        self.ui.tabWidgetFields.tabCloseRequested.connect(self.ui.tabWidgetFields.removeTab)

        delegate = NumericDelegate(self.ui.dailyResources)
        self.ui.dailyResources.setItemDelegateForColumn(1, delegate)
        delegate = NumericDelegate(self.ui.periodResources)
        self.ui.periodResources.setItemDelegateForColumn(1, delegate)
        #self.ui.actionset1.triggered.connect(get_data_sets)
        #self.ui.actionsave.triggered.connect(self.save_data_to_file)

        save_action = QAction("save data", self)
        load_action = QAction("load data", self)
        save_action.triggered.connect(self.save_data_to_file)
        load_action.triggered.connect(self.load_data)
        self.ui.menubar.addAction(save_action)
        self.ui.menubar.addAction(load_action)
        self.ui.tournamentBox.hide()
        #self.ui.penaltyBox.hide()

        self.ui.selectionType.activated.connect(self.hide_show_tournament)
        self.ui.unacceptableFixType.activated.connect(self.hide_show_penalty)

        self.ui.maxIter.valueChanged.connect(self.change_label_multiplier)
        self.ui.multiplierLastLabel.setText("multiplier at " + str(self.ui.maxIter.value()) + " iteration")
        #self.sc.axes.plot([5, 6, 2, 3, 4, 7, 6, 6, 6, 6])
        #self.ui.verticalLayout_3.addWidget(self.sc)

    def change_label_multiplier(self):
        self.ui.multiplierLastLabel.setText("multiplier at " + str(self.ui.maxIter.value()) + " iteration")

    def hide_show_tournament(self):
        selection_type = self.ui.selectionType.currentText()
        if selection_type == "tournament":
            self.ui.tournamentBox.show()
        else:
            self.ui.tournamentBox.hide()

    def hide_show_penalty(self):
        unacceptable_fix_type = self.ui.unacceptableFixType.currentText()
        if unacceptable_fix_type == "penalty":
            self.ui.penaltyBox.show()
        else:
            self.ui.penaltyBox.hide()


    def save_data_to_file(self):
        filename = QFileDialog.getSaveFileName(self, 'Open file','../', "JSON files (*.json)")[0]
        self.save_data(filename)

    def plot(self, best_results):
        self.sc.axes.plot(best_results)
        self.ui.verticalLayout_3.addWidget(self.sc)

    def get_parameters(self):
        max_iter = self.ui.maxIter.value()
        max_iter_no_progress = self.ui.maxIterNoProgress.value()
        start_date = self.ui.startDate.date().toPython()
        num_days = self.ui.numDays.value()
        mutation_probability = self.ui.mutationProbability.value()
        crossover_type = self.ui.crossoverType.currentText()
        initial_population_type = self.ui.initialPopulationType.currentText()
        population_size = self.ui.populationSize.value()
        unacceptable_fix_type = self.ui.unacceptableFixType.currentText()
        penalty_multiplier_first = self.ui.penaltyMultiplierFirst.value()
        penalty_multiplier_last = self.ui.penaltyMultiplierLast.value()
        selection_type = self.ui.selectionType.currentText()
        mating_pool_size = self.ui.matingPoolSize.value()
        elite_size = self.ui.eliteSize.value()
        tournament_size = self.ui.tournamentSize.value()

        par = Parameters(max_iter=max_iter, max_iter_no_progress=max_iter_no_progress, start_date=start_date,
                         num_days=num_days, crossover_type=crossover_type, mutation_probability=mutation_probability,
                         initial_population_type=initial_population_type, population_size=population_size,
                         unacceptable_fix_type=unacceptable_fix_type, penalty_multiplier_first=penalty_multiplier_first,
                         penalty_multiplier_last=penalty_multiplier_last, selection_type=selection_type,
                         mating_pool_size=mating_pool_size, elite_size=elite_size, tournament_size=tournament_size)
        return par

    def run_optimization(self):
        par = self.get_parameters()
        self.save_data()
        resources, fields, cultivation_types = load_files()
        self.optimization = Optimization(resources, fields, cultivation_types)
        df, df_resources, best_results = self.optimization.evolution_algorithm(par)
        self.result = Result(df, df_resources, cultivation_types)
        self.result.setGeometry(QRect(100, 100, 800, 800))
        self.result.show()
        self.plot(best_results)


    def save_data(self, filename="../data/model_data.json"):

        fields = self.save_fields()
        resources = self.save_resources()
        cult_types = self.save_cultivation_types()
        model_data = {"fields": fields,
                      "resources": resources,
                      "cultivation_types": cult_types}

        model_data_json = json.dumps(model_data, indent=2)
        with open(filename, "w") as outfile:
            outfile.write(model_data_json)




    def load_data(self):
        #file_name = QFileDialog.getOpenFileName(self, 'Open file','../sample_data', "JSON files (*.json)")[0]
        file_name = "../sample_data/data1.json"
        if file_name == "":
            return 0
        with open(file_name, "r") as file:
            data = json.load(file)
        self.load_cultivation_types(data["cultivation_types"])
        self.load_fields_types(data["fields"])
        self.load_resources(data["resources"])

    def load_cultivation_types(self, cultivation_types_list):
        data = cultivation_types_list
        self.ui.tabWidgetCultTypes.removeTab(0)
        for i in data:
            tab = self.add_new_cult_type()
            tab.ui.name.setText(i["name"])
            tab.ui.profit.setValue(i["profit"])
            date = QDate(i["start_date"]["year"], i["start_date"]["month"], i["start_date"]["day"])
            tab.ui.startDate.setDate(date)
            tab.ui.plusMinus.setValue(i["start_date"]["plus_minus_days"])
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

    def load_fields_types(self, fields_types_list):
        data = fields_types_list
        self.ui.tabWidgetFields.removeTab(0)
        for i in data:
            field = self.add_field()
            field.ui.name.setText(i["name"])
            field.ui.area.setValue(i["area"])
            table = field.ui.coefficients
            table.removeRow(0)
            for row in i["coefficients"]:
                table.insertRow(table.rowCount())
                resource = QtWidgets.QTableWidgetItem(row)
                quantity = QtWidgets.QTableWidgetItem(str(i["coefficients"][row]))
                table.setItem(table.rowCount() - 1, 0, resource)
                table.setItem(table.rowCount() - 1, 1, quantity)

    def load_resources(self, resources_list):
        data = resources_list
        daily_resources = self.ui.dailyResources
        period_resources = self.ui.periodResources
        daily_resources.removeRow(0)
        period_resources.removeRow(0)

        for row in data["daily_resources"]:
            table = daily_resources
            table.insertRow(table.rowCount())
            resource = QtWidgets.QTableWidgetItem(row)
            quantity = QtWidgets.QTableWidgetItem(str(data["daily_resources"][row]))
            table.setItem(table.rowCount() - 1, 0, resource)
            table.setItem(table.rowCount() - 1, 1, quantity)

        for row in data["entire_period_resources"]:
            table = period_resources
            table.insertRow(table.rowCount())
            resource = QtWidgets.QTableWidgetItem(row)
            quantity = QtWidgets.QTableWidgetItem(str(data["entire_period_resources"][row]))
            table.setItem(table.rowCount() - 1, 0, resource)
            table.setItem(table.rowCount() - 1, 1, quantity)


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
            cultivation_types.append(new_type)

        return cultivation_types

    def save_fields(self):
        fields = []
        for i in range(self.ui.tabWidgetFields.count()):
            tab = self.ui.tabWidgetFields.widget(i).ui
            coefficients = {}
            for k in range(tab.coefficients.rowCount()):
                if tab.coefficients.item(k, 0) is not None and tab.coefficients.item(k, 1) is not None:
                    resource = tab.coefficients.item(k, 0).text()
                    value = float(tab.coefficients.item(k, 1).text())
                    coefficients[resource] = value

            new_type = {"name": tab.name.text(),
                        "area": tab.area.value(),
                        "coefficients": coefficients}

            fields.append(new_type)

        return fields

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

        return resources

    def add_new_cult_type(self):
        tab = CultTypeTab()
        self.ui.tabWidgetCultTypes.addTab(tab, "sds")
        return tab

    def remove_cult_type(self):
        index = self.ui.tabWidgetCultTypes.currentIndex()
        self.ui.tabWidgetCultTypes.removeTab(index)

    def add_field(self):
        field = FieldTypeTab()
        self.ui.tabWidgetFields.addTab(field, "sds")
        return field

    def remove_field(self):
        index = self.ui.tabWidgetFields.currentIndex()
        self.ui.tabWidgetFields.removeTab(index)

    def add_daily_resources(self):
        table = self.ui.dailyResources
        table.insertRow(table.rowCount())

    def remove_daily_resources(self):
        table = self.ui.dailyResources
        table.removeRow(table.rowCount()-1)

    def add_period_resources(self):
        table = self.ui.periodResources
        table.insertRow(table.rowCount())

    def remove_period_resources(self):
        table = self.ui.periodResources
        table.removeRow(table.rowCount()-1)

def get_data_sets():
    return next(os.walk('../data'))[1]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
