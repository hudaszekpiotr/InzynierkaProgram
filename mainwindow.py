# This Python file uses the following encoding: utf-8
import json
import os
import sys

from PySide6.QtCore import QRect, QDate
from PySide6.QtGui import QIntValidator, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QStyledItemDelegate, QLineEdit, QFileDialog, QMessageBox
from PySide6 import QtWidgets


from gui.class_cult_type_tab import CultTypeTab
from gui.class_field_type_tab import FieldTypeTab
from gui.class_result import Result
from src.exceptions import NoValidCultivationTypesException
from src.optimization import Optimization
from src.parameters import Parameters
from gui.ui_form import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):
            editor.setValidator(QIntValidator(0, 999999))
        return editor


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Modeling and Optimization of Agricultural Production")
        self.ui.tabWidgetCultTypes.addTab(CultTypeTab(), "type 1")
        self.ui.tabWidgetFields.addTab(FieldTypeTab(), "field 1")
        self.ui.runButton.clicked.connect(self.run_optimization)
        self.ui.addCultType.clicked.connect(self.add_new_cult_type)
        self.ui.addField.clicked.connect(self.add_field)
        self.ui.addDailyResources.clicked.connect(self.add_daily_resources)
        self.ui.removeDailyResources.clicked.connect(self.remove_daily_resources)
        self.ui.addPeriodResources.clicked.connect(self.add_period_resources)
        self.ui.removePeriodResources.clicked.connect(self.remove_period_resources)
        self.sc = MplCanvas(self, width=5, height=3, dpi=80)
        self.ui.verticalLayout_3.addWidget(self.sc)
        self.result = None
        self.ui.tabWidgetCultTypes.tabCloseRequested.connect(self.ui.tabWidgetCultTypes.removeTab)
        self.ui.tabWidgetFields.tabCloseRequested.connect(self.ui.tabWidgetFields.removeTab)

        delegate = NumericDelegate(self.ui.dailyResources)
        self.ui.dailyResources.setItemDelegateForColumn(1, delegate)
        delegate = NumericDelegate(self.ui.periodResources)
        self.ui.periodResources.setItemDelegateForColumn(1, delegate)

        save_action = QAction("save data", self)
        load_action = QAction("load data", self)
        save_action.triggered.connect(self.save_data_to_file)
        load_action.triggered.connect(self.load_data)
        self.ui.menubar.addAction(save_action)
        self.ui.menubar.addAction(load_action)
        self.ui.tournamentBox.hide()
        self.ui.penaltyBox.hide()

        self.ui.selectionType.activated.connect(self.hide_show_tournament)
        self.ui.unacceptableFixType.activated.connect(self.hide_show_penalty)

        self.ui.maxIter.valueChanged.connect(self.change_label_multiplier)
        self.ui.multiplierLastLabel.setText("multiplier at " + str(self.ui.maxIter.value()) + " iteration")
        self.i = 0

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
        filename = QFileDialog.getSaveFileName(self, 'Open file', '.', "JSON files (*.json)")[0]
        self.save_data(filename)

    def plot(self, best_results):
        self.i += 1
        self.sc.axes.plot(best_results, label=f"run {self.i} - highest profit = {max(best_results)}")
        self.sc.axes.legend(loc="upper right")
        self.sc.axes.set_xlabel("iteration")
        self.sc.axes.set_ylabel("profit")
        self.ui.verticalLayout_3.addWidget(self.sc)

    def get_parameters(self):
        parameters = Parameters(max_iter=self.ui.maxIter.value(),
                                max_iter_no_progress=self.ui.maxIterNoProgress.value(),
                                start_date=self.ui.startDate.date().toPython(),
                                num_days=self.ui.numDays.value(),
                                crossover_type=self.ui.crossoverType.currentText(),
                                mutation_probability=self.ui.mutationProbability.value(),
                                initial_population_type=self.ui.initialPopulationType.currentText(),
                                population_size=self.ui.populationSize.value(),
                                unacceptable_fix_type=self.ui.unacceptableFixType.currentText(),
                                penalty_multiplier_first=self.ui.penaltyMultiplierFirst.value(),
                                penalty_multiplier_last=self.ui.penaltyMultiplierLast.value(),
                                selection_type=self.ui.selectionType.currentText(),
                                mating_pool_percent=self.ui.matingPoolSize.value(),
                                elite_percent=self.ui.eliteSize.value(),
                                tournament_size=self.ui.tournamentSize.value(),
                                mutation_type=self.ui.mutationType.currentText())
        return parameters

    def run_optimization(self):
        self.fix_resources()
        self.fix_coefficients()
        parameters = self.get_parameters()
        self.save_data()
        optimization = Optimization()
        try:
            df, df_resources, period_df, best_results = optimization.run_algorithm(parameters)
            self.result = Result(df, df_resources, period_df, optimization.cultivation_types)
            self.result.setGeometry(QRect(0, 0, 400, 400))
            self.result.show()
            self.plot(best_results)
        except NoValidCultivationTypesException:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("No valid cultivation types")
            dlg.setText("In selected time period there aren't any valid cultivation types")
            button = dlg.exec_()

    def save_data(self, filename="data/model_data.json"):
        if filename == '':
            return 0

        fields = self.save_fields()
        resources = self.save_resources()
        cult_types = self.save_cultivation_types()
        model_data = {"fields": fields,
                      "resources": resources,
                      "cultivation_types": cult_types}

        model_data_json = json.dumps(model_data, indent=2)

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as file:
            file.write(model_data_json)

    def load_data(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', '.', "JSON files (*.json)")[0]
        if file_name == "":
            return 0
        with open(file_name, "r") as file:
            try:
                data = json.load(file)
            except ValueError:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Invalid JSON")
                dlg.setText(f"""File is not a valid json file""")
                button = dlg.exec_()
                return 0

        self.ui.tabWidgetCultTypes.clear()
        self.ui.tabWidgetFields.clear()
        self.ui.dailyResources.setRowCount(0)
        self.ui.periodResources.setRowCount(0)

        valid_cult_types = 0
        if "cultivation_types" in data:
            valid_cult_types = self.load_cultivation_types(data["cultivation_types"])

        valid_fields = 0
        if "fields" in data:
            valid_fields = self.load_fields_types(data["fields"])

        valid_resource_types = 0
        if "resources" in data:
            valid_resource_types = self.load_resources(data["resources"])

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Loading summary")
        dlg.setText(
            f"Successfully loaded:\n{valid_cult_types} cultivation types\n{valid_fields} fields\n{valid_resource_types} resource types")
        button = dlg.exec()

    def load_cultivation_types(self, cultivation_types_list):
        data = cultivation_types_list

        valid = 0
        for i in data:
            try:
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
            except Exception as e:
                print(e)
            else:
                valid += 1
        return valid

    def load_fields_types(self, fields_types_list):
        data = fields_types_list
        valid = 0

        for i in data:
            try:
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
            except Exception as e:
                print(e)
            else:
                valid += 1
        return valid

    def load_resources(self, resources_list):
        data = resources_list
        daily_resources = self.ui.dailyResources
        period_resources = self.ui.periodResources
        daily_resources.removeRow(0)
        period_resources.removeRow(0)
        valid = 0

        if "daily_resources" in data:
            for row in data["daily_resources"]:
                try:
                    table = daily_resources
                    table.insertRow(table.rowCount())
                    resource = QtWidgets.QTableWidgetItem(row)
                    quantity = QtWidgets.QTableWidgetItem(str(data["daily_resources"][row]))
                    table.setItem(table.rowCount() - 1, 0, resource)
                    table.setItem(table.rowCount() - 1, 1, quantity)
                except Exception as e:
                    print(e)
                else:
                    valid += 1

        if "entire_period_resources" in data:
            for row in data["entire_period_resources"]:
                try:
                    table = period_resources
                    table.insertRow(table.rowCount())
                    resource = QtWidgets.QTableWidgetItem(row)
                    quantity = QtWidgets.QTableWidgetItem(str(data["entire_period_resources"][row]))
                    table.setItem(table.rowCount() - 1, 0, resource)
                    table.setItem(table.rowCount() - 1, 1, quantity)
                except Exception as e:
                    print(e)
                else:
                    valid += 1
        return valid

    def fix_resources(self):
        entire_period_resources_needed = set()
        daily_resources_needed = set()
        for i in range(self.ui.tabWidgetCultTypes.count()):
            tab = self.ui.tabWidgetCultTypes.widget(i).ui

            for k in range(tab.periodResources.rowCount()):
                if tab.periodResources.item(k, 0) is not None and tab.periodResources.item(k, 1) is not None:
                    resource = tab.periodResources.item(k, 0).text()
                    entire_period_resources_needed.add(resource)

            for k in range(tab.tabWidgetStages.count()):
                tab_stages = tab.tabWidgetStages.widget(k).ui
                for j in range(tab_stages.resources.rowCount()):
                    if tab_stages.resources.item(j, 0) is not None and tab_stages.resources.item(j, 1) is not None:
                        resource = tab_stages.resources.item(j, 0).text()
                        daily_resources_needed.add(resource)

        daily_resources_present = set()
        entire_period_resources_present = set()
        for k in range(self.ui.dailyResources.rowCount()):
            resources = self.ui.dailyResources
            if resources.item(k, 0) is not None and resources.item(k, 1) is not None:
                resource = resources.item(k, 0).text()
                daily_resources_present.add(resource)

        for k in range(self.ui.periodResources.rowCount()):
            resources = self.ui.periodResources
            if resources.item(k, 0) is not None and resources.item(k, 1) is not None:
                resource = resources.item(k, 0).text()
                entire_period_resources_present.add(resource)

        missing_period_resources = entire_period_resources_needed.difference(entire_period_resources_present)
        missing_daily_resources = daily_resources_needed.difference(daily_resources_present)

        if missing_period_resources or missing_daily_resources:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Missing resources")
            period_text = ''
            if missing_period_resources:
                period_text = f"Entire period resources - {missing_period_resources}"
            dlg.setText(f"""There are resources needed for cultivation types which are not present in resources tab\n
            Daily resources - {missing_daily_resources} {period_text} \nThose resources have been added with quantity 0""")
            button = dlg.exec_()

        for missing_period_resource in missing_period_resources:
            table = self.ui.periodResources
            table.insertRow(table.rowCount())
            table.setItem(table.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(missing_period_resource))
            table.setItem(table.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(str(0)))

        for missing_daily_resource in missing_daily_resources:
            table = self.ui.dailyResources
            table.insertRow(table.rowCount())
            table.setItem(table.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(missing_daily_resource))
            table.setItem(table.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(str(0)))

    def fix_coefficients(self):
        coefficients_needed = set()

        for i in range(self.ui.tabWidgetCultTypes.count()):
            tab = self.ui.tabWidgetCultTypes.widget(i).ui
            coefficients_needed.add(tab.name.text())

        missing_coefficients = []
        for i in range(self.ui.tabWidgetFields.count()):
            coefficients_present = set()
            tab = self.ui.tabWidgetFields.widget(i).ui
            for k in range(tab.coefficients.rowCount()):
                if tab.coefficients.item(k, 0) is not None and tab.coefficients.item(k, 1) is not None:
                    coefficients_present.add(tab.coefficients.item(k, 0).text())

            missing_coefficients.append(coefficients_needed.difference(coefficients_present))

        if any(missing_coefficients):
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Missing coefficients")
            dlg.setText(f"""There are cultivation types which are missing coefficients in fields tab. Those 
            coefficients have been added with value 1.""")
            button = dlg.exec_()

        for field_index, field in enumerate(missing_coefficients):
            tab = self.ui.tabWidgetFields.widget(field_index).ui
            table = tab.coefficients
            for coefficient in field:
                table.insertRow(table.rowCount())
                table.setItem(table.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(coefficient))
                table.setItem(table.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(str(1)))

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

            start_date_raw = tab.startDate.date().toPython()

            start_date = {"year": start_date_raw.year,
                          "month": start_date_raw.month,
                          "day": start_date_raw.day,
                          "plus_minus_days": tab.plusMinus.value()}
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
        count = self.ui.tabWidgetCultTypes.count()
        self.ui.tabWidgetCultTypes.addTab(tab, "type " + str(count + 1))
        return tab

    def remove_cult_type(self):
        index = self.ui.tabWidgetCultTypes.currentIndex()
        self.ui.tabWidgetCultTypes.removeTab(index)

    def add_field(self):
        field = FieldTypeTab()
        count = self.ui.tabWidgetFields.count()
        self.ui.tabWidgetFields.addTab(field, "field " + str(count + 1))
        return field

    def remove_field(self):
        index = self.ui.tabWidgetFields.currentIndex()
        self.ui.tabWidgetFields.removeTab(index)

    def add_daily_resources(self):
        table = self.ui.dailyResources
        table.insertRow(table.rowCount())

    def remove_daily_resources(self):
        table = self.ui.dailyResources
        rows = sorted(set(index.row() for index in table.selectedIndexes()), reverse=True)
        for row in rows:
            table.removeRow(row)
        if not rows:
            table.removeRow(table.rowCount() - 1)

    def add_period_resources(self):
        table = self.ui.periodResources
        table.insertRow(table.rowCount())

    def remove_period_resources(self):
        table = self.ui.periodResources
        rows = sorted(set(index.row() for index in table.selectedIndexes()), reverse=True)
        for row in rows:
            table.removeRow(row)
        if not rows:
            table.removeRow(table.rowCount() - 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Modeling and Optimization of Agricultural Production")
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
