import sys
import theme
import CreatWidget
import customTimePicker
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout, QDateEdit, 
    QFrame, QDialog, QFileDialog,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

complitedBool = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1920, 1080)
        self.setWindowTitle("Заказ тортов")
        self.showMaximized()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        self.current_theme = "dark"  # стартовая тема
        self.apply_theme(self.current_theme)


        leftLayoutBorder = QFrame()
        leftLayoutBorder.setStyleSheet("""
            QFrame {
                border: 2px solid grey;
                border-radius: 5px;
            }
        """)

        RightLayoutBorder = QFrame()
        RightLayoutBorder.setStyleSheet("""
            QFrame {
                border: 2px solid grey;
                border-radius: 5px;
            }
        """)

#region левая часть экрана
        left_layout = QVBoxLayout()
        left_layout.setSpacing(20)
        left_layout.setContentsMargins(20, 0, 20, 360)

        leftLayoutBorder.setLayout(left_layout)
        main_layout.addWidget(leftLayoutBorder, 20)

        self.title = CreatWidget.create_label("Данные получателя: ", 30)
        self.fullname = CreatWidget.create_line_edit("Введите ФИО:")

        fullnamLayout = CreatWidget.create_layout("v", [self.title, self.fullname])
        fullnamLayout.setSpacing(10)
        left_layout.addLayout(fullnamLayout)

        self.phoneNumber = CreatWidget.create_line_edit("Введите телефон номера: ")
        left_layout.addWidget(self.phoneNumber)

        self.adress = CreatWidget.create_line_edit("Адрес: ")
        left_layout.addWidget(self.adress)

        self.gender = CreatWidget.create_combo_box(["Мужчина", "Женщина"])
        left_layout.addWidget(self.gender)

        self.group = CreatWidget.create_combo_box(["Жалал-Абад", "Ош"])
        left_layout.addWidget(self.group)

        self.birthday = QDateEdit()
        self.birthday.setCalendarPopup(True)
        self.birthday.setFixedHeight(50)
        left_layout.addWidget(self.birthday)
#endregion
        
