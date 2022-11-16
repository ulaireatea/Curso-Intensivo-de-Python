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
    
