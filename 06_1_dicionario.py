# Um dic de obejtos semelhantes
favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', 
}
print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() +
    ".")

### Exercícios

# 6.1 - Pessoa
person = {
    'first_name': 'Et', 'last_name': 'Varginha', 'age': 40, 
    'city': 'Porto Alegre'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6.2 - Números
favorite_numbers = {1: 'Marcelo', 2: 'Paula', 3: 'Lucas', 4: 'Ana', 5: 'Lucifer'}
print(favorite_numbers[5])

# 6.3 - Glossário (dicionario real)
glossario = {
    'append()': 'Adiciona um item ao fim da lista.',
    'extend()': 'Prolonga a lista, adicionando no fim todos os elementos do argumento iterable passado como parâmetro.',
    'insert()': 'Insere um item em uma dada posição.', 
    'remove()': 'Remove o primeiro item encontrado na lista cujo valor é igual a x.'
    }
for word, value in glossario.items():
    print(word + ':' + value + '\n')

