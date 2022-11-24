# Passando uma lista para uma função
def greet_users(names):
    """ Exibe uma saudação simples a cada usuário da lista."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modificando uma lista em uma função (sem usar uma função)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simula a impressão de cada design, até que não haja mais nenhum
# Transfere a cada design para completed_models após impressão
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simula a criação de uma impressão 3D a partir do design
    print("Printing model: " + current_design)
    completed_models.append(current_design)

    # Exibe todos os modelos finalizados
print("\nThe following models have benn printed:")
    
for completed_model in completed_models:
    print(completed_model)

# Modificando uma lista em uma função (usando duas funções)
def print_models(unprinted_designs, completed_models):
    """ Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para completed_models após a impressão.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simula a criação de uma impressão 3D a partir do design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """ Mostra todos os modelos impressos."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)