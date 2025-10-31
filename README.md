# Todo List Flask

Uma aplicação web para organização de tarefas construído com Flask e MySQL.
( Sem autenticação )

![Screenshot do Projeto](static/print.png)

## Funcionalidades

- Criar tarefas
- Editar tarefas existentes
- Remover tarefas
- Limite máximo de 5 tarefas
- Notificações com fade out automático

## Tecnologias Utilizadas

- Python 3.x
- Flask / Jinja2
- MySQL (via XAMPP)
- HTML/CSS
- JavaScript

## Arquivos principais do projeto

```
ToDoPessoal/
├── static/
│   ├── script.js
│   └── style.css
├── templates/
│   ├── base.html
│   ├── edit.html
│   └── home.html
└── main.py
```

## Como Executar

1. Certifique-se de ter Python 3.x instalado
2. Instale as dependências:
```bash
pip install flask mysql-connector-python
```

3. Configure o MySQL via XAMPP:
   - Inicie o XAMPP e ative o MySQL
   - Host: localhost
   - Usuário: root
   - Senha: (vazia)
   - Database: todo_flask (O código criará o banco se não existir)

4. Execute o aplicativo:
```bash
python main.py
```

5. Acesse http://localhost:5000 no navegador

## Funcionalidades do Banco de Dados

- Tabela `tarefas`:
  - `id` (INT, AUTO_INCREMENT)
  - `nome_tarefa` (VARCHAR(100))
  - `data_criacao` (DATETIME)

## Features Implementadas

- [x] CRUD completo de tarefas
- [x] Validação de limite máximo
- [x] Flash messages com fade out
- [x] Confirmação de exclusão
- [ ] Responsividade mobile