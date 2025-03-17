import itertools

# Таблиці перестановок та підстановок для S-DES
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]
S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]

def permute(bits, table):
    return [bits[i-1] for i in table]

def left_shift(bits, shifts):
    return bits[shifts:] + bits[:shifts]

def key_schedule(key):
    key = permute(key, P10)
    left, right = key[:5], key[5:]
    left, right = left_shift(left, 1), left_shift(right, 1)
    K1 = permute(left + right, P8)
    left, right = left_shift(left, 2), left_shift(right, 2)
    K2 = permute(left + right, P8)
    return K1, K2

def s_box(bits, box):
    row = int(f"{bits[0]}{bits[3]}", 2)
    col = int(f"{bits[1]}{bits[2]}", 2)
    return list(map(int, f"{box[row][col]:02b}"))

def f_k(bits, key):
    left, right = bits[:4], bits[4:]
    expanded = permute(right, EP)
    xor_res = [b ^ k for b, k in zip(expanded, key)]
    s0_out = s_box(xor_res[:4], S0)
    s1_out = s_box(xor_res[4:], S1)
    p4_out = permute(s0_out + s1_out, P4)
    return [l ^ p for l, p in zip(left, p4_out)] + right

def sdes_encrypt(plain_text, key):
    bits = permute(plain_text, IP)
    K1, K2 = key_schedule(key)
    bits = f_k(bits, K1)
    bits = bits[4:] + bits[:4]
    bits = f_k(bits, K2)
    return permute(bits, IP_INV)

def sdes_decrypt(cipher_text, key):
    bits = permute(cipher_text, IP)
    K1, K2 = key_schedule(key)
    bits = f_k(bits, K2)
    bits = bits[4:] + bits[:4]
    bits = f_k(bits, K1)
    return permute(bits, IP_INV)

def string_to_bits(s):
    return [list(map(int, f"{ord(c):08b}")) for c in s]

def bits_to_string(b):
    return ''.join(chr(int(''.join(map(str, byte)), 2)) for byte in b)

def encrypt_string(text, key):
    return [sdes_encrypt(byte, key) for byte in string_to_bits(text)]

def decrypt_string(encrypted_text, key):
    return bits_to_string([sdes_decrypt(byte, key) for byte in encrypted_text])

# Тестування
key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]  # Приклад ключа
plain_text = "NIHAO"
cipher_text = encrypt_string(plain_text, key)
decrypted_text = decrypt_string(cipher_text, key)

print("Вхідний текст:", plain_text)
print("Зашифрований текст (біти):", cipher_text)
print("Розшифрований текст:", decrypted_text)

# Перевірка на різних ключах
key2 = [0, 1, 0, 1, 1, 1, 1, 1, 0, 1]
cipher_text2 = encrypt_string(plain_text, key2)
decrypted_text2 = decrypt_string(cipher_text2, key2)

print("Зашифрований текст (інший ключ, біти):", cipher_text2)
print("Розшифрований текст (інший ключ):", decrypted_text2)