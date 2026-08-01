
# Escreva uma função chamada validar_texto(dado) que recebe um parâmetro.

# Se dado for do tipo str (string), retorne: "Entrada válida: é uma string".

# Caso contrário, retorne: "Entrada inválida: esperava uma string".

# Dica: Utilize isinstance(dado, str) para a verificação.

def validar_texto(dado):
    if isinstance(dado, str):
        return 'Entrada Válida: Uma String foi inserida'
    else:
        return 'Entrada Inválida: Estava aguardando uma String!'
print(validar_texto('Olá MUndo'))