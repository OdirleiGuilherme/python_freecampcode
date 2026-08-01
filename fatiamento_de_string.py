# O fatiamento de strings permite extrair uma porção de uma string ou trabalhar
#  apenas com uma parte específica dela.

# STRING[START:STOP]

# Se você quiser extrair caracteres de um determinado índice para outro,
#  basta separar os startíndices stopcom dois pontos:

hello_world_str = 'Hello World'
print(hello_world_str[1:4])
print(hello_world_str[:5])
print(hello_world_str[8:])
print(hello_world_str[:])



name = 'ODIRLEI'
print(name[3:6])
print(name[-5:-2])
print(name[0: : 3]) # iniciando no indíce START  e STOP e passando um PARÂMETRO de 3 em 3 para impressão
print(name[::-1]) # parâmetro é inverter uma string definindo `step` como `0` -1 e deixando start`and` em stop branco:

say = 'Hello'
print(say[2:])