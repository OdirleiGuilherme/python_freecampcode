primeiro_nome = input('Informe primeiro nome: ')
ultimo_nome = input('Informe último nome: ')
nome_completo = primeiro_nome + ' ' + ultimo_nome

idade_funcionario = int(input('Digite sua idade: '))

#endereco = input('Informe nome da rua: ')
#numero_endereco = int(input('nº da residência: '))
#bairro = input('informe bairro: ')
#municipio = input('informe município: ')
#estado = input('Informe estado: ')

empregado_info = nome_completo+', '+ str( idade_funcionario)+ ' anos'


print(empregado_info)


