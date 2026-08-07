preco_base = 40
tipo_assento = 'Ouro'
horario_sessao = 'Noite'

idade = int(input('digite sua idade: '))

if idade > 18: 
    print('O usuário está apto para reservar um ingresso')
else:
    print('Não apto para realizar reserva de ingresso')

if idade >= 21: 
    print('O usuário tem direito a ingresso para o show noturno!')
else:
    print('Sem direito para ir ao show noturno')