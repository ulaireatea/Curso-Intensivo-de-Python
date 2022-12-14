age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# if else
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# if elif else (quanto apenas 1 condição passará)
age = 3
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("You admission cost is $10.")

# reformatando o exemplo acima
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

# vários elif
age = 19
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

# omitindo else
age = 12
if age < 4: 
    price = 0
elif age < 18: 
    price = 5
elif age < 65: 
    price = 10
elif age >= 65: 
    price = 5
print("Your admission cost is $" + str(price) + ".")

# testando inúmeras condições (quando todas condições passam pelo teste)
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'peperoni' in requested_toppings:
    print("Adding peperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza!")

### Exercícios

# 5.5 - Cores de alienígenas
alien_color = 'red'
if alien_color == 'green': 
    pts = 5
elif alien_color == 'red': 
    pts = 10
else:
    pts = 15
print("You received " + str(pts) + " pts.")

# 5.6 - Estágios da vida
age = 1
if age >=2 and age < 4:
    print("You is a child.")
elif age >=4 and age < 13:
    print("You is a young.")
elif age >= 13 and age < 20:
    print("You is a tennager.")
elif age >= 20 and age < 65:
    print("You is a adult.")
elif age >= 65:
    print("You is a older.")
else:
    print("You is a infant.")

# 5.7 - Fruta favorita
favorite_fruits = ['manga', 'morango', 'abacaxi']
if 'manga' in favorite_fruits:
    print("You really like Manga.")
if 'morango' in favorite_fruits:
    print("You really like Morango.")
if 'abacaxi' in favorite_fruits:
    print("You really like Abacaxi.")
