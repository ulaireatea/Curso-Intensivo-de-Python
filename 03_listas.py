bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[-1])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

## Exercícios

# 3.1 - Nomes
names = ['mauro', 'Roberto', 'marcos', 'luciano', 'william']
print(names[0].title())

# 3.2 - Saudações
print("Olá caro amigo " + names[1])

# Modificando elementos da lista [ ]

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

# Adicionando elementos em lista .append() "sempre no final da lista"

motorcycles.append('triumph')
print(motorcycles)

# Adicionando elementos em posições especifícas .insert(posição, 'nome do elementos')

motorcycles.insert(0, 'ktm')
print(motorcycles)

# Removendo elementos da lista '.del lista [posição]'

del motorcycles[0]
print(motorcycles)

# Removendo com .pop()

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Removendo com .pop(posição)

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(1)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Removendo pelo nome '.remove(nome)' Apaga apenas uma ocorrência da lista, se houver necessidade de excluir mais usar laço.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print("\n")
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

### Exercícios

# 3.4 - Lista de convidados
invited = ['morrison', 'joplin', 'hendrix']
print('\n\tDear ' + invited[1].title() + ',\n\n\tCome have dinner with us.\n')

# 3.5 - Alterando a lista de convidados
canceled = 'joplin'
invited.remove(canceled)
print(invited)
print(canceled)

# 3.6 - Mais convidados
invited.insert(0, 'cantrell')
invited.insert(2, 'hammet')
invited.insert(4, 'ulrich')
print(invited)

# 3.7 - Reduzindo a lista de convidados
popped_invited = invited.pop(4), invited.pop(3), invited.pop(2)
print('Dear ' + popped_invited[0].title() + '\nSorry, but dinner was canceled.')
print('Dear ' + popped_invited[1].title() + '\nSorry, but dinner was canceled.')
print('Dear ' + popped_invited[2].title() + '\nSorry, but dinner was canceled.')

print('Dear ' + invited[0].title() + '\nWe waiting you for dinner.')
print('Dear ' + invited[1].title() + '\nWe waiting you for dinner.')

del invited[0]
del invited[0]
print(invited)
