# '''Operador NOT que recebe um único operando e inverte seu valor booleano.
#  Ele converte valores verdadeiros (True) em falso (False) e valores falsos (False) em verdadeiros (True). 
# Ao contrário dos operadores anteriores que vimos, o operador NOT inverte 
# sempre retorna verdadeiro (True) ou falso (False). '''
# Exemplo:
print('Com o operador not o que é verdadeiro vira falso, o falso se torna verdadeiro')
print(not 'Hello') # retorna FALSO, pois uma string não vazia tem caractristica verdadeira
print(not '')# Uma string vazia tem caracteristica FALSA como citada acima, mas com not ela retorna como verdadeiro
print (not 0) # int em zero tem caracteristica FALS mas com not imprime verdadeiro
print(not 1)
print(not 0.0)
print(not 3.14)
print(not False)
print(not True)

# É comum usar o operador NOT em condicionais para verificar se algo não é verdadeiro (True) ou falso (False),
# como nesse exemplo: 
print('Aqui vamos verificar se a pessoa é um administrador ou não\n')
admin = False

if not admin:
    print('Acesso negado para não administradores.\n') # acesso negado para quem não é administrador
else:
    print('Seja bem-vindo, Administrador!!\n')

'''Como admin é Falso, então not admin está dizendo o que não Falso é 
Verdadeiro. Portanto, a mensagem Access denied for non-administrators.será impressa.'''

carrinho_compras = []

if not carrinho_compras:
    print('Carrinho de compras vazio\n')
else:
    print('Carrinho de compra com itens\n')

print('Vamos encher esse carrinho e ver o resultado.') 
carrinho_compras = ['maçã','uva', 'limão']

if not carrinho_compras:
    print('Carrinho de compras vazio')
else:
    print('Carrinho de compra com itens')