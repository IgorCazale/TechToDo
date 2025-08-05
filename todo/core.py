from todo.storage import carregar_tarefas, salvar_tarefas

def exibir_menu():
    print("\n=== TechToDo ===")
    print("1. Listar tarefas")
    print("2. Adicionar tarefa")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Editar tarefa")
    print("6. Concluir várias tarefas")
    print("7. Remover várias tarefas")
    print("8. Alternar status de tarefas")
    print("0. Sair")

def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa encontrada.")
        return

    print("\n📋 Suas Tarefas:")
    for idx, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["feito"] else "❌"

        prioridade = tarefa.get("prioridade", "")
        if prioridade == "Alta":
            cor = "🔴"
        elif prioridade == "Média":
            cor = "🟡"
        elif prioridade == "Baixa":
            cor = "🟢"
        else:
            cor = ""

        prioridade_txt = f" ({cor} {prioridade})" if prioridade else ""
        prazo_txt = f" 🗓 {tarefa['prazo']}" if tarefa.get("prazo") else ""
        print(f"{idx}. {tarefa['descricao']}{prioridade_txt}{prazo_txt} [{status}]")

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ").strip()
    if not descricao:
        print("⚠️ Descrição inválida.")
        return

    print("Digite a prioridade:")
    print("1. 🔴 Alta")
    print("2. 🟡 Média")
    print("3. 🟢 Baixa")
    print("0. Sem prioridade")

    prioridade_opcao = input("Escolha uma opção (0-3): ").strip()
    mapa_prioridade = {
        "1": "Alta",
        "2": "Média",
        "3": "Baixa"
    }
    prioridade = mapa_prioridade.get(prioridade_opcao, "")

    prazo = input("Digite o prazo da tarefa (DD/MM/AAAA) ou deixe em branco: ").strip()

    nova_tarefa = {
        "descricao": descricao,
        "feito": False,
        "prioridade": prioridade,
        "prazo": prazo
    }

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada com sucesso!")

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

def editar_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a editar: "))
        if 1 <= indice <= len(tarefas):
            nova_descricao = input("Digite a nova descrição: ").strip()
            if nova_descricao:
                tarefas[indice - 1]["descricao"] = nova_descricao
                salvar_tarefas(tarefas)
                print("✏️ Tarefa atualizada com sucesso!")
            else:
                print("⚠️ Descrição inválida. Nenhuma alteração feita.")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("⚠️ Digite um número válido.")

def concluir_varias_tarefas(tarefas):
    listar_tarefas(tarefas)
    entrada = input("Digite os números das tarefas a concluir (ex: 1;2;4): ").strip()
    if not entrada:
        print("⚠️ Nenhuma entrada fornecida.")
        return

    indices = entrada.split(";")
    alteradas = []

    for item in indices:
        try:
            indice = int(item.strip())
            if 1 <= indice <= len(tarefas):
                tarefas[indice - 1]["feito"] = True
                alteradas.append(indice)
            else:
                print(f"⚠️ Tarefa {indice} não existe.")
        except ValueError:
            print(f"⚠️ '{item}' não é um número válido.")

    if alteradas:
        salvar_tarefas(tarefas)
        print(f"✅ Tarefas {', '.join(map(str, alteradas))} marcadas como concluídas!")
    else:
        print("⚠️ Nenhuma tarefa foi atualizada.")

def remover_varias_tarefas(tarefas):
    listar_tarefas(tarefas)
    entrada = input("Digite os números das tarefas a remover (ex: 1;2;4): ").strip()
    if not entrada:
        print("⚠️ Nenhuma entrada fornecida.")
        return

    indices = entrada.split(";")
    indices_validos = []

    for item in indices:
        try:
            indice = int(item.strip())
            if 1 <= indice <= len(tarefas):
                indices_validos.append(indice)
            else:
                print(f"⚠️ Tarefa {indice} não existe.")
        except ValueError:
            print(f"⚠️ '{item}' não é um número válido.")

    if not indices_validos:
        print("⚠️ Nenhuma tarefa válida para remoção.")
        return

    removidas = []
    for i in sorted(indices_validos, reverse=True):
        tarefa = tarefas.pop(i - 1)
        removidas.append(tarefa["descricao"])

    salvar_tarefas(tarefas)
    print(f"🗑️ Tarefas removidas: {', '.join(removidas)}")

def alternar_status_tarefas(tarefas):
    listar_tarefas(tarefas)
    entrada = input("Digite os números das tarefas para alternar o status (ex: 1;3;5): ").strip()
    if not entrada:
        print("⚠️ Nenhuma entrada fornecida.")
        return

    indices = entrada.split(";")
    alteradas = []

    for item in indices:
        try:
            indice = int(item.strip())
            if 1 <= indice <= len(tarefas):
                tarefa = tarefas[indice - 1]
                tarefa["feito"] = not tarefa["feito"]
                alteradas.append((indice, tarefa["descricao"], tarefa["feito"]))
            else:
                print(f"⚠️ Tarefa {indice} não existe.")
        except ValueError:
            print(f"⚠️ '{item}' não é um número válido.")

    if alteradas:
        salvar_tarefas(tarefas)
        for idx, desc, status in alteradas:
            icone = "✅" if status else "❌"
            print(f"🔁 Tarefa {idx} — '{desc}' atualizada para [{icone}]")
    else:
        print("⚠️ Nenhuma tarefa foi atualizada.")

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
        elif opcao == "5":
            editar_tarefa(tarefas)
        elif opcao == "6":
            concluir_varias_tarefas(tarefas)
        elif opcao == "7":
            remover_varias_tarefas(tarefas)
        elif opcao == "8":
            alternar_status_tarefas(tarefas)
        elif opcao == "0":
            print("👋 Saindo... Até mais!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")
