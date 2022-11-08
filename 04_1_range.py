for value in range(1, 6):
    print(value)

# Colocar números numa lista
numbers = list(range(1, 6))
print(numbers)

# Pares entre 1 e 10 numa lista
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Dez primeiros quadrados perfeitos numa lista
squares = []
for value in range (1, 11):
    squares.append(value**2)
print(squares)

# Menor valor, maior e a soma dos digítos
digits =[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# IMPORTANTE: List Comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)

### Exercícios

# 4.3 - Contando até vinte
for vinte in range(1, 21):
    print(vinte)

# 4.4 - Um milhão
#milhao = []
#for lista in range(1, 1000001):
#    milhao.append(lista)
#    print(lista)

#print(min(milhao))
#print(max(milhao))

# 4.5 - Somando
#print(sum(milhao))

# 4.6 - Números ímpares
for impares in range(1, 21, +2):
    print(impares)

# 4.7 - Três
for tres in range(3, 31, +3):
    print(tres)

# 4.8 - Cubos
cubos = []
for cubo in range(1, 11):
    cubos.append(cubo**3)
print(cubos)

# 4.9 - Comprehesion de cubos
cubos = [cubo**3 for cubo in range(1, 11)]
print(cubos)