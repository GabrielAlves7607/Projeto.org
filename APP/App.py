import sys
import os
import threading
import requests
import pandas as pd
import PyPDF2
from PIL import Image

# PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QStackedWidget, QMessageBox, QTableWidget,
    QTableWidgetItem, QLineEdit, QDialog, QFileDialog, QFrame,
    QTextEdit
)



# === CLASSE PRINCIPAL DA APLICAÇÃO ===
class MainApp(QMainWindow):
    """
    Classe principal responsável pela janela e pela navegação entre páginas do sistema.
    """

    def __init__(self):
        super().__init__()
        self.modo_escuro = True  # Define se o tema escuro está ativado
        self.initUI()  # Inicializa a interface gráfica

    def initUI(self):
        """
        Método responsável por configurar toda a interface gráfica da aplicação.
        """
        self.setWindowTitle("Sistema Completo com PyQt5")
        self.setGeometry(100, 100, 1200, 800)

        # Define o widget central da janela
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout principal vertical
        self.layout = QVBoxLayout(self.central_widget)

        # Widget de páginas empilhadas para navegação
        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)

        # Instancia cada página da aplicação
        self.inicial_page = InicialApp()
        self.tabela_page = TabelaApp()
        self.notificacoes_page = ConversãoApp()
        self.em_andamento4_page = ChatBotIAApp()

        # Adiciona páginas ao stack
        self.stack.addWidget(self.inicial_page)
        self.stack.addWidget(self.tabela_page)
        self.stack.addWidget(self.notificacoes_page)
        self.stack.addWidget(self.em_andamento4_page)

        # Criação de botões para navegação
        self.btn_inicial = QPushButton("Início")
        self.btn_tabela = QPushButton("Tabela")
        self.btn_notificacoes = QPushButton("Conversor")
        self.btn_em_andamento4 = QPushButton("ChatBot")

        # Conecta os botões às páginas
        self.btn_inicial.clicked.connect(lambda: self.stack.setCurrentWidget(self.inicial_page))
        self.btn_tabela.clicked.connect(lambda: self.stack.setCurrentWidget(self.tabela_page))
        self.btn_notificacoes.clicked.connect(lambda: self.stack.setCurrentWidget(self.notificacoes_page))
        self.btn_em_andamento4.clicked.connect(lambda: self.stack.setCurrentWidget(self.em_andamento4_page))

        # Layout horizontal para os botões de navegação
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_inicial)
        button_layout.addWidget(self.btn_tabela)
        button_layout.addWidget(self.btn_notificacoes)
        button_layout.addWidget(self.btn_em_andamento4)
        button_layout.addStretch()  # Alinha os botões à esquerda

        self.layout.addStretch()  # Empurra o conteúdo para o topo
        self.layout.addLayout(button_layout)

        self.aplicar_tema_escuro()  # Aplica tema escuro ao iniciar

    def aplicar_tema_escuro(self):
        """
        Define o estilo visual da aplicação em modo escuro.
        """
        estilo = """
        QWidget { background-color: #2E2E2E; color: white; }
        QPushButton { background-color: #444; color: white; border-radius: 5px; padding: 8px; }
        QPushButton:hover { background-color: #555; }
        QTableWidget { background-color: #3B3B3B; color: white; gridline-color: #555; }
        QHeaderView::section { background-color: #444; color: white; padding: 5px; }
        """
        self.setStyleSheet(estilo)

    def closeEvent(self, event):
        """
        Exibe uma caixa de diálogo de confirmação antes de fechar a aplicação.
        """
        resposta = QMessageBox.question(
            self, "Sair", "Tem certeza que deseja sair?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if resposta == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# === PÁGINA INICIAL ===
class InicialApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Interface Inicial")
        label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(label)
        layout.addStretch()


# === PÁGINA DE TABELA ===
class TabelaApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Tabela principal com 3 colunas e 3 linhas
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["ID", "Nome", "Idade"])
        self.tabela.setRowCount(3)
        self.tabela.setFixedSize(1000, 600)
        self.tabela.setColumnWidth(0, 300)
        self.tabela.setColumnWidth(1, 350)
        self.tabela.setColumnWidth(2, 350)
        self.tabela.setRowHeight(0, 50)
        self.tabela.setRowHeight(1, 50)
        self.tabela.setRowHeight(2, 50)

        # Preenchendo dados iniciais
        dados = [("1", "Fulano", "25"), ("2", "Deltrano", "30"), ("3", "Ciclano", "22")]
        for row, (id_val, nome, idade) in enumerate(dados):
            self.tabela.setItem(row, 0, QTableWidgetItem(id_val))
            self.tabela.setItem(row, 1, QTableWidgetItem(nome))
            self.tabela.setItem(row, 2, QTableWidgetItem(idade))

        # Botões de controle da tabela
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

        # Layout dos botões
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_editar_cabecalhos)
        button_layout.addWidget(self.btn_adicionar_coluna)
        button_layout.addWidget(self.btn_adicionar_linha)
        button_layout.addWidget(self.btn_deletar_linha)
        button_layout.addWidget(self.btn_deletar_coluna)

        layout.addWidget(self.tabela)
        layout.addLayout(button_layout)

    def abrir_janela_edicao_cabecalhos(self):
        """
        Abre janela para editar os títulos das colunas da tabela.
        """
        self.janela_edicao = QDialog(self)
        self.janela_edicao.setWindowTitle("Editar Cabeçalhos")
        layout = QVBoxLayout(self.janela_edicao)

        self.campos_cabecalhos = []
        for col in range(self.tabela.columnCount()):
            campo = QLineEdit(self.tabela.horizontalHeaderItem(col).text())
            layout.addWidget(QLabel(f"Cabeçalho {col + 1}:"))
            layout.addWidget(campo)
            self.campos_cabecalhos.append(campo)

        btn_aplicar = QPushButton("Aplicar")
        btn_aplicar.clicked.connect(self.aplicar_mudancas_cabecalhos)
        layout.addWidget(btn_aplicar)

        self.janela_edicao.exec_()

    def aplicar_mudancas_cabecalhos(self):
        """
        Aplica os novos nomes aos cabeçalhos da tabela.
        """
        for col, campo in enumerate(self.campos_cabecalhos):
            self.tabela.setHorizontalHeaderItem(col, QTableWidgetItem(campo.text()))
        self.janela_edicao.close()

    def adicionar_coluna(self):
        """
        Adiciona uma nova coluna à tabela.
        """
        coluna_atual = self.tabela.columnCount()
        self.tabela.setColumnCount(coluna_atual + 1)
        self.tabela.setHorizontalHeaderItem(coluna_atual, QTableWidgetItem(f"Coluna {coluna_atual + 1}"))

    def adicionar_linha(self):
        """
        Adiciona uma nova linha à tabela.
        """
        linha_atual = self.tabela.rowCount()
        self.tabela.setRowCount(linha_atual + 1)

    def deletar_linha(self):
        """
        Remove a linha atualmente selecionada na tabela.
        """
        linha_selecionada = self.tabela.currentRow()
        if linha_selecionada >= 0:
            self.tabela.removeRow(linha_selecionada)

    def deletar_coluna(self):
        """
        Remove a coluna atualmente selecionada na tabela.
        """
        coluna_selecionada = self.tabela.currentColumn()
        if coluna_selecionada >= 0:
            self.tabela.removeColumn(coluna_selecionada)


