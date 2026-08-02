# Os tipos de dados numéricos principais em Python são inteiros e de ponto flutuante. 
# Com eles, você pode armazenar dados numéricos e realizar operações matemáticas.

# Os números inteiros são números sem casas decimais, positivos ou negativos
 
int_1 = 30
int_2 = -11

print(type(int_1))
print(type(int_2))

# Acima vemos que utilizando o metódo type, indica que ambos são números inteiros (integer/int)

# Agora vamos realizar uma operação de adição com números inteiros

int_3 = 17
int_4 = 32

sum_int = int_3 + int_4
print(f'A soma de {int_3} + {int_4} é {sum_int}')

# Nesse exemplo vamos subtrair com números inteiros

int_5 = 32
int_6 = 14
diff_int = int_5 - int_6
print(f'A subtração entre os núemros {int_5} - {int_6} é: {diff_int}')

# realizando multiplicação

int_7 = 5
int_8 = 5
product_int = int_7 * int_8
print(f'Multiplicando os números {int_7} * {int_8} temos o produto {product_int}')

# Agora vem a divisão, mas atenção temos 3 modos de divisão a comum (/), inteira (//), módulo ou resto da divisão( % )
# DIVISÃO COMUM

div_int = int_5 / int_7
print(f'A divisão entre {int_5} / {int_7} é {div_int}') 