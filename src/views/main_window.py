from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox
from PyQt5.QtCore import pyqtSignal

class MainWindow(QMainWindow):
    encrypt_signal = pyqtSignal(str, str)
    decrypt_signal = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Encryptor/Decryptor")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.input_label = QLabel("No input file selected")
        layout.addWidget(self.input_label)

        self.output_label = QLabel("No output file selected")
        layout.addWidget(self.output_label)

        select_input_btn = QPushButton("Select Input Image")
        select_input_btn.clicked.connect(self.select_input_file)
        layout.addWidget(select_input_btn)

        select_output_btn = QPushButton("Select Output Location")
        select_output_btn.clicked.connect(self.select_output_file)
        layout.addWidget(select_output_btn)

        encrypt_btn = QPushButton("Encrypt")
        encrypt_btn.clicked.connect(self.encrypt_image)
        layout.addWidget(encrypt_btn)

        decrypt_btn = QPushButton("Decrypt")
        decrypt_btn.clicked.connect(self.decrypt_image)
        layout.addWidget(decrypt_btn)

        self.input_path = ""
        self.output_path = ""

    def select_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Input Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            self.input_path = file_path
            self.input_label.setText(f"Input: {file_path}")

    def select_output_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Select Output Location", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            self.output_path = file_path
            self.output_label.setText(f"Output: {file_path}")

    def encrypt_image(self):
        if self.input_path and self.output_path:
            self.encrypt_signal.emit(self.input_path, self.output_path)
        else:
            self.show_error("Please select both input and output files.")

    def decrypt_image(self):
        if self.input_path and self.output_path:
            self.decrypt_signal.emit(self.input_path, self.output_path)
        else:
            self.show_error("Please select both input and output files.")

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def show_success(self, message):
        QMessageBox.information(self, "Success", message)