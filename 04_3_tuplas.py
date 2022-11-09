# Tuplas são dados simples, utilizados para quando não se quer alterar os dados durante o programa
dimensions = (200, 50)
print(dimensions[0]) 
print(dimensions[1])

# Percorrendo um tupla
for dimension in dimensions:
    print(dimension)

# Sobrescrevendo um tupla
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

### Exercícios

# 4.13 - Buffet
buffets = ('Arroz', 'Feijão', 'Batata', 'Bife', 'Salada')
for buffet in buffets:
    print(buffet)

buffets = ('Arroz', 'Feijão', 'Batata', 'Chuleta', 'Molho')
for buffet in buffets:
    print(buffet)

