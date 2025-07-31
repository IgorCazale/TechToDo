from todo.storage import carregar_tarefas, salvar_tarefas

def exibir_menu():
    print("\n=== TechToDo ===")
    print("1. Listar tarefas")
    print("2. Adicionar tarefa")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("0. Sair")

def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa encontrada.")
        return

    print("\n📋 Suas Tarefas:")
    for idx, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["feito"] else "❌"
        print(f"{idx}. {tarefa['descricao']} [{status}]")

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ").strip()
    if descricao:
        nova_tarefa = {"descricao": descricao, "feito": False}
        tarefas.append(nova_tarefa)
        salvar_tarefas(tarefas)
        print("✅ Tarefa adicionada com sucesso!")
    else:
        print("⚠️ Descrição inválida.")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a concluir: "))
        if 1 <= indice <= len(tarefas):
            tarefas[indice - 1]["feito"] = True
            salvar_tarefas(tarefas)
            print("✅ Tarefa marcada como concluída!")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("⚠️ Digite um número válido.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a remover: "))
        if 1 <= indice <= len(tarefas):
            removida = tarefas.pop(indice - 1)
            salvar_tarefas(tarefas)
            print(f"🗑️ Tarefa '{removida['descricao']}' removida.")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("⚠️ Digite um número válido.")

def menu():
    tarefas = carregar_tarefas()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "0":
            print("👋 Saindo... Até mais!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")