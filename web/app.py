from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)

CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), '..', 'data', 'tasks.json')

def carregar_tarefas():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    tarefas = carregar_tarefas()
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    descricao = request.form.get('descricao').strip()
    prioridade = request.form.get('prioridade', '')
    prazo = request.form.get('prazo', '')

    if descricao:
        tarefas = carregar_tarefas()
        nova_tarefa = {
            'descricao': descricao,
            'feito': False,
            'prioridade': prioridade,
            'prazo': prazo
        }
        tarefas.append(nova_tarefa)
        salvar_tarefas(tarefas)

    return redirect(url_for('index'))

@app.route('/editar/<int:indice>', methods=['POST'])
def editar(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas[indice]['descricao'] = request.form.get('descricao', '').strip()
        tarefas[indice]['prioridade'] = request.form.get('prioridade', '')
        tarefas[indice]['prazo'] = request.form.get('prazo', '')
        salvar_tarefas(tarefas)
    return redirect(url_for('index'))

@app.route('/alternar/<int:indice>', methods=['POST'])
def alternar_tarefa(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas[indice]['feito'] = not tarefas[indice].get('feito', False)
        salvar_tarefas(tarefas)
    return redirect(url_for('index'))

@app.route('/remover/<int:indice>', methods=['POST'])
def remover(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        salvar_tarefas(tarefas)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
