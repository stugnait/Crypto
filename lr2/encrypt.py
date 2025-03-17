import os


def gcd(a , b):
    """Обчислює найбільший спільний дільник (НСД) для взаємно простих значень"""
    while b:
        a , b = b , a % b
    return a


def mod_inverse(a , m):
    """Знаходить мультиплікативне обернене (a^(-1) mod m)"""
    for x in range(1 , m):
        if (a * x) % m == 1:
            return x
    return None


def affine_encrypt(text , a , b):
    """Шифрує текст за допомогою афінного шифру"""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_char = chr(((a * (ord(char) - offset) + b) % 26) + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # зберігаємо символ без змін
    return encrypted_text


def main():
    input_file = input("Введіть ім'я вхідного файлу: ")
    output_file = "encrypted_" + input_file

    if not os.path.exists(input_file):
        print("Файл не знайдено!")
        return

    a = int(input("Введіть значення a (має бути взаємно простим із 26): "))
    while gcd(a , 26) != 1:
        print("Число a не є взаємно простим із 26! Введіть інше значення.")
        a = int(input("Введіть значення a: "))

    b = int(input("Введіть значення b: "))

    with open(input_file , "r" , encoding = "utf-8") as f:
        plaintext = f.read()

    ciphertext = affine_encrypt(plaintext , a , b)

    with open(output_file , "w" , encoding = "utf-8") as f:
        f.write(f"{a} {b}\n{ciphertext}")

    print(f"Файл '{output_file}' успішно збережено!")


if __name__ == "__main__":
    main()