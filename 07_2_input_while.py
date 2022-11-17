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

