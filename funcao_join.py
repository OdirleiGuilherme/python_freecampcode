# JOIN une os elementos de um iterável em uma string com um separador

my_list = ['Odirlei', 'da', 'Silva', 'Guiherme']

uniao = ' '.join(my_list)

print(uniao)

# starwith(prefix) Retorna um valor booleano indicando se uma string
# começa com o prefixo especificado.

palavra_str = 'Bom Dia'

palavra_inicia = palavra_str.startswith('Bom')
print(palavra_inicia)

# endswith(suffix) Retorna um valor booleano indicando se uma string
# termina com o sufixo especificado.

palavra_termina = palavra_str.endswith('Dia')
print(palavra_termina)

# .FIND Ele busca o texto informado e retorna o índice da primeira ocorrência onde esse texto é encontrado.

texto = 'Vingadores Avante!'

texto_find = texto.find('Avante')
texto_find2 = texto.find('Ghost Rider') # Quando não existir a palavra pesquisada com find o returnovai ser -1
print(texto_find)
print(texto_find2)

# COUNT retorna o número de vezs que uma substring aparece em uma string

frase = 'O Rato Roeu a Roupa o Rei de Roma'
frase_count = frase.count('o') # vaiser impresso 5 letras 'o" pois o minúsculo é diferente do maiúsculo
frase_count2 = frase.count('R')
print(frase_count)
print(frase_count2)