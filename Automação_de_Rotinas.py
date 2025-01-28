import tkinter as tk
from tkinter import ttk, messagebox


# Função para alternar entre frames
def mostrar_frame(frame):
    frame.tkraise()


# Função para criar a tabela (Frame 2)
def criar_tabela():
    dados = [
        (1, "Fulano", 25),
        (2, "Deltrano", 30),
        (3, "Ciclano", 22)
    ]
    for item in dados:
        tabela.insert("", tk.END, values=item)


# Função para adicionar dados à tabela
def adicionar_dados():
    id_valor = entry_id.get()
    nome_valor = entry_nome.get()
    idade_valor = entry_idade.get()

    if id_valor and nome_valor and idade_valor:
        tabela.insert("", tk.END, values=(id_valor, nome_valor, idade_valor))
        entry_id.delete(0, tk.END)
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos para adicionar um item!")


# Função para remover dados selecionados na tabela
def remover_dados():
    selecionado = tabela.selection()
    if selecionado:
        tabela.delete(selecionado)
    else:
        messagebox.showwarning("Aviso", "Selecione um item para remover!")


# Função para editar dados selecionados na tabela
def editar_dados():
    selecionado = tabela.selection()
    if selecionado:
        valores = tabela.item(selecionado, "values")
        entry_id.delete(0, tk.END)
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        
        entry_id.insert(0, valores[0])
        entry_nome.insert(0, valores[1])
        entry_idade.insert(0, valores[2])
        
        tabela.delete(selecionado)
    else:
        messagebox.showwarning("Aviso", "Selecione um item para editar!")


# Função para ativar a edição de células na tabela
def editar_celula(event):
    # Obter o item selecionado e a coluna clicada
    item_selecionado = tabela.selection()
    if not item_selecionado:
        return

    coluna = tabela.identify_column(event.x)  # Identifica a coluna clicada
    linha = tabela.identify_row(event.y)      # Identifica a linha clicada

    if linha and coluna:
        coluna_index = int(coluna.replace('#', '')) - 1  # Remove '#' e ajusta para índice
        item = tabela.item(linha)
        valores = list(item['values'])

        # Abrir uma Entry no local para edição
        x, y, width, height = tabela.bbox(linha, column=coluna_index)
        entry_edit = tk.Entry(frame2, font=("Arial", 12))
        entry_edit.place(x=x, y=y + 150, width=width, height=height)
        entry_edit.insert(0, valores[coluna_index])

        # Função para salvar a edição
        def salvar_edicao(event=None):
            novos_valores = valores
            novos_valores[coluna_index] = entry_edit.get()
            tabela.item(linha, values=novos_valores)  # Atualizar os valores
            entry_edit.destroy()

        # Vincular a tecla Enter para salvar a edição
        entry_edit.bind('<Return>', salvar_edicao)
        entry_edit.focus()


def abrir_janela_config():
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Configurações")
    nova_janela.geometry("400x300")
    nova_janela.configure(bg="#2e2e2e")
    
    # Adicionar widgets na nova janela
    tk.Label(nova_janela, text="janela de configurações!", bg="#2e2e2e", fg="white", font=("Arial", 14)).place(x=50, y=25)
    tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy, bg="#3b3b3b", fg="white", font=("Arial", 12)).place(x=25, y=250)


# Função para criar o Frame 1 (Interface Principal)
def criar_frame1(root):
    global frame1
    frame1 = tk.Frame(root, bg="#2e2e2e")
    frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    tk.Label(frame1, text="Frame 1", bg="#2e2e2e", fg="white", font=("Arial", 24)).place(x=50, y=100)
    
    tk.Button(frame1, text="Frame 2", command=lambda: mostrar_frame(frame2), fg="white", bg="#3b3b3b", font=("Arial", 16, "bold")).place(x=50, y=25)
    tk.Button(frame1, text="Frame 3", command=lambda: criar_frame3(root), fg="white", bg="#3b3b3b", font=("Arial", 16, "bold")).place(x=200, y=25)
    tk.Button(frame1, text="Frame 4", command=lambda: criar_frame4(root), fg="white", bg="#3b3b3b", font=("Arial", 16, "bold")).place(x=350, y=25)
    tk.Button(frame1, text="Frame 5", command=lambda: criar_frame5(root), fg="white", bg="#3b3b3b", font=("Arial", 16, "bold")).place(x=500, y=25)

    tk.Button(frame1, text="Config", command=abrir_janela_config, fg="white", bg="#3b3b3b", font=("Arial", 16, "bold")).place(x=900, y=25)


