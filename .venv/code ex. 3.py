# Task 3. Password Generator
# Напишите генератор паролей. Хороший пароль
# должен содержать
# строчные буквы
# заглавные буквы
# цифры
# символы
# Пароли должны быть случайными. Пользователь должен иметь возможность задать длину пароля.
# Используйте модуль: https://docs.python.org/3.3/library/random.html

import random
lengthp = int(input("Задайте длину пароля: "))
def password(length):
    if length < lengthp:
        print('Пароль ненадежен')
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'  # строчные буквы
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # заглавные буквы
    digits = '0123456789'  # цифры
    symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?/'  # специальные символы
    fullpassword = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    if length > lengthp:
        all_characters = lowercase_letters + uppercase_letters + digits + special_characters
        fullpassword += random.choices(all_characters, k=length - 4)
    random.shuffle(fullpassword)
    return ''.join(fullpassword)
try:
    password_length = int(input("Введите длину пароля (не менее 4 символов): "))
    new_password = password(password_length)
    print("Сгенерированный пароль: ", new_password)
except ValueError as e:
    print(e)



