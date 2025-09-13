from PyQt6.QtWidgets import (
    QLineEdit, QComboBox, QLabel,
    QPushButton, QHBoxLayout, QVBoxLayout,
    QTextEdit
)

def create_line_edit(placeholder: str, height: int = 50, width: int = None, enabled: bool = True) -> QTextEdit:
    line_edit = QTextEdit()
    if width is not None:
        line_edit.setFixedSize(width, height)
    else:
        line_edit.setFixedHeight(height)
    line_edit.setPlaceholderText(placeholder)
    line_edit.setEnabled(enabled)
    return line_edit

def create_label(text: str, height: int = 50, width: int = None) -> QLabel:
    label = QLabel()
    if width is not None:
        label.setMaximumSize(width, height)
    else:
        label.setFixedHeight(height)
    label.setText(text)
    return label

def create_Button(text: str, click, height: int = 50, width: int = None) -> QPushButton:
    button = QPushButton()
    if width is not None:
        button.setFixedSize(width, height)
    else:
        button.setFixedHeight(height)
    button.setText(text)
    button.clicked.connect(click)
    return button

isClicked = False

def create_check_box(text1: str = "✓", text2: str = " ", height: int = 50) -> QPushButton:
    button = QPushButton()
    button.setFixedHeight(height)

    # Изначальное состояние
    button.setText(text2)

    def toggle():
        global isClicked
        isClicked = not isClicked
        button.setText(text1 if isClicked else text2) 

    button.clicked.connect(toggle)
    return button

def create_layout(orientation: str, widgets: list) -> QHBoxLayout:
    if orientation == "v":
        layout = QVBoxLayout()
    elif orientation == "h":
        layout = QHBoxLayout()
    for widget in widgets:
        layout.addWidget(widget)
    
    
    return layout

def create_combo_box(items: list, height: int = 50, width: int = None) -> QComboBox:
    combo = QComboBox()
    if width is not None:
        combo.setFixedSize(width, height)
    else:
        combo.setFixedHeight(height)
    combo.addItems(items)
    return combo
