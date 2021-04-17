import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculus')
        self.move(300, 100)
        self.resize(1400, 850)

        self.text_edit = QTextEdit()
        # self.text_edit.setAccleptRichText(False)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_edit)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 300)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MainApp()
   sys.exit(app.exec_())
