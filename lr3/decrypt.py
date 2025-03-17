def generate_gamma(key, length):
    """Генерує ту ж саму гамму, що і під час шифрування"""
    a, b, c = key
    gamma = []
    for i in range(length):
        gamma.append((a * i + b) % 256)
        a, b, c = b, c, (a + b + c) % 256
    return gamma

def decrypt_file(input_filename, output_filename, key):
    """Розшифровує шифротекст"""
    with open(input_filename, 'r', encoding='utf-8') as f:
        ciphertext = f.read()

    gamma = generate_gamma(key, len(ciphertext))
    decrypted_text = [chr(ord(char) ^ gamma[i]) for i, char in enumerate(ciphertext)]
    plaintext = ''.join(decrypted_text)

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(plaintext)

    print("Розшифрований текст:")
    print(plaintext)
    print(f"Файл розшифровано та збережено у {output_filename}")

if __name__ == "__main__":
    input_file = "encrypted.txt"
    output_file = "decrypted.txt"
    key = tuple(map(int, input("Введіть 3 числа для сеансового ключа (через пробіл): ").split()))

    if len(key) != 3:
        print("Помилка: потрібно ввести рівно 3 числа!")
    else:
        decrypt_file(input_file, output_file, key)
