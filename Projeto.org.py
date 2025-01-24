import tkinter as tk

root = tk.Tk()
root.title("Interface Dark Mode")
root.geometry("800x600")  # Tamanho da janela

# Definindo a cor de fundo da janela para um tom escuro
root.configure(bg="#2e2e2e")

# Criando um label com texto claro
label = tk.Label(root, text="Bem-vindo ao Projeto.org! Voce é um dos criadores", fg="white", bg="#2e2e2e", font=("Arial", 14))
label.pack(pady=50)

# Iniciando o loop da interface
root.mainloop()
