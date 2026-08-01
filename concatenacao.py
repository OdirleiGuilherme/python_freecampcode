
# Concatenando strings para impressãoutilizando o símbolo +
str_1 = 'Hello'
str_2 = 'World'

print(str_1 + ' ' + str_2)

# Sequência repetidas
lol = 'Buahaha'
print(lol * 5)

# Sequência repetida mais Concatenação
risada = 'Ha'
print(risada * 6 +'' + '!')

# Concatenando strings com números
# essa concatenação não funciona se tentar realiza-lá com número

name = 'Carlos'
age = 36

# print( name + '' + age)

# Traceback (most recent call last):
# File "e:\Estudando\Estudo PYTHON\python_freecampcode\concatenacao.py", line 22, in <module>
#    print( name + '' + age)
#           ~~~~~~~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str

name_and_age = name +' '+str(age) # convertando int para string

print(name_and_age)

# Podemos usar o operador de atribuição para concatenação, representado por += que realiza
# tanto a concatenação quanto a atribuição em uma única etapa.

nome = 'Vitor'
idade = 26

nome_e_idade = nome +' '
nome_e_idade +=  str(idade)
print(nome_e_idade)

