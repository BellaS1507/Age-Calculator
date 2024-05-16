import sys


from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import (
    QApplication,
    QDateEdit,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(" AN AGE CALCULATOR <3")
        self.setContentsMargins(12, 12, 12, 100)
        self.resize(320, 240)

        #Fonts
        self.set_fonts("lazy_dog.ttf")
        self.set_fonts("KidsCorner-Regular.ttf")
        self.set_fonts("MuseoSansRounded500.otf")

        layout = QVBoxLayout()
        title_label = QLabel("AN AGE CALCULATOR <3")
    
        title_label.setFont(QFont("Kids Corner", 22))

        #Date(Birthday) input
        birth_layout = QVBoxLayout()
        birth_label = QLabel("Birthday!: ")
        birth_label.setFont(QFont("Kids Corner", 15))
        birth_box = QDateEdit()
        birth_layout.addWidget(birth_label)
        birth_layout.addWidget(birth_box)
       
        #Date(Given) input
        given_layout = QVBoxLayout()
        given_label = QLabel("Given date: ")
        given_label.setFont(QFont("Kids Corner", 15))
        given_box = QDateEdit()
        given_layout.addWidget(given_label)
        given_layout.addWidget(given_box)

        #Buttons yipee
        cbutton_layout = QVBoxLayout()
        clear_button = QPushButton("Never mind :]")
        clear_button.setFont(QFont("Museo Sans Rounded"))
        cbutton_layout.addWidget(clear_button)

        

        #add widgets & layout to main layout
        layout.addWidget(title_label)
        layout.addLayout(birth_layout)
        layout.addLayout(given_layout)
        layout.addLayout(cbutton_layout)
    
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
    
    def set_fonts(self, font_name: str) -> None:
        font_dir = "Resorces/Fonts/"
        font_path = font_dir + font_name
        success = QFontDatabase.addApplicationFont(font_path)

        #if it failed to add the font
        if success == -1:
            print(f"{font_name} not loaded.\nTried path {font_path}")

app = QApplication(sys.argv)
stylesheet = None
styles_path = "Resorces/styles.qss"
#Stylesheet path
with open(styles_path, "r") as f:
    stylesheet = f.read()
app.setStyleSheet(stylesheet)



window = MainWindow()
window.show()

app.exec()
