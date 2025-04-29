# Sistema Completo em PyQt5 com Login, Conversor, Tabela e Chatbot IA

Este é um sistema de interface gráfica feito com **PyQt5** que integra múltiplas funcionalidades em um único aplicativo desktop. O projeto inclui:

- Autenticação de usuário com cadastro e login
- Interface principal com navegação entre páginas
- Tabela interativa com edição dinâmica
- Conversor de arquivos (imagem, CSV e PDF)
- Chatbot com integração à API da OpenRouter

---

🚀 Funcionalidades

🔐 Tela de Login
- Cadastro de novo usuário com senha criptografada
- Validação de login e redirecionamento para o sistema principal
- Armazenamento de usuários com SQLite

📄 Página Inicial
- Tela de boas-vindas personalizável

📊 Tabela Interativa
- Adição e remoção de linhas/colunas
- Edição dos cabeçalhos
- Visualização de dados simulados

🔄 Conversor de Arquivos
- `.jpg/.jpeg` ➜ `.png`
- `.csv` ➜ `.xlsx`
- `.pdf` ➜ `.txt`

🤖 Chatbot com IA
- Comunicação via API com o modelo **GPT** da [OpenRouter](https://openrouter.ai)
- Interface integrada ao app com histórico de mensagens
  
---

⚙️ Tecnologias Utilizadas

- [PyQt5](https://pypi.org/project/PyQt5/)
- [Pandas](https://pypi.org/project/pandas/)
- [Pillow (PIL)](https://pypi.org/project/Pillow/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [Werkzeug (hash de senhas)](https://pypi.org/project/Werkzeug/)
- [SQLite3](https://www.sqlite.org/index.html)
- [OpenRouter API](https://openrouter.ai)
 
⚡ Como Obter a API Key para o Chatbot

Para que o chatbot funcione corretamente, é necessário gerar uma API Key no site da OpenRouter. Siga os passos abaixo:

1 - Acesse o site da OpenRouter e faça login na sua conta.
![Captura de tela 2025-04-28 230413](https://github.com/user-attachments/assets/163953d6-e2b7-4db0-8564-0c15a38ff762)

2 - Clique no menu (três barrinhas no canto) e selecione "Keys".
![Captura de tela 2025-04-28 230431](https://github.com/user-attachments/assets/3744ff6d-2928-4f57-8378-9e5f61b9682c)

3 - Crie uma nova API Key preenchendo apenas o campo de nome.
(A OpenRouter oferece alguns pontos para começar a usar o chatbot!)
![Captura de tela 2025-04-28 230445](https://github.com/user-attachments/assets/176bcfce-34ad-472f-97b7-c5636ecad952)

![Captura de tela 2025-04-28 230459](https://github.com/user-attachments/assets/0dfc4840-c7e6-46a3-8b57-f56fb483684b)

![Captura de tela 2025-04-28 230556](https://github.com/user-attachments/assets/2fdb5dce-b342-4872-84b4-628af3111bd6)

4 - Copie a API Key gerada.
![Captura de tela 2025-04-28 232709](https://github.com/user-attachments/assets/8d5e02f1-a545-473c-9ce8-c4e53aead7fc)

5 - Baixe os arquivos do projeto Pyorg, abra o arquivo App.py no VS Code (ainda sem executar).
![Captura de tela 2025-04-28 230640](https://github.com/user-attachments/assets/e7e1c6c1-1ece-406f-b012-92044b87a6c5)
![Captura de tela 2025-04-28 230717](https://github.com/user-attachments/assets/1027fdb9-01dd-4c64-a4ce-ae22024217d0)

6 - Localize no código a variável onde está "API_KEY" e substitua pelo valor da sua API Key. Aproveite! 🚀
![Captura de tela 2025-04-28 230820](https://github.com/user-attachments/assets/b2826490-3224-4c13-9733-10b1ed1dc870)


