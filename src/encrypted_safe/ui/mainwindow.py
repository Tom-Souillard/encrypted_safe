import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QLineEdit, QMessageBox
from encrypted_safe.core.file import File
from encrypted_safe.core.encryption_key import EncryptionKey

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Encrypted Safe')
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label for showing selected file path
        self.file_path_label = QLabel('No file selected')
        layout.addWidget(self.file_path_label)

        # Button to select file
        self.btn_select_file = QPushButton('Select File')
        self.btn_select_file.clicked.connect(self.select_file)
        layout.addWidget(self.btn_select_file)

        # Entry for encryption/decryption key
        self.key_entry = QLineEdit()
        self.key_entry.setPlaceholderText('Enter your encryption key here')
        layout.addWidget(self.key_entry)

        # Button to encrypt file
        self.btn_encrypt = QPushButton('Encrypt File')
        self.btn_encrypt.clicked.connect(self.encrypt_file)
        layout.addWidget(self.btn_encrypt)

        # Button to decrypt file
        self.btn_decrypt = QPushButton('Decrypt File')
        self.btn_decrypt.clicked.connect(self.decrypt_file)
        layout.addWidget(self.btn_decrypt)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select file")
        if file_path:
            self.file_path_label.setText(file_path)

    def encrypt_file(self):
        if not self.file_path_label.text() or self.file_path_label.text() == 'No file selected':
            QMessageBox.warning(self, 'Error', 'Please select a file first.')
            return
        encryption_key = EncryptionKey()
        file = File(self.file_path_label.text())
        file.encrypt(encryption_key)
        QMessageBox.information(self, 'Success', 'File encrypted successfully!')


    def decrypt_file(self):
        if not self.file_path_label.text() or self.file_path_label.text() == 'No file selected':
            QMessageBox.warning(self, 'Error', 'Please select a file first.')
            return
        encryption_key = EncryptionKey()
        file = File(self.file_path_label.text())
        file.decrypt(encryption_key)
        QMessageBox.information(self, 'Success', 'File decrypted successfully!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
