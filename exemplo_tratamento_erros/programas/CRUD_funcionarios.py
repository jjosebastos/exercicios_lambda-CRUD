def main():
    lista_funcionarios = []
    resp = 1
    while (resp != 0):
        print("1 - Inserir funcionario.")
        print("2 - Alterar funcionario.")
        print("3 - Excluir funcionario.")
        print("4 - Exibir funcionario.")
        opc = int(input("Digite a opção desejada: "))
        match opc:
            case 1:
                inserir_funcionario(lista_funcionarios)
            case 2:
                nome_func = input("Digite o nome do funcionário")
                indice = buscar_funcionario_nome(lista_funcionarios,nome_func)
                if (indice != -1):
                    alterar_funcionario(lista_funcionarios, indice)
                else:
                    print("Funcionário não encontrado")
            case 3:
                nome_func = input("Digite o nome do funcionário a ser excluido")
                indice = buscar_funcionario_nome(lista_funcionarios, nome_func)
                if (indice != -1):
                    excluir_funcionario(lista_funcionarios, indice)
                else:
                    print("Funcionário não encontrado")
            case 4:
                exibir_funcionarios(lista_funcionarios)
            case _:
                print("Opção inválida!")
        resp = int(input("Deseja continuar? (1- SIM/0- NÃO):" ))
def inserir_funcionario(lista_funcionarios):
    try:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        salario = float(input("Digite o salário: "))
    except ValueError:
        print("Digite valores numéricos para idade e salário")
    else:
        funcioario = {'Nome': nome, 'Idade':idade, 'Salario':salario}
        lista_funcionarios.append(funcioario)
    finally:
        print("Operação finalizada")

def buscar_funcionario_nome(lista_funcionarios, nome_func):
    indice = -1
    for i in range(len(lista_funcionarios)):
        if(lista_funcionarios[i]['Nome'] == nome_func):
            indice = i
    return (indice)

def alterar_funcionario(lista_funcionarios, indice):
    try:
            print(f"Nome: {lista_funcionarios[indice]['Nome']}")
            nome = input("Digite o novo nome: ")
            print(f"Idade:{lista_funcionarios[indice]['Idade']}")
            idade = input("Digite a nova idade: ")
            print(f"Salario:{lista_funcionarios[indice]['Salario']}")
            salario = input("Digite o novo salario: ")
    except ValueError:
        print("Digite valores numericos para idade e salario")
    else:
        lista_funcionarios[indice]['Nome'] = nome
        lista_funcionarios[indice]['Idade'] = idade
        lista_funcionarios[indice]['Salario'] = salario
        print("Dados inseridos com sucesso!")
    finally:
        print("Operação finalizada")

def excluir_funcionario(lista_funcionarios, indice):
    lista_funcionarios.pop(indice)
    print("Funcionario excluido com sucesso!")

def exibir_funcionarios(lista_funcionarios):
    for i in range(len(lista_funcionarios)):
        for chave, valor in lista_funcionarios[i].items():
            print(f"{chave}: {valor}")
        print("--------------------------------------")

if __name__ == "__main__":
    main()