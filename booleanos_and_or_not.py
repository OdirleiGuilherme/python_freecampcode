''' Existem três operadores booleanos em Python: and`&` or, `&` e `& not`.
 Vamos primeiro analisar o AND.
 O and operador recebe dois operandos e retorna o primeiro se for falso; caso contrário, retorna o segundo. 
 Ambos os operandos devem ser verdadeiros para que uma expressão resulte em um valor verdadeiro.'''

cidadao = True
age = str(34) # transformando int para string para concatenar com a string 'Anos de idade'
age+= ' Anos de idade'

print(cidadao and age) # vai imprimir somante 34 anos de idade.

