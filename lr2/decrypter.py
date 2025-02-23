def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_decrypt(text, a, b, m=26):
    decrypted_text = ""
    a_inv = mod_inverse(a, m)  # Обчислення оберненого елемента a за модулем m

    if a_inv is None:
        print(f"Неможливо знайти обернений елемент для a = {a}")
        return None

    for char in text:
        if char.isalpha():  # Перевірка, чи є символ літерою
            shift_base = 65 if char.isupper() else 97  # Визначення бази (A або a)
            y = ord(char.lower()) - 97  # Переведення літери в числовий код (0-25)
            decrypted_char = chr((a_inv * (y - b)) % m + shift_base)  # Афінне розшифрування
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Не шифруємо пробіли та інші символи
    return decrypted_text


# Читання зашифрованого тексту з файлу
with open('resources/encrypted_text.txt', 'r', encoding='utf-8') as file:
    encrypted_text = file.read()

# Введення значень a і b
a = int(input("Введіть значення a (повинно бути взаємно простим з 26): "))
b = int(input("Введіть значення b: "))

# Розшифрування
decrypted_text = affine_decrypt(encrypted_text, a, b)

# Виведення розшифрованого тексту на екран
if decrypted_text:
    print("Розшифрований текст:")
    print(decrypted_text)