# === PÁGINA DE CONVERSÃO (PLACEHOLDER) === 
# Converte arquivos de imagem .jpg ou .jpeg para .png | Converte arquivos .csv para .xlsx (Excel) | Extrai o texto de um PDF e salva em um arquivo .txt
class ConversãoApp(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(100, 80, 100, 80)

        # Título
        titulo = QLabel("Conversor de Arquivos")
        titulo.setStyleSheet("font-size: 28px; font-weight: bold; margin-bottom: 20px;")
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)

        # Informações do arquivo
        self.label_arquivo = QLabel("Nenhum arquivo selecionado.")
        self.label_arquivo.setAlignment(Qt.AlignCenter)
        self.label_arquivo.setStyleSheet("font-size: 16px; padding: 10px; border: 1px solid #666; border-radius: 6px;")
        layout.addWidget(self.label_arquivo)

        # Botões
        botoes_layout = QHBoxLayout()
        self.botao_selecionar = QPushButton("Selecionar Arquivo")
        self.botao_converter = QPushButton("Converter")
        self.botao_selecionar.setFixedHeight(40)
        self.botao_converter.setFixedHeight(40)
        botoes_layout.addWidget(self.botao_selecionar)
        botoes_layout.addWidget(self.botao_converter)
        layout.addLayout(botoes_layout)

        # Linha divisória
        linha = QFrame()
        linha.setFrameShape(QFrame.HLine)
        linha.setFrameShadow(QFrame.Sunken)
        layout.addWidget(linha)

        # Status
        self.status = QLabel("")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet("font-size: 14px; color: #00cc66;")
        layout.addWidget(self.status)

        # Conexões
        self.botao_selecionar.clicked.connect(self.selecionar_arquivo)
        self.botao_converter.clicked.connect(self.converter)

        self.arquivo_entrada = ""

    def selecionar_arquivo(self):
        caminho, _ = QFileDialog.getOpenFileName(self, "Selecionar arquivo")
        if caminho:
            self.arquivo_entrada = caminho
            self.label_arquivo.setText(f"Arquivo selecionado:\n{os.path.basename(caminho)}")
            self.status.setText("")

    def converter(self):
        if not self.arquivo_entrada:
            QMessageBox.warning(self, "Aviso", "Selecione um arquivo primeiro.")
            return

        nome, extensao = os.path.splitext(self.arquivo_entrada)
        extensao = extensao.lower()

        try:
            if extensao in ['.jpg', '.jpeg']:
                saida = f"{nome}.png"
                imagem = Image.open(self.arquivo_entrada)
                imagem.save(saida, 'PNG')
                self.status.setText(f"Imagem convertida com sucesso:\n{saida}")

            elif extensao == '.csv':
                saida = f"{nome}.xlsx"
                df = pd.read_csv(self.arquivo_entrada)
                df.to_excel(saida, index=False)
                self.status.setText(f"CSV convertido com sucesso:\n{saida}")

            elif extensao == '.pdf':
                saida = f"{nome}.txt"
                with open(self.arquivo_entrada, 'rb') as pdf_file:
                    leitor = PyPDF2.PdfReader(pdf_file)
                    texto = ''.join(pagina.extract_text() for pagina in leitor.pages)
                with open(saida, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(texto)
                self.status.setText(f"PDF convertido com sucesso:\n{saida}")

            else:
                QMessageBox.critical(self, "Erro", f"Extensão não suportada: {extensao}")
                return

            QMessageBox.information(self, "Sucesso", f"Arquivo convertido com sucesso!")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro na conversão:\n{str(e)}")


# === CHATBOT COM INTEGRAÇÃO OPENROUTER ===
class ChatBotIAApp(QWidget):
    def __init__(self):
        super().__init__()
        self.historico = [
            {"role": "system", "content": "Você é um assistente útil e educado."},
        ]
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.chatbox = QTextEdit()
        self.chatbox.setReadOnly(True)
        self.chatbox.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.chatbox)

        self.entrada = QLineEdit()
        self.entrada.setPlaceholderText("Digite sua mensagem e pressione Enter...")
        self.entrada.returnPressed.connect(self.responder)
        layout.addWidget(self.entrada)

        self.btn_enviar = QPushButton("Enviar")
        self.btn_enviar.clicked.connect(self.responder)
        layout.addWidget(self.btn_enviar)

    def responder(self):
        """
        Captura a mensagem do usuário, exibe na tela e inicia thread de resposta.
        """
        user_msg = self.entrada.text().strip()
        if not user_msg:
            return

        self.chatbox.append(f"<b>Você:</b> {user_msg}")
        self.entrada.clear()

        self.historico.append({"role": "user", "content": user_msg})
        threading.Thread(target=self.responder_em_thread, args=(user_msg,)).start()

    def responder_em_thread(self, user_msg):
        """
        Thread para evitar travamentos na UI ao obter resposta da API.
        """
        try:
            resposta = self.gerar_resposta()
            self.chatbox.append(f"<b>Bot:</b> {resposta}")
            self.historico.append({"role": "assistant", "content": resposta})
        except Exception as e:
            self.chatbox.append(f"<span style='color:red;'>[ERRO] {e}</span>")

        if len(self.historico) > 20:
            self.historico[:] = [self.historico[0]] + self.historico[-19:]

    def gerar_resposta(self):
        """
        Envia o histórico à API da OpenRouter e retorna a resposta gerada pelo modelo.
        """
        API_KEY = "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"
        MODELO = "openai/gpt-3.5-turbo"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "MeuChatTurbo"
        }

        payload = {
            "model": MODELO,
            "messages": self.historico
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"Erro: {response.status_code} - {response.json()}")

        resposta = response.json()
        return resposta["choices"][0]["message"]["content"].strip()


# === INICIALIZAÇÃO DA APLICAÇÃO ===
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
