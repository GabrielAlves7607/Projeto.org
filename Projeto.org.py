root = tk.Tk()
root.title("Projeto.org")
root.geometry("800x600")  # Tamanho da janela

# Definindo a cor de fundo da janela para um tom escuro
root.configure(bg="#2e2e2e")

# Criando um label com texto claro
#label = tk.Label(root, text="Bem-vindo ao Projeto.org! Voce é um dos criadores", fg="white", bg="#2e2e2e", font=("Arial", 14))
#label.place(x=50, y=50)

button = tk.Button(root, text="Botão 1", fg="white", bg="#3b3b3b", font=("Arial", 16, "bold"))
button.place(x=50, y=25)

button = tk.Button(root, text="Botão 2", fg="white", bg="#3b3b3b", font=("Arial", 16, "bold"))
button.place(x=175, y=25)

button = tk.Button(root, text="Botão 3", fg="white", bg="#3b3b3b", font=("Arial", 16, "bold"))
button.place(x=300, y=25)

button = tk.Button(root, text="Botão 4", fg="white", bg="#3b3b3b", font=("Arial", 16, "bold"))
button.place(x=425, y=25)



# Iniciando o loop da interface
root.mainloop()


