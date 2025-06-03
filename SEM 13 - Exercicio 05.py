# Implemente uma calculadora simples em Python utilizando funções. A
# calculadora deve ser capaz de realizar as seguintes operações
# matemáticas básicas:
# • Soma
# • Subtração
# • Multiplicação
# • Divisão
# Requisitos:
# • Crie uma função para cada operação matemática (soma,
# subtração, multiplicação e divisão). As funções devem receber
# dois valores e retornar o resultado da operação.
# • Implemente uma função para exibir o menu de opções para o
# usuário.
# • O programa deve repetir o menu após cada operação, até que
# o usuário escolha a opção de sair.

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


def menu():

    print(f"=-=-= Bem-vindo(a) à Calculadora! =-=-=\n")
    print(f"=-=-= > Soma (+) [1]")
    print(f"=-=-= > Subtração (-) [2]")
    print(f"=-=-= > Multiplicação (*) [3]")
    print(f"=-=-= > Divisão (/) [4]")
    print(f"=-=-= > Sair [5]\n")
    return input("Escolha uma das opções: ")


def soma(a,b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def sair():
    print("\nVocê saiu da calculadora! Muito obrigado por utilizar o programa! :)")



#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

while True:

    opcao = menu()
    
    if opcao == "5":
        sair()
        break

    a = int(input("Escolha o primeiro número: "))
    b = int(input("Escolha o segundo número: "))

    if opcao == "1":
        print(f"\nA RESPOSTA É: {soma(a,b)}\n")

    elif opcao == "2":
        print(f"\nA RESPOSTA É: {subtracao(a,b)}\n")

    elif opcao == "3":
        print(f"\nA RESPOSTA É: {multiplicacao(a,b)}\n")

    elif opcao == "4":
        print(f"\nA RESPOSTA É: {divisao(a,b)}\n")

    else:
        print("Escolha uma opção válida!")
