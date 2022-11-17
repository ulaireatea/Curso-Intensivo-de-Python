# Transferindo itens de uma lista para outra
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# verificar cada usuário até que não haja mais usuários não confirmados
# transfere cada usuário verificado para a lista de usuários confirmados
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# exibe todos os usuários confirmados
print("\nThe following users have benn confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
    
# Removendo todas instâncias de valores específicos de uma lista
pets = ['dog', 'cat', 'dog', 'goldfish', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    print(pets)


# Preenchendo um dicionário com dados de entrada do usuário
responses = {}
# define uma flag para indicar que a enquete está ativada
polling_active = True

while polling_active:
    # pede o nome da pessoa e a resposta
    name = input("\nWhats your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # armazena a resposta no dicionário
    responses[name] = response

    # descobre se outra pessoa vai responder à enquete
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
        
        # a enquete foi concluída
        print("\n--- Poll Results ---")
        for name, response in responses.items():
            print(name + " would like to climb " + response + ".")

## Exercícios

# 7.8 - Lanchonete
sandwich_orders = ['bauru', 'xis', 'beirute', 'chivito']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print("Preparei seu prato: " + sandwich.title())
    finished_sandwiches.append(sandwich)
print("Os seguintes pratos foram preparados: ")
print(finished_sandwiches)

# 7.9 - Sem pastrami
sandwich_orders = ['pastrami', 'atum', 'pastrami', 'pastrami', 'mortadela', 'presunto']
message = print("A Lanchonete esta sem pastrami\n")
finished_sandwiches = []
for sandwich in sandwich_orders:
    print("Preparei seu sanduíche: " + sandwich.title())
    finished_sandwiches.append(sandwich)
print("Os seguintes pratos foram preparados: ")
print(finished_sandwiches)
while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove('pastrami')
    print(finished_sandwiches)

# 7.10 - Férias dos sonhos
responses = {}
active = True

while active:
    name = input("\nQual seu nome? ")
    response = input("Se pudesse visitar um lugar do mundo, para onde você iria? ")
    responses[name] = response
    repeat = input("Outra pessoa vai responder? (yes/no) ")
    if repeat == 'no':
        active = False
        print("\n--- Resultados da pesquisa ---")
        for name, response in responses.items():
            print(name.title() + " gostaria de ir para " + response.title() + ".")