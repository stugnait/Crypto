def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Зчитування тексту з файлу
with open('resources/input_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Введення зсуву
shift = int(input("Введіть величину зміщення для шифру Цезаря: "))

# Шифрування
encrypted_text = caesar_cipher_encrypt(text, shift)

with open('resources/encrypted_text.txt', 'w', encoding='utf-8') as file:
    file.write(encrypted_text)

print("Текст успішно зашифровано!")
