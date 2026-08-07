preco_base = 40
desconto = preco_base - (15/100) * 40
tipo_assento = 'Ouro'
horario_sessao = 'Noite'
membro = True
fim_de_semana = False


idade = int(input('digite sua idade: '))

if idade > 18: 
    print('O usuário está apto para reservar um ingresso')
else:
    print('Não apto para realizar reserva de ingresso')

if idade >= 21: 
    print('O usuário tem direito a ingresso para o show noturno!')
else:
    print('Sem direito para ir ao show noturno')

if membro is True:
    desconto_membro = desconto
    print(f'Seu ingresso saiu por R$ {desconto_membro} por ser membro')
else:
    print(f'O preço do igresso é R$ {preco_base}' )
