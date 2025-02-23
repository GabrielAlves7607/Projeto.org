import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from login import UserDatabase  # Importando a classe UserDatabase do seu arquivo login.py

class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.db = UserDatabase()  # Instanciando a classe UserDatabase
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 400, 300)

        # Aplicar estilo escuro com detalhes azuis
        self.setStyleSheet("""
            QWidget {
                background-color: #2E3440;
                color: #ECEFF4;
            }
            QLabel {
                color: #ECEFF4;
            }
            QLineEdit {
                background-color: #4C566A;
                color: #ECEFF4;
                border: 1px solid #81A1C1;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                background-color: #81A1C1;
                color: #2E3440;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5E81AC;
            }
            QCheckBox {
                color: #ECEFF4;
            }
            QCheckBox::indicator {
                width: 15px;
                height: 15px;
                border: 1px solid #81A1C1;
                border-radius: 3px;
                background-color: #4C566A;
            }
            QCheckBox::indicator:checked {
                background-color: #81A1C1;
            }
        """)

        layout = QVBoxLayout()

        # Título "FAÇA SEU LOGIN"
        self.label_title = QLabel('FAÇA SEU LOGIN')
        self.label_title.setFont(QFont('Arial', 18, QFont.Bold))
        self.label_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_title)

        # Campo de Email
        self.label_email = QLabel('Email:')
        self.label_email.setFont(QFont('Arial', 12))
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText('email@dominio.com')
        layout.addWidget(self.label_email)
        layout.addWidget(self.input_email)

        # Campo de Senha
        self.label_password = QLabel('Senha:')
        self.label_password.setFont(QFont('Arial', 12))
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText('........')
        self.input_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)

        # Checkbox "Lembrar-me"
        self.checkbox_remember = QCheckBox('Lembrar-me')
        self.checkbox_remember.setFont(QFont('Arial', 10))
        layout.addWidget(self.checkbox_remember)

        # Botão "Entrar"
        self.button_login = QPushButton('Entrar')
        self.button_login.setFont(QFont('Arial', 12))
        self.button_login.clicked.connect(self.on_login)
        layout.addWidget(self.button_login)

        # Botão "Criar Conta"
        self.button_register = QPushButton('Criar Conta')
        self.button_register.setFont(QFont('Arial', 12))
        self.button_register.clicked.connect(self.on_register)
        layout.addWidget(self.button_register)

        self.setLayout(layout)

    def on_login(self):
        email = self.input_email.text()
        password = self.input_password.text()

        if not email or not password:
            QMessageBox.warning(self, 'Erro', 'Por favor, preencha todos os campos.')
            return

        if self.db.verify_user(email, password):
            QMessageBox.information(self, 'Sucesso', 'Login realizado com sucesso!')
        else:
            QMessageBox.warning(self, 'Erro', 'Credenciais inválidas.')

    def on_register(self):
        email = self.input_email.text()
        password = self.input_password.text()

        if not email or not password:
            QMessageBox.warning(self, 'Erro', 'Por favor, preencha todos os campos.')
            return

        if self.db.add_user(email, password):
            QMessageBox.information(self, 'Sucesso', f"Usuário '{email}' cadastrado com sucesso!")
        else:
            QMessageBox.warning(self, 'Erro', 'Nome de usuário já existe. Escolha outro nome.')

    def closeEvent(self, event):
        self.db.close()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_app = LoginApp()
    login_app.show()
    sys.exit(app.exec_())
