import tkinter as tk
from tkinter import ttk

# Funções de cada Botão do Programa
def Botão_1():

    colunas = ("ID", "Nome", "Idade")
    tabela = ttk.Treeview(root, columns=colunas, show="headings")

    # Configurar os cabeçalhos e colunas
    tabela.heading("ID", text="ID")
    tabela.heading("Nome", text="Nome")
    tabela.heading("Idade", text="Idade")

    tabela.column("ID", width=100, anchor="center")
    tabela.column("Nome", width=250, anchor="w")
    tabela.column("Idade", width=100, anchor="center")

    # Configurando estilo
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", 
                background="#3b3b3b", 
                foreground="white", 
                fieldbackground="#3b3b3b",
                rowheight=25)
    style.map("Treeview", background=[("selected", "#1f77b4")])

    # Adicionar dados na tabela
    dados = [
        (1, "Alice", 25),
        (2, "Bob", 30),
        (3, "Charlie", 22),
        (4, "Diana", 28),
    ]
    for item in dados:
        tabela.insert("", tk.END, values=item)

    # Posicionar a tabela na interface
    tabela.place(x= 50, y= 100, width= 700, height= 400)


def Botão_2():
    label_resultado.config(text='Funcionou!!!! 2')


def Botão_3():
    label_resultado.config(text='Funcionou!!!! 3')


def Botão_4():
    label_resultado.config(text='Funcionou!!!! 4')


root = tk.Tk()
root.title("Projeto.org")
root.geometry("1024x768")

# Definindo a cor de fundo da janela para um tom escuro
root.configure(bg="#2e2e2e")

# Rótulo para exibir os resultados
label_resultado = tk.Label(root, text="Clique em um botão para ver o resultado", bg="#2e2e2e", fg="white", font=("Arial", 14))
label_resultado.place(x=50, y=100)

# Botões do Programa
button1 = tk.Button(root, text="Botão 1", command=Botão_1, fg="white", bg="#3b3b3b", font=("Arial", 16, "bold"))
button1.place(x=50, y=25)

button2 = tk.Button(root, text="Botão 2", command=Botão_2, fg="white", bg="#3b3b3b", font=("Arial", 16, "bold"))
button2.place(x=175, y=25)

button3 = tk.Button(root, text="Botão 3", command=Botão_3, fg="white", bg="#3b3b3b", font=("Arial", 16, "bold"))
button3.place(x=300, y=25)

button4 = tk.Button(root, text="Botão 4", command=Botão_4, fg="white", bg="#3b3b3b", font=("Arial", 16, "bold"))
button4.place(x=425, y=25)

# Iniciando o loop da interface
root.mainloop()
