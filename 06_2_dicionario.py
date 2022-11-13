# Percorrendo todos os pares chave-valor com um laço
user_0 = {
    'username': 'efermi', 'first': 'enrico', 'last': 'fermi', }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# Percorrendo todas as CHAVES de um dicionário com um laço
favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + 
        favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Percorrendo as chaves de um dicionario usando um laço - ORDENADO
favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Percorrendo todos os VALORES de um dicionário com um laço
favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Para verificar os valores SEM repetições
favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

### Exercícios

# 6.5 - Rios
rios = {'nilo': 'egito', 'amazonas': 'brasil', 'mississipi': 'estados unidos'}
for rio, pais in rios.items():
    print("O " + rio.title() + " corre pelo " + pais.title() + ".")
for rio in rios:
    print(rio.title())
for rio in rios.values():
    print(rio.title())

# 6.6 - Enquete
favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
peoples = ['robert', 'watson', 'sarah', 'jen']
for people in peoples:
    if people in favorite_languages:
        print(people.title() + ", thank you for participate.")
    else:
        print(people.title() + ", please, answer the questionary.")