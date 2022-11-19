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

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class CultTypeTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_cult_type_tab.Ui_widget()
        self.ui.setupUi(self)




class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        resources, fields, cultivation_types = load_files()

        #self.ui.tabWidget_2.addTab(CultTypeTab(), "sds")


        self.optimization = Optimization(resources, fields, cultivation_types)
        self.ui.runButton.clicked.connect(self.run_optimization)
        self.ui.cultTypesPeriodResourcesAddRow.clicked.connect(self.add_new_resource)
        self.ui.cultTypesAddNewStage.clicked.connect(self.add_stage)
        self.ui.addType.clicked.connect(self.add_new_cult_type)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        # self.setCentralWidget(sc)
        self.ui.verticalLayout_3.addWidget(sc)


    def run_optimization(self):
        self.optimization.evolution_algorithm()

    def add_new_resource(self):
        table = self.ui.cultTypesPeriodResources
        self.ui.cultTypesPeriodResources.insertRow(table.rowCount())

    def add_stage(self):
        self.ui.stages.addTab(QWidget(), "new")

    def add_new_cult_type(self):
        self.ui.tabWidgetCultTypes.addTab(CultTypeTab(), "sds")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
