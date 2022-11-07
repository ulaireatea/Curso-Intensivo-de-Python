name = "ada lovelace"
# title() primeira letra de cada palavra da string maiúscula
print(name.title())

# upper() todas letras da string maiúsculas
print(name.upper())

# lower() todas letras da string minúsculas
print(name.lower())

# concatenando
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
# print(full_name)
# print("Hello, " + full_name.title() + '!')
message = "Hello, " + full_name.title() + "!"
print(message)

# \t = tabulação
# \n = quebra de linha

print("Languages: \n\tPython\n\tJavascript")


# removendo espaçoes em brancos das strings temporariamente (bom para verificação de acesso por login)

favorite_language = ' python '
# lado direito
favorite_language.rstrip()
print(favorite_language)
# lado esquerdo
favorite_language.lstrip()
print(favorite_language)
# ambos lados
favorite_language.strip()
print(favorite_language)

# removendo espaços em brancos permanentemente

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

### Exercicios

# 2.3 - Mensagem pessoal:
name = "Eric"
print("Alô " + name + ", você gostaria de aprender um pouco de Python hoje?")

# 2.4 - Letras maipusculas e minúsculas em nomes:
name = "Eric"
print(name.lower(), name.upper(), name.title())

# 2.5 - Citação famosa
name = "albert einstein"
quote = '"Uma pessoa que nunca cometeu um erro jamais tentou nada novo."'
print(name.title() + " certa vez disse: " + quote)

# 2.6 - Removendo caracteres em branco de nomes
name = "  Eric "
print(name.lstrip(), "\n", name.rstrip(), "\n", name.strip(), '\n''\t', name)
