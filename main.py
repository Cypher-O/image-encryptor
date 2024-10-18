import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from controller import Controller

def main():
    app = QApplication(sys.argv)
    view = MainWindow()
    controller = Controller(view)
    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()