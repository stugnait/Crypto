import os


def mod_inverse(a , m):
    """Знаходить мультиплікативне обернене (a^(-1) mod m)"""
    for x in range(1 , m):
        if (a * x) % m == 1:
            return x
    return None


def affine_decrypt(text , a , b):
    """Розшифровує текст за допомогою афінного шифру"""
    decrypted_text = ""
    a_inv = mod_inverse(a , 26)

    if a_inv is None:
        print("Помилка: не існує мультиплікативного оберненого числа для a!")
        return None

    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decrypted_char = chr(((a_inv * (ord(char) - offset - b)) % 26) + offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # зберігаємо символ без змін
    return decrypted_text


def main():
    input_file = input("Введіть ім'я зашифрованого файлу: ")

    if not os.path.exists(input_file):
        print("Файл не знайдено!")
        return

    with open(input_file , "r" , encoding = "utf-8") as f:
        lines = f.readlines()

    # Отримуємо значення a і b з першого рядка
    a , b = map(int , lines[0].split())
    ciphertext = "".join(lines[1:])  # решта рядків — це сам шифротекст

    decrypted_text = affine_decrypt(ciphertext , a , b)

    if decrypted_text:
        print("\nРозшифрований текст:")
        print(decrypted_text)


if __name__ == "__main__":
    main()
