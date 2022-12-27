from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QStyledItemDelegate, QLineEdit

from gui import ui_cult_type_stage


class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):
            editor.setValidator(QIntValidator(0, 999999))
        return editor


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
        rows = sorted(set(index.row() for index in table.selectedIndexes()), reverse=True)
        for row in rows:
            table.removeRow(row)
        if not rows:
            table.removeRow(table.rowCount() - 1)
