# This Python file uses the following encoding: utf-8
import copy
import json
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from src.optimization import Optimization
from src.utils import parse_resources, load_files
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
import ui_cult_type_tab
import ui_cult_type_stage
import ui_field_type_tab

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class FieldTypeTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_field_type_tab.Ui_Form()
        self.ui.setupUi(self)
        self.ui.addCoef.clicked.connect(self.add_coef)
        self.ui.removeCoef.clicked.connect(self.remove_coef)

    def add_coef(self):
        table = self.ui.coefficient
        table.insertRow(table.rowCount())

    def remove_coef(self):
        table = self.ui.coefficient
        table.removeRow(table.rowCount()-1)

class CultTypeStage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_cult_type_stage.Ui_Widget()
        self.ui.setupUi(self)
        self.ui.addResources.clicked.connect(self.add_daily_resource)
        self.ui.removeResources.clicked.connect(self.remove_daily_resource)

    def add_daily_resource(self):
        table = self.ui.dailyResources
        table.insertRow(table.rowCount())

    def remove_daily_resource(self):
        table = self.ui.dailyResources
        table.removeRow(table.rowCount()-1)

class CultTypeTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_cult_type_tab.Ui_Widget()
        self.ui.setupUi(self)
        self.ui.addPeriodResources.clicked.connect(self.add_period_resource)
        self.ui.removePeriodResources.clicked.connect(self.remove_period_resource)
        self.ui.tabWidgetStages.addTab(CultTypeStage(), "sds")
        self.ui.addStage.clicked.connect(self.add_stage)
        self.ui.removeStage.clicked.connect(self.remove_stage)

    def add_period_resource(self):
        table = self.ui.periodResources
        table.insertRow(table.rowCount())

    def remove_period_resource(self):
        table = self.ui.periodResources
        table.removeRow(table.rowCount()-1)

    def add_stage(self):
        self.ui.tabWidgetStages.addTab(CultTypeStage(), "sds")

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
        self.ui.removeCultType.clicked.connect(self.remove_cult_type)
        self.ui.addField.clicked.connect(self.add_field)
        self.ui.removeField.clicked.connect(self.remove_field)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        # self.setCentralWidget(sc)
        self.ui.verticalLayout_3.addWidget(sc)


    def run_optimization(self):
        self.save_data()
        self.optimization.evolution_algorithm()

    def save_data(self):
        for i in range(self.ui.tabWidgetCultTypes.count()):
            pass
            name = self.ui.tabWidgetCultTypes.widget(i).ui.name.text()
            print(name)



    def add_new_cult_type(self):
        self.ui.tabWidgetCultTypes.addTab(CultTypeTab(), "sds")

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
