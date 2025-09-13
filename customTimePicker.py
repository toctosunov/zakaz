from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QComboBox,
    QDialogButtonBox, QLabel
)
from PyQt6.QtCore import QTime


class QTimePickerDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Выберите время")
        self.setMinimumWidth(400)

        # Заголовок
        self.label = QLabel("Выберите время:")

        # Комбобокс с временными интервалами
        self.time_combo = QComboBox()
        self.populate_times(step_minutes=60)  # шаг 15 минут

        # Кнопки ОК / Отмена
        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)


        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.time_combo)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def populate_times(self, step_minutes=15):
        times = []
        for hour in range(24):
            for minute in range(0, 60, step_minutes):
                time_str = f"{hour:02d}:{minute:02d}"
                times.append(time_str)
        self.time_combo.addItems(times)

    def selected_time(self) -> QTime:
        time_str = self.time_combo.currentText()
        return QTime.fromString(time_str, "HH:mm")
