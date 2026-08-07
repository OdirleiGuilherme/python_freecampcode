''' Existem três operadores booleanos em Python: and`&` or, `&` e `& not`.
 Vamos primeiro analisar o AND.
 O and operador recebe dois operandos e retorna o primeiro se for falso; caso contrário, retorna o segundo. 
 Ambos os operandos devem ser verdadeiros para que uma expressão resulte em um valor verdadeiro.'''

cidadao = True
age = str(34) # transformando int para string para concatenar com a string 'Anos de idade'
age+= ' Anos de idade'

print(cidadao and age, ('foi impresso, pois os dois operando em AND são verdadeiros')) # vai imprimir somante 34 anos de idade.

''' Agora, vamos dar uma olhada no oroperador. Este operador retorna o primeiro operando se ele for verdadeiro;
 caso contrário, retorna o segundo operando. Uma orexpressão resulta em um valor verdadeiro se 
 pelo menos um operando for verdadeiro. O oroperador também é conhecido como operador de curto-circuito. 
 Aqui está um exemplo: '''

age = 19 
empregado = False
print(age or empregado, (',foi impresso pelo fato do operando OR apenas precisar de uma condição verdeira para retornar verdadeiro'))


''' Para verificar se uma ou mais expressões são verdadeiras True, podemos
utilizar o operando OR em uma condicional'''

aprovado_prova = True
idade = 17

if idade >= 18 or aprovado_prova:
    print('Você é elegivél para iniciar seu curso de formação na PRF')
else:
    print('Não elegivél para prosseguir processo no curso de formação')


