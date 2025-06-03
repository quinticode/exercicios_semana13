# 2. Crie uma função chamada e_palindromo que receba uma string como
# parâmetro e retorne True se a string for um palíndromo (ou seja, se lida de trás
# para frente for igual à original) e False caso contrário.

def e_palindromo(string):

    tamanho = len(string)
    
    for i in range(tamanho // 2): # isso aqui divide por dois e arredonda pro inteiro pra baixo
        
        if string[i] != string[tamanho - i - 1]:
            return False
        return True
    

print(e_palindromo("aaaa"))
print(e_palindromo("ana"))
print(e_palindromo("radar"))
print(e_palindromo("Marina"))
print(e_palindromo("falsidade"))
print(e_palindromo("socorrosubinoonibusemmarrocos"))
