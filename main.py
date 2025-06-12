import os
import json

arquivo = "tarefas.json"

def carregarTarefas():
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            return json.load(f)
    return []

def salvarTarefas(tarefas):
    with open(arquivo, "w") as f:
        json.dump(tarefas, f, indent=4)

def mostrarMenu():
    print("\nLista de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

def adicionarTarefa(tarefas):
    nome_tarefa = input("Digite sua nova tarefa: ")
    tarefas.append({"Tarefas": nome_tarefa, "Concluída": False})

def listarTarefas(tarefas):
    print("\nTarefas:")
    for i, t in enumerate(tarefas):
        status = "✅" if t["Concluída"] else "❌"
        print(f"{i+1}. {t["Tarefas"]} [{status}]")

def marcarComoConcluída(tarefas):
    listarTarefas(tarefas)
    try:
        i = int(input("Digite o número da tarefas concluída: ")) - 1
        tarefas[i]["Concluída"] = True
    except (IndexError, ValueError):
        print("Tarefa inválida")

def removerTarefa(tarefas):
    listarTarefas(tarefas)
    try:
        i = int(input("Digite o número da tarefa: ")) - 1
        tarefas.pop(i)
    except (IndexError, ValueError):
        print("Tarefa inválida")

def main():
    tarefas = carregarTarefas()
    while True:
        mostrarMenu()
        escolha = int(input("\nEscolha uma opção: "))
        if escolha == 1:
            adicionarTarefa(tarefas)
        elif escolha == 2:
            listarTarefas(tarefas)
        elif escolha == 3:
            marcarComoConcluída(tarefas)
        elif escolha == 4:
            removerTarefa(tarefas)
        elif escolha == 5:
            salvarTarefas(tarefas)
            print("Até mais!")
            break
        else: 
            print("Opção inválida")

if __name__ == "__main__":
    main()
