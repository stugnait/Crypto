def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Зчитування зашифрованого тексту з файлу
with open('resources/encrypted_text.txt', 'r', encoding='utf-8') as file:
    encrypted_text = file.read()

# Розшифрування
shift = int(input("Введіть величину зміщення для розшифровки: "))
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

# Виведення розшифрованого тексту на екран
print("Розшифрований текст:")
print(decrypted_text)
