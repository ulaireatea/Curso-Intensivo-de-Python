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

# Percorrendo todas as chaves de um dicionário com um laço

