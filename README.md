# 📝 TechToDo

**TechToDo** é uma aplicação simples de **lista de tarefas via terminal**, feita com **Python puro**, que salva tudo em um arquivo `.json`.  
É o primeiro projeto Python 100% solo de [Igor] — criado com foco em aprendizado, boas práticas e organização para publicar no GitHub com orgulho! 🚀

---

## 📸 Demonstração


=== TechToDo ===
1. Listar tarefas
2. Adicionar tarefa
3. Marcar tarefa como concluída
4. Remover tarefa
0. Sair
🧠 Funcionalidades
✅ Adicionar novas tarefas

✅ Listar tarefas (com status de concluída ou pendente)

✅ Marcar tarefas como concluídas

✅ Remover tarefas

✅ Armazenamento automático em data/tasks.json

✅ Interface simples via terminal

✅ Código separado em módulos (boa prática)

💻 Como rodar o projeto
Clone o repositório:




git clone https://github.com/SEU-USUARIO/TechToDo.git
cd TechToDo
(Opcional) Crie e ative o ambiente virtual:




python -m venv venv
venv\Scripts\activate         # Windows
source venv/bin/activate      # macOS/Linux
Execute o app: python main.py


## 📂 Estrutura do projeto

```text
TechToDo/
├── data/
│   └── tasks.json         # Armazena as tarefas salvas
├── todo/
│   ├── core.py            # Lógica principal do menu
│   ├── storage.py         # Leitura/escrita no JSON
│   └── __init__.py        # Define o pacote
├── main.py                # Arquivo principal do app
├── requirements.txt       # (vazio por enquanto)
├── .gitignore             # Ignora venv, __pycache__, etc
└── README.md              # Documentação do projeto
```


## 🔧 Extensões recomendadas (VS Code)

| Extensão         | Finalidade                        |
|------------------|-----------------------------------|
| Python           | Execução e debug de scripts       |
| Pylance          | IntelliSense e tipagem            |
| AutoDocstring    | Geração automática de docstrings  |
| Black Formatter  | Formatação automática do código   |
| isort            | Organização dos imports           |
| DotENV           | (Para futuros projetos com `.env`) |


🚀 Aprendizados do projeto
📦 Estruturação modular com Python

🧠 Uso de listas, dicionários e funções puras

💾 Salvamento de dados com JSON

🧪 Testes no terminal

🧰 Git + GitHub + VS Code com extensões profissionais

🧱 Organização de código para repositório público

