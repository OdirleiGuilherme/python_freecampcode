# Utilizando as aspas Simples e Triplas e criando Multilinhas
msg = 'It\'s a beautiful day' # Exemplo 1
msg2 = "It's a beautiful day" # Exemplo 2
msg3 = ''' Olá aqui eu posso escrever uma mensgam
    em varias linhas , colocando o texto entre aspas triplas '''
msg4 = """ Olá aqui eu posso escrever uma mensgam
    em varias linhas , colocando o texto entre aspas triplas """

print(msg)
print(msg2)
print(msg3)
print(msg4)

# utizando IN com strings que serve para verificar se a string possui um ou mais caracter

texto = 'A pipa caiu no chão' 
print('chão' in texto)
print('menino' in texto)

# Obtendo o comprimeto de uma string com  LEN() e trabalhando com seus caracteres individuais e com indexação

texto2 = 'Rio de Janeiro'

print(len(texto2)) # 14
print(texto2[7]) # J

# A indexação negativa também é permitida, então podemos obter o último caracter da string com -1 

print(texto2[-14]) # R

greetings = 'hi'
greetings = 'hello'

print(greetings)

greeting = 'hi'
greeting[0] = 'H'

print(greeting)




