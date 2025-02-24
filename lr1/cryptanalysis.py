from collections import Counter

def frequency_analysis(text):
    text = ''.join([char.lower() for char in text if char.isalpha()])
    letter_counts = Counter(text)
    total_letters = sum(letter_counts.values())
    frequency = {char: count / total_letters for char, count in letter_counts.items()}
    return frequency

def decrypt(text, shift):
    decrypted_text = []
    for char in text:
        if char.isalpha():
            new_char = chr(((ord(char.lower()) - ord('a') - shift) % 26) + ord('a'))
            decrypted_text.append(new_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)


# Зчитування зашифрованого тексту з файлу
with open('resources/encrypted_text.txt', 'r', encoding='utf-8') as file:
    encrypted_text = file.read()

# Виконання частотного аналізу
frequencies = frequency_analysis(encrypted_text)

# Виведення частот
print("Частоти літер у зашифрованому тексті:")
for char, freq in sorted(frequencies.items(), key=lambda x: x[1], reverse=True):
    print(f"{char}: {freq:.4f}")

# Пошук ймовірного зсуву на основі частоти літери
most_frequent_char = max(frequencies, key=frequencies.get)
shift = (ord(most_frequent_char) - ord('e')) % 26
print(f"Ймовірний зсув: {shift}")

decrypted_text = decrypt(encrypted_text, shift)
print("Розшифроване слово/текст:")
print(decrypted_text)