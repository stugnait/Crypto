def affine_encrypt(text, a, b, m=26):
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Перевірка, чи є символ літерою
            shift_base = 65 if char.isupper() else 97  # Визначення бази (A або a)
            t = ord(char.lower()) - 97  # Переведення літери в числовий код (0-25)
            encrypted_char = chr((a * t + b) % m + shift_base)  # Афінне шифрування
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Не шифруємо пробіли та інші символи
    return encrypted_text


# Читання тексту з файлу
with open('resources/input_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Введення значень a і b
a = int(input("Введіть значення a (повинно бути взаємно простим з 26): "))
b = int(input("Введіть значення b: "))

# Шифрування
encrypted_text = affine_encrypt(text, a, b)

# Запис зашифрованого тексту в файл
with open('resources/encrypted_text.txt', 'w', encoding='utf-8') as file:
    file.write(encrypted_text)

print("Текст успішно зашифровано!")
