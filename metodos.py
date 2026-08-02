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

# CAPITALIZE() Retorna uma nova string com a primeira etra maiúscula e as demais minúsculas

palavra = 'avião'

palavra_capitalaze = palavra.capitalize()
print(palavra_capitalaze)

# ISUPPER(): Retorna verdadeiro(True) se todas as letras na string forem maiúsculas e (False)
# falso caso contrário.

palavra2 = 'hello world'
palavra_isupper = palavra2.isupper()
print(palavra_isupper)

# ISLOWER(): Retorna verdadeiro Truese todas as letras na string forem minúsculas e Falsefalso caso contrário.
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)

# TITLE(): Retorna uma nova string com a primeira letra de cada palavra em maiúscula.

my_str = 'seja bem-vindo!'

my_str_title = my_str.title()
print(my_str_title)