# Valores de retorno

# Devolvendo um valor simples
def get_formatted_name(first_name, last_name):
    """ Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Deixando um argumento opcional
def get_formatted_names(first_name, last_name, middle_name=''):
    """Devolve um nome completo formatado de modo elegante."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()

musician = get_formatted_names('jimi', 'hendrix')
print(musician)
musician = get_formatted_names('john', 'hooker', 'lee')
print(musician)

# Devolvendo um dicionário
def build_person(first_name, last_name, age=''):
    """Devolve um dicionário com informações sobre uma pessoa."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Usando uma função com um laço while
def get_formatted_name(first_name, last_name):
    """ Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your")
    print("(enter 'q' at any time for quit)")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    if f_name == 'q' or l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

## Exercicíos

# 8.6 - Nomes de cidade
def city_country(city, country):
    full_location = '"' + city + ', ' + country + '"'
    return full_location.title()

locale = city_country('porto alegre', 'brasil')
print(locale)

# 8.7 - Album
def make_album(artist, disco, songs=''):
    album = {'name': artist, 'disc': disco }
    if songs:
        album['songs'] = songs
        return album

discografia = make_album('deep purple', 'shades of deep purple', 9)
print(discografia)

