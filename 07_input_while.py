#prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt += "\nWhat is your first name? "
#name = input(prompt) 
#print("\nHello, " + name + "!")

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!") 
else:
    print("\nYou'll be able to ride when you're a little older.")


number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0: print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.") 


## Exercícios

# 7.1 - Locação de automóveis
car = input("Qual modelo de carro você tem interesse? ")
print("Deixe-me ver se consigo um " + car.title() + " para você.")

# 7.2 - Lugares em um restaurante
pessoas = int(input("Quantas pessoas seria a mesa? "))
if pessoas > 8:
    print("Será necessário aguardar um mesa.")
else:
    print("Sua mesa está disponível.")

# 7.3 - Múltiplo de dez
num = int(input("Digite um número: "))
if (num % 10 == 0):
    print("Número é múltiplo de dez.")
else:
    print("Número não é múltiplo de dez.")

##