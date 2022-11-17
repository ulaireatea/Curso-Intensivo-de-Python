def greet_user(username):
    """ Exibe uma saudação simples."""
    print("Hello, "+ username.title() + "!")
greet_user('jesse')


## Exercícios

# 8.1 - Mensagem
def display_message(topic):
    print("This chapter, we learn: " + topic.title() + ".")
display_message('functions')

# 8.2 - Livro favorito
def favorite_book(book):
    print("My favorite book is: " + book.title())
favorite_book('alice in the wonderlands')