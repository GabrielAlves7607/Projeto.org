import tkinter as tk
from tkinter import ttk, messagebox

# Função para alternar entre frames
def mostrar_frame(frame):
    frame.tkraise()


# Função para criar tabela (segundo frame)
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


def Botão_2():
    print("Funcionou 2")

def Botão_3():
    print("Funcionou 3")

def Botão_4():
    print("Funcionou 4")


# Configuração da janela principal
root = tk.Tk()
root.title("Interface Dinâmica")
root.geometry("1024x768")
root.configure(bg="#2e2e2e")


# Criar frames
frame1 = tk.Frame(root, bg="#2e2e2e")
frame2 = tk.Frame(root, bg="#2e2e2e")


for frame in (frame1, frame2):
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)


# Frame 1 - Interface Principal
tk.Button(frame1, text="Botão 1", command=lambda: mostrar_frame(frame2), fg="white", bg="#3b3b3b", font=("Arial", 16, "bold")).place(x=50, y=25)
tk.Button(frame1, text="Botão 2", command=Botão_2 ,fg="white", bg="#3b3b3b", font=("Arial", 16, "bold")).place(x=200, y=25)
tk.Button(frame1, text="Botão 3", command=Botão_3 ,fg="white", bg="#3b3b3b", font=("Arial", 16, "bold")).place(x=350, y=25)
tk.Button(frame1, text="Botão 4", command=Botão_4 ,fg="white", bg="#3b3b3b", font=("Arial", 16, "bold")).place(x=500, y=25)


# Frame 2 - Interface com Tabela
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



# Criar tabela no frame2
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
style.configure("Treeview", 
                background="#3b3b3b", 
                foreground="white", 
                fieldbackground="#3b3b3b",
                rowheight=25)
style.map("Treeview", background=[("selected", "#1f77b4")])


tabela.place(x=50, y=150, width=900, height=500)
criar_tabela()


mostrar_frame(frame1)
root.mainloop()
