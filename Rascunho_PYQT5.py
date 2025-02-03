import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QLabel, QMessageBox, QMainWindow, QStackedWidget

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.modo_escuro = False
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Sistema Completo com PyQt5")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        
        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)

        self.inicial_page = InicialApp()
        self.tabela_page = TabelaApp()
        self.notificacoes_page = NotificacoesApp()
        self.em_andamento4_page = EmAndamento4App()
        self.em_andamento5_page = EmAndamento5App()
        self.config_page = ConfiguracoesApp()

        self.stack.addWidget(self.inicial_page)
        self.stack.addWidget(self.tabela_page)
        self.stack.addWidget(self.notificacoes_page)
        self.stack.addWidget(self.em_andamento4_page)
        self.stack.addWidget(self.em_andamento5_page)
        self.stack.addWidget(self.config_page)

        self.btn_inicial = QPushButton("Início")
        self.btn_tabela = QPushButton("Tabela")
        self.btn_notificacoes = QPushButton("Notificações")
        self.btn_em_andamento4 = QPushButton("Em andamento 4")
        self.btn_em_andamento5 = QPushButton("Em andamento 5")
        self.btn_config = QPushButton("Configurações")
        self.btn_tema = QPushButton("Modo Escuro")

        self.btn_inicial.clicked.connect(lambda: self.stack.setCurrentWidget(self.inicial_page))
        self.btn_tabela.clicked.connect(lambda: self.stack.setCurrentWidget(self.tabela_page))
        self.btn_notificacoes.clicked.connect(lambda: self.stack.setCurrentWidget(self.notificacoes_page))
        self.btn_em_andamento4.clicked.connect(lambda: self.stack.setCurrentWidget(self.em_andamento4_page))
        self.btn_em_andamento5.clicked.connect(lambda: self.stack.setCurrentWidget(self.em_andamento5_page))
        self.btn_config.clicked.connect(lambda: self.stack.setCurrentWidget(self.config_page))
        self.btn_tema.clicked.connect(self.alternar_tema)

        button_layout = QGridLayout()
        button_layout.addWidget(self.btn_inicial, 0, 0)
        button_layout.addWidget(self.btn_tabela, 0, 1)
        button_layout.addWidget(self.btn_notificacoes, 0, 2)
        button_layout.addWidget(self.btn_em_andamento4, 1, 0)
        button_layout.addWidget(self.btn_em_andamento5, 1, 1)
        button_layout.addWidget(self.btn_config, 1, 2)
        button_layout.addWidget(self.btn_tema, 2, 1)
        
        self.layout.addLayout(button_layout)
    
    def alternar_tema(self):
        if self.modo_escuro:
            estilo = """
            QWidget { background-color: white; color: black; }
            QPushButton { background-color: #DDD; color: black; border-radius: 5px; padding: 8px; }
            QPushButton:hover { background-color: #BBB; }
            QTableWidget { background-color: white; color: black; gridline-color: #CCC; }
            QHeaderView::section { background-color: #EEE; color: black; padding: 5px; }
            """
            self.btn_tema.setText("Modo Escuro")
        else:
            estilo = """
            QWidget { background-color: #2E2E2E; color: white; }
            QPushButton { background-color: #444; color: white; border-radius: 5px; padding: 8px; }
            QPushButton:hover { background-color: #555; }
            QTableWidget { background-color: #3B3B3B; color: white; gridline-color: #555; }
            QHeaderView::section { background-color: #444; color: white; padding: 5px; }
            """
            self.btn_tema.setText("Modo Claro")
        
        self.setStyleSheet(estilo)
        self.modo_escuro = not self.modo_escuro

class InicialApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Interface Inicial"))

class TabelaApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["ID", "Nome", "Idade"])
        self.tabela.setRowCount(3)
        dados = [("1", "Fulano", "25"), ("2", "Deltrano", "30"), ("3", "Ciclano", "22")]
        for row, (id_val, nome, idade) in enumerate(dados):
            self.tabela.setItem(row, 0, QTableWidgetItem(id_val))
            self.tabela.setItem(row, 1, QTableWidgetItem(nome))
            self.tabela.setItem(row, 2, QTableWidgetItem(idade))
        layout.addWidget(self.tabela)

class NotificacoesApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Sistema de Notificações"))

class EmAndamento4App(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Em Andamento 4"))

class EmAndamento5App(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Em Andamento 5"))

class ConfiguracoesApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Configurações do Sistema"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
