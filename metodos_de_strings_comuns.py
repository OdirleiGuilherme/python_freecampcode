phrase = 'hello world'
print(phrase.upper())  # Output: 'HELLO WORLD'

phrase2 = 'HELLO WORLD'
print(phrase2.lower())  # Output: 'hello world'

phrase3 = '   hello world  '
print(phrase3.strip())  # Output: 'hello world'

# replace(old, new) - retorna uma nova string com todas as ocorrências de 'old' substituídas por 'new'
phrase4 = 'Hello World'
print(phrase4.replace('World', 'Python'))  # Output: 'Hello Python'

nome = 'Odirlei da Silva Guilherme'
print(nome.split())  # Output: ['Odirlei', 'da', 'Silva', 'Guilherme']

nome = 'Odirlei da Silva Guilherme'
nome_split = nome.split(' ', 1)
print(nome_split)  # Output: ['Odirlei', 'da Silva Guilherme']

nome = 'Odirlei da Silva Guilherme'
print(nome.split(' ', 2))   # Output: ['Odirlei', 'da', 'Silva Guilherme'] 