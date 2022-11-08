# Fatiando
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# Percorrendo lista
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copiando lista
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite food are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

### Exercícios

# 4.10 - Fatias
items = ['monitor', 'keyboard', 'cpu', 'mouse', 'modem']
print("The first three items of the list are:")
print(items[:3])
print("Three items in middle are:")
print(items[1:4])
print("The last three items are:")
print(items[-3:])

# 4.11 - Minhas pizzas, suas pizzas
pizzas = ['calabresa', 'portuguesa', 'suprema']

for pizza in pizzas:
    print("I like " + pizza.title() + " pizza.\n")

print("I really like pizzas.")

friend_pizzas = pizzas[:]
pizzas.append('peperoni')
friend_pizzas.append('mussarela')

print("My favorites pizzas are:")
for pizza in pizzas:
    print(pizza)
    print('\n')

print("The favorites pizzas of my friends are:")
for friend in friend_pizzas:
    print(friend)
    print('\n')

# 4.12 - Mais laços
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
for food in my_foods:
    print(food)
for f_foods in friend_foods:
    print(f_foods)