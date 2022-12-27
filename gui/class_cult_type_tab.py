from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QStyledItemDelegate, QLineEdit

from gui import ui_cult_type_tab
from gui.class_cult_type_stage import CultTypeStage


class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):
            editor.setValidator(QIntValidator(0, 999999))
        return editor

class CultTypeTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_cult_type_tab.Ui_widget()
        self.ui.setupUi(self)
        self.ui.addPeriodResources.clicked.connect(self.add_period_resource)
        self.ui.removePeriodResources.clicked.connect(self.remove_period_resource)
        self.ui.tabWidgetStages.addTab(CultTypeStage(), "stage 1")
        self.ui.addStage.clicked.connect(self.add_stage)
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
        rows = sorted(set(index.row() for index in table.selectedIndexes()), reverse=True)
        for row in rows:
            table.removeRow(row)
        if not rows:
            table.removeRow(table.rowCount() - 1)

    def add_stage(self):
        stage = CultTypeStage()
        count = self.ui.tabWidgetStages.count()
        self.ui.tabWidgetStages.addTab(stage, "stage " + str(count + 1))
        for i in range(self.ui.tabWidgetStages.count()):
            tab_stages = self.ui.tabWidgetStages.widget(i).ui
            tab_stages.duration.valueChanged.connect(self.sum_duration)
        return stage

    def remove_stage(self):
        index = self.ui.tabWidgetStages.currentIndex()
        self.ui.tabWidgetStages.removeTab(index)