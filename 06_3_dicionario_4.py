# Aninhamentos

## Uma lista de dicionarios
aliens_0 = {'color': 'green', 'points': 5}
aliens_1 = {'color': 'yellow', 'points': 10}
aliens_2 = {'color': 'red', 'points': 15}

aliens = [aliens_0, aliens_1, aliens_2]
for alien in aliens:
    print(alien)

# cria uma lista vazia para armazenar alienígenas
aliens = []
#cria 30 alienígenas verdes
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

    for alien in aliens[0:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10
        elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['points'] = 15
# mostra os cinco primeiros alienígenas
for alien in aliens[:5]:
        print(alien)
print("...")


## Uma lista em um dicionário
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'], }
# resume o pedido
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# exemplo 2
favorite_languages = {
    'jen': ['python', 'ruby'], 'sarah': ['c'], 'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'], }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorites languages are:")
    for language in languages:
        print("\t" + language.title())


# Um dicionário em um dicionário
users = {
    'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton', },
    'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris', },
    }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


## Exercícios

# 6.7 - Pessoas
person = {
    'first_name': 'Et', 'last_name': 'Varginha', 'age': 20, 
    'city': 'Porto Alegre'}
person1 = {
    'first_name': 'Marcelo', 'last_name': 'Cabral', 'age': 40,
    'city': 'Porto Alegre'}
person2 = {
    'first_name': 'Lucifer', 'last_name': 'God', 'age': 666,
    'city': 'Hell'}
people = [person, person1, person2]
for id in people:
    print(id['first_name'] + " " + id['last_name'] + " " + str(id['age']) + " " + id['city'])
