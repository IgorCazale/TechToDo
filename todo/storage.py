import json
from pathlib import Path

# Caminho do arquivo JSON onde as tarefas serão salvas
TASKS_FILE = Path("data/tasks.json")


def carregar_tarefas():
    """
    Lê o arquivo JSON e retorna a lista de tarefas.
    Se o arquivo estiver vazio ou não existir, retorna uma lista vazia.
    """
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def salvar_tarefas(tarefas):
    """
    Salva a lista de tarefas no arquivo JSON.

    Parâmetros:
        tarefas (list): Lista de dicionários com as tarefas.
    """
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)