# Função para criar o Frame 2 (Tabela)
def criar_frame2(root):
    global frame2, entry_id, entry_nome, entry_idade, tabela

    frame2 = tk.Frame(root, bg="#2e2e2e")
    frame2.place(relx=0, rely=0, relwidth=1, relheight=1)

    tk.Label(frame2, text="ID:", bg="#2e2e2e", fg="white", font=("Arial", 12)).place(x=50, y=20)
    entry_id = tk.Entry(frame2, font=("Arial", 12))
    entry_id.place(x=100, y=20, width=100)

    tk.Label(frame2, text="Nome:", bg="#2e2e2e", fg="white", font=("Arial", 12)).place(x=250, y=20)
    entry_nome = tk.Entry(frame2, font=("Arial", 12))
    entry_nome.place(x=310, y=20, width=200)

    tk.Label(frame2, text="Idade:", bg="#2e2e2e", fg="white", font=("Arial", 12)).place(x=550, y=20)
    entry_idade = tk.Entry(frame2, font=("Arial", 12))
    entry_idade.place(x=620, y=20, width=100)

    tk.Button(frame2, text="Adicionar", command=adicionar_dados, fg="white", bg="#3b3b3b", font=("Arial", 12)).place(x=50, y=60)
    tk.Button(frame2, text="Remover", command=remover_dados, fg="white", bg="#3b3b3b", font=("Arial", 12)).place(x=150, y=60)
    tk.Button(frame2, text="Editar", command=editar_dados, fg="white", bg="#3b3b3b", font=("Arial", 12)).place(x=250, y=60)
    tk.Button(frame2, text="Voltar", command=lambda: mostrar_frame(frame1), fg="white", bg="#3b3b3b", font=("Arial", 12)).place(x=350, y=60)

    colunas = ("ID", "Nome", "Idade")
    tabela = ttk.Treeview(frame2, columns=colunas, show="headings")
    tabela.heading("ID", text="ID")
    tabela.heading("Nome", text="Nome")
    tabela.heading("Idade", text="Idade")

    tabela.column("ID", width=100, anchor="center")
    tabela.column("Nome", width=250, anchor="w")
    tabela.column("Idade", width=100, anchor="center")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#3b3b3b", foreground="white", fieldbackground="#3b3b3b", rowheight=25)
    style.map("Treeview", background=[("selected", "#1f77b4")])

    tabela.place(relx=0.05 , rely=0.2, relwidth=0.9, relheight=0.5)
    tabela.bind("<Double-1>", editar_celula)  # Duplo clique para editar células
    criar_tabela()


# Função para criar o Frame 3 (Notificações)
def criar_frame3(root):
    global frame3
    frame3 = tk.Frame(root, bg="#2e2e2e")
    frame3.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    tk.Label(frame3, text="Sistemas de notificações ( Opcional )", bg="#2e2e2e", fg="white", font=("Arial", 24)).place(relx=0.5, rely=0.1, anchor="center")
    
    tk.Label(frame3, text="@Gmail:", bg="#2e2e2e", fg="white", font=("Arial", 12)).place(x=50, y=150)
    entrada1 = tk.Entry(frame3, font=("Arial", 12))
    entrada1.place(x=150, y=150, width=300)
    
    tk.Label(frame3, text="Telegrama:", bg="#2e2e2e", fg="white", font=("Arial", 12)).place(x=50, y=200)
    entrada2 = tk.Entry(frame3, font=("Arial", 12))
    entrada2.place(x=150, y=200, width=300)
    
    tk.Button(frame3, text="Voltar", command=lambda: mostrar_frame(frame1), fg="white", bg="#3b3b3b", font=("Arial", 12)).place(relx=0.95, rely=0.05, anchor="ne")


#Função para criar o Frame 4 (Em andamento)
def criar_frame4(root):
    global frame4
    frame4 = tk.Frame(root, bg="#2e2e2e")
    frame4.place(relx=0, rely=0, relwidth=1, relheight=1)


    tk.Button(frame4, text="Voltar", command=lambda: mostrar_frame(frame1), fg="white", bg="#3b3b3b", font=("Arial", 12)).place(relx=0.95, rely=0.05, anchor="ne")


#Função para criar o Frame 5 (Em andamento)
def criar_frame5(root):
    global frame5
    frame5 = tk.Frame(root, bg="#2e2e2e")
    frame5.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    
    tk.Button(frame5, text="Voltar", command=lambda: mostrar_frame(frame1), fg="white", bg="#3b3b3b", font=("Arial", 12)).place(relx=0.95, rely=0.05, anchor="ne")

# Configuração da janela principal
root = tk.Tk()
root.title("")
root.geometry("1024x768")
root.configure(bg="#2e2e2e")
root.maxsize(width=1280, height=720)
root.minsize(width=800, height=600)


# Criar frames
criar_frame1(root)
criar_frame2(root)
criar_frame3(root)
criar_frame4(root)
criar_frame5(root)


# Exibir o primeiro frame
mostrar_frame(frame1)


# Iniciar o loop principal
root.mainloop()
