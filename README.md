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
