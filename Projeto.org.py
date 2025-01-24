import tkinter as tk

# Funções de cada Botão do Programa
def Botão_1():
    label_resultado.config(text='Funcionou!!!! 1')


def Botão_2():
    label_resultado.config(text='Funcionou!!!! 2')


def Botão_3():
    label_resultado.config(text='Funcionou!!!! 3')


def Botão_4():
    label_resultado.config(text='Funcionou!!!! 4')


root = tk.Tk()
root.title("Projeto.org")
root.geometry("800x600")

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
