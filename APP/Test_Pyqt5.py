import sys
from PyQt5.QtWidgets import *

# Classe principal da aplicação
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.modo_escuro = False  # Variável para armazenar o estado do tema
        self.initUI()
    
    def initUI(self):
        # Configurações iniciais da janela
        self.setWindowTitle("Sistema Completo com PyQt5")
        self.setGeometry(100, 100, 1200, 800)  # Aumentei o tamanho da janela
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Layout principal (vertical)
        self.layout = QVBoxLayout(self.central_widget)
        
        # Criando um widget para alternar entre páginas
        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)

        # Criando instâncias das diferentes páginas da aplicação
        self.inicial_page = InicialApp()
        self.tabela_page = TabelaApp()
        self.notificacoes_page = NotificacoesApp()
        self.em_andamento4_page = EmAndamento4App()
        self.em_andamento5_page = EmAndamento5App()
        self.config_page = ConfiguracoesApp()

        # Adicionando as páginas ao stack de widgets
        self.stack.addWidget(self.inicial_page)
        self.stack.addWidget(self.tabela_page)
        self.stack.addWidget(self.notificacoes_page)
        self.stack.addWidget(self.em_andamento4_page)
        self.stack.addWidget(self.em_andamento5_page)
        self.stack.addWidget(self.config_page)

        # Criando botões para navegação entre as páginas
        self.btn_inicial = QPushButton("Início")
        self.btn_tabela = QPushButton("Tabela")
        self.btn_notificacoes = QPushButton("Notificações")
        self.btn_em_andamento4 = QPushButton("Em andamento 4")
        self.btn_em_andamento5 = QPushButton("Em andamento 5")
        self.btn_config = QPushButton("Configurações")
        self.btn_tema = QPushButton("Modo Escuro")

        # Conectando os botões às funções para alternar as páginas
        self.btn_inicial.clicked.connect(lambda: self.stack.setCurrentWidget(self.inicial_page))
        self.btn_tabela.clicked.connect(lambda: self.stack.setCurrentWidget(self.tabela_page))
        self.btn_notificacoes.clicked.connect(lambda: self.stack.setCurrentWidget(self.notificacoes_page))
        self.btn_em_andamento4.clicked.connect(lambda: self.stack.setCurrentWidget(self.em_andamento4_page))
        self.btn_em_andamento5.clicked.connect(lambda: self.stack.setCurrentWidget(self.em_andamento5_page))
        self.btn_config.clicked.connect(lambda: self.stack.setCurrentWidget(self.config_page))
        self.btn_tema.clicked.connect(self.alternar_tema)  # Alterna entre modo claro e escuro

        # Layout para organizar os botões na parte inferior (horizontal)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_inicial)
        button_layout.addWidget(self.btn_tabela)
        button_layout.addWidget(self.btn_notificacoes)
        button_layout.addWidget(self.btn_em_andamento4)
        button_layout.addWidget(self.btn_em_andamento5)
        button_layout.addWidget(self.btn_config)
        button_layout.addWidget(self.btn_tema)

        # Adicionando um espaçador para empurrar os botões para a esquerda
        button_layout.addStretch()

        # Adicionando o layout de botões na parte inferior do layout principal
        self.layout.addStretch()  # Adiciona um espaçador para empurrar os botões para baixo
        self.layout.addLayout(button_layout)
    
    def alternar_tema(self):
        # Alterna entre modo claro e escuro
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

# Páginas individuais da aplicação
class InicialApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Interface Inicial"))

class TabelaApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        
        # Tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["ID", "Nome", "Idade"])
        self.tabela.setRowCount(3)
        
        # Ajustando o tamanho da tabela
        self.tabela.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Adicionando dados na tabela
        dados = [("1", "Fulano", "25"), ("2", "Deltrano", "30"), ("3", "Ciclano", "22")]
        for row, (id_val, nome, idade) in enumerate(dados):
            self.tabela.setItem(row, 0, QTableWidgetItem(id_val))
            self.tabela.setItem(row, 1, QTableWidgetItem(nome))
            self.tabela.setItem(row, 2, QTableWidgetItem(idade))
        
        # Botões relacionados à tabela
        self.btn_editar_cabecalhos = QPushButton("Editar Cabeçalhos")
        self.btn_editar_cabecalhos.clicked.connect(self.abrir_janela_edicao_cabecalhos)
        
        self.btn_adicionar_coluna = QPushButton("Adicionar Coluna")
        self.btn_adicionar_coluna.clicked.connect(self.adicionar_coluna)
        
        self.btn_adicionar_linha = QPushButton("Adicionar Linha")
        self.btn_adicionar_linha.clicked.connect(self.adicionar_linha)
        
        self.btn_deletar_linha = QPushButton("Deletar Linha")
        self.btn_deletar_linha.clicked.connect(self.deletar_linha)
        
        self.btn_deletar_coluna = QPushButton("Deletar Coluna")
        self.btn_deletar_coluna.clicked.connect(self.deletar_coluna)
        
        # Layout para os botões da tabela
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_editar_cabecalhos)
        button_layout.addWidget(self.btn_adicionar_coluna)
        button_layout.addWidget(self.btn_adicionar_linha)
        button_layout.addWidget(self.btn_deletar_linha)
        button_layout.addWidget(self.btn_deletar_coluna)
        
        # Adicionando a tabela e os botões ao layout principal
        layout.addWidget(self.tabela)
        layout.addLayout(button_layout)

    def abrir_janela_edicao_cabecalhos(self):
        # Janela para editar cabeçalhos
        self.janela_edicao = QDialog(self)
        self.janela_edicao.setWindowTitle("Editar Cabeçalhos")
        layout = QVBoxLayout(self.janela_edicao)

        # Campos de texto para editar cada cabeçalho
        self.campos_cabecalhos = []
        for col in range(self.tabela.columnCount()):
            campo = QLineEdit(self.tabela.horizontalHeaderItem(col).text())
            layout.addWidget(QLabel(f"Cabeçalho {col + 1}:"))
            layout.addWidget(campo)
            self.campos_cabecalhos.append(campo)

        # Botão para aplicar as mudanças
        btn_aplicar = QPushButton("Aplicar")
        btn_aplicar.clicked.connect(self.aplicar_mudancas_cabecalhos)
        layout.addWidget(btn_aplicar)

        self.janela_edicao.exec_()

    def aplicar_mudancas_cabecalhos(self):
        # Aplica as mudanças nos cabeçalhos
        for col, campo in enumerate(self.campos_cabecalhos):
            self.tabela.setHorizontalHeaderItem(col, QTableWidgetItem(campo.text()))
        self.janela_edicao.close()

    def adicionar_coluna(self):
        # Adiciona uma nova coluna à tabela
        coluna_atual = self.tabela.columnCount()
        self.tabela.setColumnCount(coluna_atual + 1)
        self.tabela.setHorizontalHeaderItem(coluna_atual, QTableWidgetItem(f"Coluna {coluna_atual + 1}"))

    def adicionar_linha(self):
        # Adiciona uma nova linha à tabela
        linha_atual = self.tabela.rowCount()
        self.tabela.setRowCount(linha_atual + 1)

    def deletar_linha(self):
        # Deleta a linha selecionada
        linha_selecionada = self.tabela.currentRow()
        if linha_selecionada >= 0:
            self.tabela.removeRow(linha_selecionada)

    def deletar_coluna(self):
        # Deleta a coluna selecionada
        coluna_selecionada = self.tabela.currentColumn()
        if coluna_selecionada >= 0:
            self.tabela.removeColumn(coluna_selecionada)

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

# Inicialização da aplicação
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
