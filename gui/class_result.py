
from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QWidget, QCheckBox, QTableView, QTableWidgetItem
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from distinctipy import distinctipy
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from gui import ui_result


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.colors = dict()

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        if role == Qt.BackgroundRole:
            color = self.colors.get((index.row(), index.column()))
            if color is not None:
                return color

    def rowCount(self, parent=QModelIndex()):

        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._data[0])

    def change_color(self, row, column, color):
        ix = self.index(row, column)
        self.colors[(row, column)] = color
        self.dataChanged.emit(ix, ix, (Qt.BackgroundRole,))


class Result(QWidget):
    def __init__(self, df, df_resources, period_df, cultivation_types, parent=None):
        super().__init__(parent)
        self.ui = ui_result.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Result window")
        self.table = QTableView()
        self.df = df
        self.cultivation_types = cultivation_types
        self.df_resources = df_resources
        self.check_boxes = []

        df = df.values.tolist()
        self.model = TableModel(df)
        self.table.setModel(self.model)
        self.table.resizeColumnsToContents()
        self.ui.topSpot.addWidget(self.table)

        self.sc = MplCanvas(self, width=5, height=4, dpi=90)
        self.sc_period = MplCanvas(self, width=3, height=2, dpi=70)

        if not df_resources.empty:
            df_resources.plot(ax=self.sc.axes, kind="bar")
        self.sc.axes.set_xlabel("days")
        self.sc.axes.set_ylabel("%")
        self.sc.axes.set_title("Used daily resources")

        if not period_df.empty:
            period_df.plot(ax=self.sc_period.axes, kind="bar")
        self.sc_period.axes.set_xticks([])
        self.sc_period.axes.set_title("Used period resources")
        self.sc_period.axes.set_ylabel("%")
        self.ui.bottomSpot.addWidget(self.sc)
        self.ui.periodSpot.addWidget(self.sc_period)
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
        self.sc.axes.set_xlabel("days")
        self.sc.axes.set_ylabel("%")
        self.sc.axes.set_title("Used daily resources")
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
            item1 = QTableWidgetItem(value)
            item2 = QTableWidgetItem(self.cultivation_types[int(value)]["name"])
            table.setItem(table.rowCount() - 1, 0, item1)
            table.setItem(table.rowCount() - 1, 1, item2)
        table.resizeColumnsToContents()
        table.verticalHeader().setVisible(False)

    def color_table(self):
        values_list = self.get_unique_types_list()
        num_colors = len(values_list)

        colors = distinctipy.get_colors(num_colors)

        for index, row in self.df.iterrows():
            for col_index, i in enumerate(row):
                if i is not None and i != '' and i != ' ':
                    color = colors[values_list.index(i)]
                    color = [int(c * 255) for c in color]
                    self.model.change_color(index, col_index, QBrush(QColor(*color, 127)))