#region правая часть
        right_layout = QVBoxLayout()
        right_layout.setSpacing(20)
        RightLayoutBorder.setLayout(right_layout)

        main_layout.addWidget(RightLayoutBorder, 80) 

        tabsLayout = QHBoxLayout()

        self.call = CreatWidget.create_Button("Звонок", self.toggle_theme)
        tabsLayout.addWidget(self.call)

        self.market = CreatWidget.create_Button("Магазин", self.toggle_theme)
        tabsLayout.addWidget(self.market)

        self.socialNetwork = CreatWidget.create_Button("Соц. сети", self.toggle_theme)
        tabsLayout.addWidget(self.socialNetwork)

        self.personal = CreatWidget.create_Button("Сотрудник", self.toggle_theme)
        tabsLayout.addWidget(self.personal)

        dateTimeLayout = QHBoxLayout()

        self.dateAndTimeText = CreatWidget.create_label("Дата и время: ", 50)
        dateTimeLayout.addWidget(self.dateAndTimeText)

        self.date = QDateEdit()
        self.date.setFixedHeight(50)
        self.date.setCalendarPopup(True)
        self.date.setFixedWidth(150)
        dateTimeLayout.addWidget(self.date)

        self.timeButton = CreatWidget.create_Button("00:00", self.open_time_picker, 50)
        dateTimeLayout.addWidget(self.timeButton)

        self.checkComplited = CreatWidget.create_check_box("Не выполнено   ×", "Выполнено   ✓", 50)
        dateTimeLayout.addWidget(self.checkComplited)

        self.Quantity = CreatWidget.create_line_edit("Количество(Вес):", 50)
        self.Price = CreatWidget.create_line_edit("Цена", 50)
        self.Price.textChanged.connect(self.countSum)
        self.Sum = CreatWidget.create_line_edit("Сумма", 50)
        self.Services = CreatWidget.create_line_edit("Услуги", 50)
        self.Total = CreatWidget.create_line_edit("Итого", 50)

        SumLayout = CreatWidget.create_layout("h", [self.Quantity, self.Price, self.Sum, self.Services, self.Total])

        appbarLayout = QVBoxLayout()
        appbarLayout.addLayout(tabsLayout)
        appbarLayout.addLayout(dateTimeLayout)
        appbarLayout.addLayout(SumLayout)
        appbarBorder = QFrame()
        appbarBorder.setStyleSheet("""
            border: 2px solid grey; 
            border-radius: 5px; 
            """
        )
        appbarBorder.setContentsMargins(30, 0, 0, 0)
        appbarBorder.setLayout(appbarLayout)
        right_layout.addWidget(appbarBorder)

        productTypeLayout = QVBoxLayout()
        productTypeLayout.setSpacing(20)
        productTypeLayout.setContentsMargins(30, 30, 30, 30)

        self.template = "Тема: {Theme}, Шаблон: {Sample}, Форма: {Form}, Начинка: {Beginning}"
        self.values = {"Theme": "", "Sample": "", "Form": "", "Beginning": ""}

        # productTypeLayout.addWidget(CreatWidget.create_label("Тема:"))
        self.cakeTheme = CreatWidget.create_combo_box([" ", "Свадьба", "День рождения"])
        self.cakeTheme.currentTextChanged.connect(lambda text: self.update_text("Theme", text))
        productTypeLayout.addWidget(self.cakeTheme)

        # productTypeLayout.addWidget(CreatWidget.create_label("Шаблон"))
        self.cakeSample = CreatWidget.create_combo_box([" ", "Эксклюзив"])
        self.cakeSample.currentTextChanged.connect(lambda text: self.update_text("Sample", text))
        productTypeLayout.addWidget(self.cakeSample)

        # productTypeLayout.addWidget(CreatWidget.create_label("Форма:"))
        self.cakeForm = CreatWidget.create_combo_box([" ", "Круглый", "Квадратный"])
        self.cakeForm.currentTextChanged.connect(lambda text: self.update_text("Form", text))
        productTypeLayout.addWidget(self.cakeForm)

        # productTypeLayout.addWidget(CreatWidget.create_label("Начинка:"))
        self.cakeBeginning = CreatWidget.create_combo_box([" ", "Каймачный"])
        self.cakeBeginning.currentTextChanged.connect(lambda text: self.update_text("Beginning", text))
        productTypeLayout.addWidget(self.cakeBeginning)

        self.productCount = CreatWidget.create_line_edit("Количество(Вес)")
        self.productCount.textChanged.connect(self.countSum)
        productTypeLayout.addWidget(self.productCount)

        self.photoCheckBox = CreatWidget.create_check_box("Строго как на фото ✓", "Строго как на фото ×", 50)
        productTypeLayout.addWidget(self.photoCheckBox)

        self.ImageLabel = CreatWidget.create_label("+", 150, 150)
        self.ImageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ImageLabel.mousePressEvent = self.openImage
        productTypeLayout.addWidget(self.ImageLabel)

        self.clearImageLabel = CreatWidget.create_Button("Очистить фото", self.clearImage, 50)
        productTypeLayout.addWidget(self.clearImageLabel)

        self.commentText = CreatWidget.create_line_edit("Коментарий", 200)
        self.commentSample = CreatWidget.create_line_edit("", 500)
        commentLayout = CreatWidget.create_layout("v", [self.commentText, self.commentSample])

        DescriptionLayout = QHBoxLayout()
        # DescriptionLayout.setContentsMargins(30, 0, 0, 0)
        productTypeBorder = QFrame()
        productTypeBorder.setLayout(productTypeLayout)
        DescriptionLayout.addWidget(productTypeBorder)
        # DescriptionLayout.addLayout(productTypeLayout)
        DescriptionLayout.addLayout(commentLayout)
        right_layout.addLayout(DescriptionLayout)

#endregion

    def countSum(self):
        try:
            count = int(self.productCount.toPlainText())
            price = int(self.Price.toPlainText())
            summa = count * price
            self.Sum.setText(str(summa))  # Преобразуем в строку
        except ValueError:
            self.Sum.setText("Ошибка ввода")


    def update_text(self, key, value):
        self.values[key] = value
        self.update_output()

    def update_output(self):
        text = self.template.format(**self.values)
        self.commentSample.setText(text)

    def clearImage(self):
        self.ImageLabel.clear()
        self.ImageLabel.setText("↺")

    def openImage(self, event):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение",
            "",
            "Изображения (*.png *.jpg *.jpeg *.bmp *.gif)"
        )

        if file_path:
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                self.ImageLabel.setPixmap(pixmap)
            else:
                self.ImageLabel.setText("Не удалось загрузить изображение.")
        else:
            self.ImageLabel.setText("+")


    def open_time_picker(self):
        dialog = customTimePicker.QTimePickerDialog()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            time = dialog.selected_time()
            self.timeButton.setText(time.toString("HH:mm"))


    def toggle_theme(self):
        if self.current_theme == "dark":
            self.current_theme = "light"
        else:
            self.current_theme = "dark"
        self.apply_theme(self.current_theme)

    def apply_theme(self, theme_name):
        if theme_name == "dark":
            self.setStyleSheet(theme.DARK_THEME)
        else:
            self.setStyleSheet(theme.LIGHT_THEME)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
