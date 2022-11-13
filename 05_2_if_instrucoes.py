requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

# Verificando se a lista não está vazia
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# Usando mais de uma lista
avaliable_toppings = ['mushrooms', 'oliva', 'green peppers', 'peperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

### Exercícios

# 5.8 - Olá admin
users = ['admin', 'marcelo', 'bruno', 'evandro', 'ricardo']
for user in users:
    if user == 'admin':
        print("Olá admin, gostaria de ver um relatório de status?")
    else:
        print("Olá " + user + ", obrigado por fazer login novamente.")

# 5.10 - Verificando nomes de usuário
current_users = ['Admin', 'Marcelo', 'bruno', 'evandro', 'ricardo']
for i in range(len(current_users)):
    current_users[i] = current_users[i].lower()

new_users = ['admin', 'marcelo', 'roberto', 'marcos', 'mauro']
for user in new_users:
    if user.lower() in current_users:
        print(user.title() + " você precisa fornecer outro nome válido para login.")
    else:
        print(user.title() + " este login é um nome de usuário disponível.")

# 5.11 - Números ordinais
numbers = list(range(1,10))
for n in numbers:
    if n == 1:
        print(str(n) + 'st')
    elif n == 2:
        print(str(n) + 'nd')
    elif n == 3:
        print(str(n) + 'rd')
    else:
        print(str(n) + 'th')
   


