# Crie uma função chamada maior_elemento que receba uma lista de números
# como parâmetro e retorne o maior elemento dessa lista.

def maior_elemento(lista):

    maior = float('-inf')
    
    for i in range(len(lista)):

        if lista[i] > maior:
            maior = lista[i]
    
    return maior

print(maior_elemento([1,2,3,4,5,6]))
print(maior_elemento([10,5,3,-1]))
print(maior_elemento([-1,-2,-3,-4]))
print(maior_elemento([-1,55555,-3,-4]))
