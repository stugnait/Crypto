import os


def generate_gamma(key , length):
    """Генерує псевдовипадкову гамму за допомогою ключа"""
    a , b , c = key
    gamma = []
    for i in range(length):
        gamma.append((a * i + b) % 256)  # Генеруємо байти гамми
        a , b , c = b , c , (a + b + c) % 256  # Оновлення параметрів
    return gamma


def encrypt_file(input_filename , output_filename , key):
    """Шифрує файл за допомогою шифру гаммування"""
    with open(input_filename , 'r' , encoding = 'utf-8') as f:
        plaintext = f.read()

    gamma = generate_gamma(key , len(plaintext))
    ciphertext = [chr(ord(char) ^ gamma[i]) for i , char in enumerate(plaintext)]  # XOR
    encrypted_text = ''.join(ciphertext)

    with open(output_filename , 'w' , encoding = 'utf-8') as f:
        f.write(encrypted_text)

    print(f"Файл зашифровано та збережено у {output_filename}")


if __name__ == "__main__":
    input_file = input("Введіть ім'я вхідного файлу: ")
    output_file = "encrypted.txt"
    key = tuple(map(int , input("Введіть 3 числа для сеансового ключа (через пробіл): ").split()))

    if len(key) != 3:
        print("Помилка: потрібно ввести рівно 3 числа!")
    else:
        encrypt_file(input_file , output_file , key)
