current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Usando uma flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Usando 'break' para sair de um laço (Break pode ser usando em qualquer laço)
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# Usando 'continue' em um laço
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# Evitando loops infinitos
x = 1
while x <= 5:
    print(x)
    x += 1

## Exercícios

# 7.4 - Ingredientes para uma pizza
while True:
    ingrediente = input("Qual ingrediente gostaria de adicionar na sua pizza: ")
    if ingrediente == 'quit':
        break
    else:
        print("Adicionado " + ingrediente.title() + " a sua pizza...")


        