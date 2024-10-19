from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QFileDialog, QLabel, QMessageBox,
                             QFrame, QGraphicsDropShadowEffect)
from PyQt5.QtCore import pyqtSignal, Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QFont, QColor

class ModernButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(200, 50)
        self.setCursor(Qt.PointingHandCursor)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(10)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(self.shadow)

        self.animation = QPropertyAnimation(self, b"styleSheet")
        self.animation.setDuration(200)

    def enterEvent(self, event):
        self.animation.setStartValue(self.styleSheet())
        self.animation.setEndValue(self.styleSheet() + "background-color: #2980b9; transform: scale(1.05);")
        self.animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animation.setStartValue(self.styleSheet())
        self.animation.setEndValue(self.styleSheet().replace("background-color: #2980b9; transform: scale(1.05);", ""))
        self.animation.start()
        super().leaveEvent(event)

class MainWindow(QMainWindow):
    encrypt_signal = pyqtSignal(str, str)
    decrypt_signal = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure Image Processor")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c3e50;
            }
            QLabel {
                color: #ecf0f1;
                font-size: 16px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 25px;
                font-size: 16px;
                font-weight: bold;
            }
            QFrame {
                background-color: #34495e;
                border-radius: 10px;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Title
        title_label = QLabel("Secure Image Processor")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 28, QFont.Bold))
        title_label.setStyleSheet("color: #ecf0f1; margin: 20px 0;")
        main_layout.addWidget(title_label)

        # File selection frame
        file_frame = QFrame()
        file_layout = QVBoxLayout(file_frame)

        self.input_label = QLabel("Input: No file selected")
        file_layout.addWidget(self.input_label)

        self.output_label = QLabel("Output: No file selected")
        file_layout.addWidget(self.output_label)

        main_layout.addWidget(file_frame)

        # Buttons
        button_layout = QHBoxLayout()

        select_input_btn = ModernButton("Select Input")
        select_input_btn.clicked.connect(self.select_input_file)
        button_layout.addWidget(select_input_btn)

        select_output_btn = ModernButton("Select Output")
        select_output_btn.clicked.connect(self.select_output_file)
        button_layout.addWidget(select_output_btn)

        main_layout.addLayout(button_layout)

        action_layout = QHBoxLayout()

        encrypt_btn = ModernButton("Encrypt")
        encrypt_btn.clicked.connect(self.encrypt_image)
        action_layout.addWidget(encrypt_btn)

        decrypt_btn = ModernButton("Decrypt")
        decrypt_btn.clicked.connect(self.decrypt_image)
        action_layout.addWidget(decrypt_btn)

        main_layout.addLayout(action_layout)

        # Status label
        self.status_label = QLabel("Ready")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #bdc3c7; font-style: italic; margin-top: 20px;")
        main_layout.addWidget(self.status_label)

        self.input_path = ""
        self.output_path = ""

    def select_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Input Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            self.input_path = file_path
            self.input_label.setText(f"Input: {file_path}")
            self.status_label.setText("Input file selected")

    def select_output_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Select Output Location", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            self.output_path = file_path
            self.output_label.setText(f"Output: {file_path}")
            self.status_label.setText("Output location selected")

    def encrypt_image(self):
        if self.input_path and self.output_path:
            self.encrypt_signal.emit(self.input_path, self.output_path)
            self.status_label.setText("Encrypting...")
        else:
            self.show_error("Please select both input and output files.")

    def decrypt_image(self):
        if self.input_path and self.output_path:
            self.decrypt_signal.emit(self.input_path, self.output_path)
            self.status_label.setText("Decrypting...")
        else:
            self.show_error("Please select both input and output files.")

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)
        self.status_label.setText("Error occurred")

    def show_success(self, message):
        QMessageBox.information(self, "Success", message)
        self.status_label.setText("Operation completed successfully")