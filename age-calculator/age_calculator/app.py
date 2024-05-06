import sys


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

        self.setWindowTitle("Age calculator")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Age Calculator")

        #Date(Birthday) input
        birth_layout = QVBoxLayout()
        birth_label = QLabel("Birthday: ")
        birth_box = QDateEdit()
        birth_layout.addWidget(birth_label)
        birth_layout.addWidget(birth_box)
       
        #Date(Given) input
        given_layout = QVBoxLayout()
        given_label = QLabel("Chosen date: ")
        given_box = QDateEdit()
        given_layout.addWidget(given_label)
        given_layout.addWidget(given_box)
        

        #add widgets & layout to main layout
        layout.addWidget(title_label)
        layout.addLayout(birth_layout)
        layout.addLayout(given_layout)
    
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
app.setStyle("Windows")
window = MainWindow()
window.show()

app.exec()
