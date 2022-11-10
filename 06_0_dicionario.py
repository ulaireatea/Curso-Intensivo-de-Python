alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Acessando valores no dic
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adicionando novos pares chave-valor (a ordem aramazenada não importa)
print('\n' + str(alien_0))
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Dicionario vazio (ideal para iniciar-se um dicionario)
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print('\n')
# Modificando valores no dic
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
print('\n')

# Exemplo
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move o alienígena para a direita e determina a distância que o alienígena deve se deslocar de acordo com sua velocidade atual
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# A nova posição é a antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# Removendo pares chave-valor (del) permanente
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
