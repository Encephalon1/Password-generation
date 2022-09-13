import random
import string


def generate_password():
    count = 0
    password = ''
    while count <= 12:
        count += 1
        letters = string.ascii_letters
        nums = '0123456789'
        syms = f'{letters}{nums}'
        password += random.choice(syms)
    return password


def save_password():
    password = generate_password()
    use = input('Введите сервис, для которого будет использоваться пароль: ')
    my_password = f'{use}: {password}'
    with open('passwords.txt', 'a') as file:
        file.write(my_password)


save_password()
