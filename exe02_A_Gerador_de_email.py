# Crie três variáveis: nome (ex: "ana"), sobrenome (ex: "silva") e dominio (ex: "empresa.com").

# Junte essas variáveis para formar um endereço de e-mail no formato:

# "ana.silva@empresa.com"

# (Tente fazer isso de duas formas: usando a concatenação com o operador + e usando uma f-string).

nome = 'Ana'.lower()
sobrenome = 'Silva'.lower()
dominio = 'empresa.com'

email = nome +'.'+sobrenome+'@'+dominio
print(email)

print(f'{nome}.{sobrenome}@{dominio}')