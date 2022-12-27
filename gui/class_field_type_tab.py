from PySide6.QtCore import QLocale
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit, QWidget

from gui import ui_field_type_tab


class NumericDelegateFloat(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegateFloat, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):
            validator = QDoubleValidator(-9.999, 9.999, 3, notation=QDoubleValidator.StandardNotation)
            validator.setLocale(QLocale.English)
            editor.setValidator(validator)
        return editor


class FieldTypeTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_field_type_tab.Ui_Form()
        self.ui.setupUi(self)
        self.ui.addCoef.clicked.connect(self.add_coefficient)
        self.ui.removeCoef.clicked.connect(self.remove_coefficient)
        delegate = NumericDelegateFloat(self.ui.coefficients)
        self.ui.coefficients.setItemDelegateForColumn(1, delegate)

    def add_coefficient(self):
        table = self.ui.coefficients
        table.insertRow(table.rowCount())

    def remove_coefficient(self):
        table = self.ui.coefficients
        rows = sorted(set(index.row() for index in table.selectedIndexes()), reverse=True)
        for row in rows:
            table.removeRow(row)
        if not rows:
            table.removeRow(table.rowCount() - 1)
