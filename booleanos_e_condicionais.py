# As instruções condicionais, ou condicionais, permitem controlar o fluxo do programa com base no fato de determinadas condições serem verdadeiras ou falsas.
# ==	Igual	Verifica se dois valores são iguais.
# !=	Não é igual	Verifica se dois valores são diferentes.
# >	Maior que	Verifica se o valor à esquerda é maior que o valor à direita.
# <	Menor que	Verifica se o valor à esquerda é menor que o valor à direita.
# >=	Maior ou igual a	Verifica se o valor à esquerda é maior ou igual ao valor à direita.
# <=	Menor ou igual a	Verifica se o valor à esquerda é menor ou igual ao valor à direita.

# Aqui estão algumas dessas expressões que resultam em Trueou False:
# print(3 > 4) # False
# print(3 < 4) # True
# print(3 == 4) # False
# print(4 == 4) # True
# print(3 != 4) # True
# print(3 >= 4) # False
# print(3 <= 4) # True

# Esses operadores podem ser usados ​​em condicionais para comparar valores e executar determinado 
# código com base no resultado da condicional, se verdadeira Trueou falsa False.

# CONDIÇÃO IF: 
# if - As declarações começam com a if (palavra-chave).
# condition é uma expressão que avalia para Trueou False, seguida por dois pontos ( :).

age = int(input('informe sua idade: '))
if age <= 11:
    print(f'Você ainda tem {age} anos, ainda é criança!')

# CONDIÇÃO ELSE: 
# A cláusula else é executada quando a condição if é falsa. Aqui está a sintaxe de uma if…else instrução:

age = int(input('Quantos anos você tem: '))
if age <= 35:
    print(f'Você tem {age} anos, ainda é novo!')
else:
    print(f'Ah tá com {age} anos, tá ficando coroa hein')

# CONDIÇÃO ELIF (IF+ELSE)
# Pode haver situações em que você queira levar em conta múltiplas condições. 
# Para isso, o Python permite que você estenda sua instrução if com a elifpalavra-chave (else if).

age = int(input('Quantos anos você tem: '))
if age <= 10:
    print(f'Você tem {age} anos, é criança')
elif age <=59:
    print(f'{age} anos, você é um adulto')
else:
    print(f'Ah tá com {age} anos, você é um idoso')

#Em Python, todo valor possui um valor booleano inerente, ou seja, 
# um sentido embutido que indica se ele deve ser tratado como verdadeiro Trueou falso Falseem um contexto lógico. 
# Muitos valores são considerados verdadeiros (truthy) , isto é, são avaliados como verdadeiros Trueem um contexto
# lógico. Outros são falsos (falsy) , ou seja, são avaliados como falsos False.
# Aqui estão alguns valores falsos:

# * None
# * False
# * Número integer 0
# * Número float 0.0
# * cadeias vazias " "

# Outros valores, como números diferentes de zero e sequências de caracteres não vazias, 
# são considerados verdadeiros.Se você quiser verificar se um valor é verdadeiro (truthy) ou falso (falsy),
#  pode usar a função integrada bool(). Ela converte explicitamente um valor para 
# seu equivalente booleano e retorna verdadeiro True(truthy) para valores 
# verdadeiros e falso False(falsy) para valores falsos. Aqui estão alguns exemplos:

print(bool(False))
print(bool(0))
print(bool(''))
print(bool(True))
print(bool(3))
print(bool('Olá Mundo'))

