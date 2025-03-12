import sys
from PyQt5.QtWidgets import *

# Classe principal da aplicação
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.modo_escuro = True  # Define o modo inicial como escuro
        self.initUI()  # Inicializa a interface do usuário
    

    def initUI(self):
        # Configurações iniciais da janela principal
        self.setWindowTitle("Sistema Completo com PyQt5")
        self.setGeometry(100, 100, 1200, 800)  # Define o tamanho da janela
        
        # Widget central que contém o layout principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Layout principal (vertical) para organizar os widgets
        self.layout = QVBoxLayout(self.central_widget)
        
        # Widget de pilha para alternar entre diferentes páginas
        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)

        # Cria instâncias das diferentes páginas da aplicação
        self.inicial_page = InicialApp()  # Página inicial
        self.tabela_page = TabelaApp()  # Página da tabela
        self.notificacoes_page = NotificacoesApp()  # Página de notificações
        self.em_andamento4_page = EmAndamento4App()  # Página em andamento 4
        self.em_andamento5_page = EmAndamento5App()  # Página em andamento 5
        self.config_page = ConfiguracoesApp()  # Página de configurações

        # Adiciona as páginas ao widget de pilha
        self.stack.addWidget(self.inicial_page)
        self.stack.addWidget(self.tabela_page)
        self.stack.addWidget(self.notificacoes_page)
        self.stack.addWidget(self.em_andamento4_page)
        self.stack.addWidget(self.em_andamento5_page)
        self.stack.addWidget(self.config_page)

        # Cria botões para navegação entre as páginas
        self.btn_inicial = QPushButton("Início")
        self.btn_tabela = QPushButton("Tabela")
        self.btn_notificacoes = QPushButton("Notificações")
        self.btn_em_andamento4 = QPushButton("Em andamento 4")
        self.btn_em_andamento5 = QPushButton("Em andamento 5")
        self.btn_config = QPushButton("Configurações")
        
        # Conecta os botões às funções para alternar as páginas
        self.btn_inicial.clicked.connect(lambda: self.stack.setCurrentWidget(self.inicial_page))
        self.btn_tabela.clicked.connect(lambda: self.stack.setCurrentWidget(self.tabela_page))
        self.btn_notificacoes.clicked.connect(lambda: self.stack.setCurrentWidget(self.notificacoes_page))
        self.btn_em_andamento4.clicked.connect(lambda: self.stack.setCurrentWidget(self.em_andamento4_page))
        self.btn_em_andamento5.clicked.connect(lambda: self.stack.setCurrentWidget(self.em_andamento5_page))
        self.btn_config.clicked.connect(lambda: self.stack.setCurrentWidget(self.config_page))

        # Layout horizontal para organizar os botões na parte inferior
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_inicial)
        button_layout.addWidget(self.btn_tabela)
        button_layout.addWidget(self.btn_notificacoes)
        button_layout.addWidget(self.btn_em_andamento4)
        button_layout.addWidget(self.btn_em_andamento5)
        button_layout.addWidget(self.btn_config)

        # Adiciona um espaçador para empurrar os botões para a esquerda
        button_layout.addStretch()

        # Adiciona o layout de botões na parte inferior do layout principal
        self.layout.addStretch()  # Adiciona um espaçador para empurrar os botões para baixo
        self.layout.addLayout(button_layout)

        # Aplica o tema escuro ao iniciar a aplicação
        self.aplicar_tema_escuro()


    def aplicar_tema_escuro(self):
        # Define o estilo do tema escuro
        estilo = """
        QWidget { background-color: #2E2E2E; color: white; }
        QPushButton { background-color: #444; color: white; border-radius: 5px; padding: 8px; }
        QPushButton:hover { background-color: #555; }
        QTableWidget { background-color: #3B3B3B; color: white; gridline-color: #555; }
        QHeaderView::section { background-color: #444; color: white; padding: 5px; }
        """
        
        # Aplica o estilo escuro à aplicação
        self.setStyleSheet(estilo)


    def closeEvent(self, event):
        # Exibe uma janela de confirmação antes de fechar a aplicação
        resposta = QMessageBox.question(self, "Sair", "Tem certeza que deseja sair?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resposta == QMessageBox.Yes:
            event.accept()  # Fecha a janela
        else:
            event.ignore()  # Mantém a janela aberta

# Páginas individuais da aplicação
class InicialApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Interface Inicial")
        label.setStyleSheet("font-size: 24px; font-weight: bold;")  # Aumenta o tamanho da fonte
        layout.addWidget(label)
        layout.addStretch()  # Adiciona um espaçador para ocupar o espaço restante


class TabelaApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        
        # Cria uma tabela com 3 colunas e 3 linhas
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["ID", "Nome", "Idade"])
        self.tabela.setRowCount(3)
        
        # Define o tamanho fixo da tabela para melhorar a visualização
        self.tabela.setFixedSize(1000, 600)  # Largura 1000px, altura 600px
        
        # Ajusta as larguras das colunas
        self.tabela.setColumnWidth(0, 300)  # Largura da Coluna 1 (ID)
        self.tabela.setColumnWidth(1, 350)  # Largura da Coluna 2 (Nome)
        self.tabela.setColumnWidth(2, 350)  # Largura da Coluna 3 (Idade)
        
        # Ajusta a altura das linhas
        self.tabela.setRowHeight(0, 50)
        self.tabela.setRowHeight(1, 50)
        self.tabela.setRowHeight(2, 50)
        
        # Adiciona dados na tabela
        dados = [("1", "Fulano", "25"), ("2", "Deltrano", "30"), ("3", "Ciclano", "22")]
        for row, (id_val, nome, idade) in enumerate(dados):
            self.tabela.setItem(row, 0, QTableWidgetItem(id_val))
            self.tabela.setItem(row, 1, QTableWidgetItem(nome))
            self.tabela.setItem(row, 2, QTableWidgetItem(idade))
        
        # Cria botões para manipulação da tabela
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
        
        # Layout horizontal para os botões da tabela
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_editar_cabecalhos)
        button_layout.addWidget(self.btn_adicionar_coluna)
        button_layout.addWidget(self.btn_adicionar_linha)
        button_layout.addWidget(self.btn_deletar_linha)
        button_layout.addWidget(self.btn_deletar_coluna)
        
        # Adiciona a tabela e os botões ao layout principal
        layout.addWidget(self.tabela)
        layout.addLayout(button_layout)
        

    def abrir_janela_edicao_cabecalhos(self):
        # Cria uma janela de diálogo para editar os cabeçalhos da tabela
        self.janela_edicao = QDialog(self)
        self.janela_edicao.setWindowTitle("Editar Cabeçalhos")
        layout = QVBoxLayout(self.janela_edicao)

        # Cria campos de texto para editar cada cabeçalho
        self.campos_cabecalhos = []
        for col in range(self.tabela.columnCount()):
            campo = QLineEdit(self.tabela.horizontalHeaderItem(col).text())
            layout.addWidget(QLabel(f"Cabeçalho {col + 1}:"))
            layout.addWidget(campo)
            self.campos_cabecalhos.append(campo)

        # Botão para aplicar as mudanças nos cabeçalhos
        btn_aplicar = QPushButton("Aplicar")
        btn_aplicar.clicked.connect(self.aplicar_mudancas_cabecalhos)
        layout.addWidget(btn_aplicar)

        self.janela_edicao.exec_()


    def aplicar_mudancas_cabecalhos(self):
        # Aplica as mudanças nos cabeçalhos da tabela
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
        # Remove a linha selecionada da tabela
        linha_selecionada = self.tabela.currentRow()
        if linha_selecionada >= 0:
            self.tabela.removeRow(linha_selecionada)


    def deletar_coluna(self):
        # Remove a coluna selecionada da tabela
        coluna_selecionada = self.tabela.currentColumn()
        if coluna_selecionada >= 0:
            self.tabela.removeColumn(coluna_selecionada)


class NotificacoesApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Sistema de Notificações"))  # Adiciona um rótulo à página de notificações


class EmAndamento4App(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Em Andamento 4"))  # Adiciona um rótulo à página em andamento 4


class EmAndamento5App(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Em Andamento 5"))  # Adiciona um rótulo à página em andamento 5


class ConfiguracoesApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Configurações do Sistema"))  # Adiciona um rótulo à página de configurações


# Inicialização da aplicação
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()  # Cria a janela principal
    window.show()  # Exibe a janela
    sys.exit(app.exec_())  # Executa o loop de eventos da aplicação
