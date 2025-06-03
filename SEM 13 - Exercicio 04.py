# Crie uma função chamada contar_caracteres que receba uma string e um
# caractere como parâmetros e retorne o número de vezes que o caractere
# aparece na string.

def contar_caracteres(string, caractere):

    contador = 0

    for i in range(len(string)):

        if string[i] == caractere:
            contador += 1
        
    return contador
    
print(contar_caracteres("aaaaa","a"))
print(contar_caracteres("aaaaa","b"))
print(contar_caracteres("Marina","a"))
print(contar_caracteres("abecedario","c"))
