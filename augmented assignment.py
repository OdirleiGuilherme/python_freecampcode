# A atribuição aumentada combina uma operação binária com uma atribuição em uma única etapa. Ela recebe uma variável, 
# aplica uma operação a ela com outro valor e armazena o resultado de volta na mesma variável.

# A sintaxe básica de uma atribuição aumentada é a seguinte:

# variable <operator>= value

# Adição (+)

num1 = 26
num1 +=20
print(f'Cliente tem {num1} anos')

# Subtração (-)

contagem = 77
contagem -= 13
print(f'A temperatura caiu para {contagem} graus celsius')

# Multiplcação (*)

multi = 5
multi*= 3
print(f'Joazinho multipicou suas balasde 5 para {multi}')

# Divisão (/)

price = 200
price/= 5
print(f'Galera a divisão do churrasco ficou {price} para cada um participante.')

# Divisão inteira (//) podemos aplicar também.

paginas = 270
paginas //= 7
print(f'O total de pagina que preciso ler por dia para concluir esse livro de 270 páginas é de {paginas} por dia.')

# Aribuição por divisão modular (%)

bits = 35
bits %= 2
print(f'coloquei a batida dessa música pra {bits} bits')