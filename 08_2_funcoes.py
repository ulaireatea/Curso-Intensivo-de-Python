# Valores default

def describe_pet(pet_name, animal_type='dog'):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".") 
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet('willie')

## Exercícios

# 8.3 - Camiseta, e 8.4 - Camisetas grandes
def make_shirt(size='G', message='Eu amo Python'):
    print("\nEstá camiseta será tamanho: " + size + ", e terá a seguinte estampa: " + message)

make_shirt('M', 'Physics Rules!')
make_shirt(message='Metallica', size='P')
make_shirt()
