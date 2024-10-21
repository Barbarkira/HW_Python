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
import string

def generate_password(length):
    if length < 4:  # Минимальная длина пароля
        print("Пароль должен содержать как минимум 4 символа.")
        return None

    lowercase_letters = string.ascii_lowercase  # строчные буквы
    uppercase_letters = string.ascii_uppercase  # заглавные буквы
    digits = string.digits  # цифры
    special_characters = string.punctuation

    password_characters = (
        random.choice(lowercase_letters) +
        random.choice(uppercase_letters) +
        random.choice(digits) +
        random.choice(special_characters)
    )


    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password_characters += ''.join(random.choice(all_characters) for _ in range(length - 4))

    password = ''.join(random.sample(password_characters, len(password_characters)))

    return password


try:
    length = int(input("Введите длину пароля (минимум 4): "))
    generated_password = generate_password(length)
    if generated_password:
        print(f"Сгенерированный пароль: {generated_password}")
except ValueError:
    print("Пожалуйста, введите корректное число.")



