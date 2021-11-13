uppercase_letters  = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у','ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
capital_letters= ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф','Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
uppercase_letters_eng= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
capital_letters_eng = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
symbols = [';', ',', '.', ' ', ':', '!', '?', '^', '+', '-', '_']

def encrypt(text, n):
    result = []
    for i in text:
        letters = 1
        if i in capital_letters_eng:
            letters = capital_letters_eng
        elif i in uppercase_letters_eng:
            letters = uppercase_letters_eng
        elif i in uppercase_letters:
            letters = uppercase_letters
        elif i in capital_letters:
            letters =capital_letters
        elif i in symbols:
            result.append(i)
            letters = -1

        if letters != 1 and letters != -1:
            index = letters.index(i)
            change_letter = (index + n) % 26
            new_letter = letters[change_letter]
            result.append(new_letter)
        elif letters != -1:
            print('Ошибка! нет такого элемента', i)

    return result


def decrypt(text, key):
    decryption = ""
    for i in text:
        alphabet = 1
        if i in capital_letters_eng:
            alphabet =capital_letters_eng
        elif i in uppercase_letters_eng:
            alphabet =uppercase_letters_eng
        elif i in uppercase_letters:
            alphabet = uppercase_letters
        elif i in capital_letters:
            alphabet = capital_letters
        elif i in symbols:
            decryption += i

        if alphabet != 1:
            c_index = alphabet.index(i)

            c_og_pos = (c_index - key) % 26

            c_og = alphabet[c_og_pos]

            decryption += c_og
    return decryption


def encrypt2(text, key):
    length = len(key)
    indexes = [ord(i) for i in key]
    indexes_of_letters = [ord(i) for i in text]
    result = ''
    for i in range(len(indexes_of_letters)):
        letter = (indexes_of_letters[i] + indexes[i % length]) % 26
        result += chr(letter + 65)
    return result


def decrypt2(text, key):
    length = len(key)
    indexes = [ord(i) for i in key]
    indexes_text = [ord(i) for i in text]
    result = ''
    for i in range(len(indexes_text)):
        letter = (indexes_text[i] - indexes[i % length]) % 26
        result += chr(letter+ 65)
    return result


print('Шифр Цезаря')
st='Hello, я Юля!'
print('До :', st)
caesar = ''.join(encrypt(st, 3))
print('После:',caesar)
print('..............................')
print('Шифр Вернама')
st2= 'Ilovemylife'
key = 'auid'
print('До:', st2)
vernam = encrypt2(st2.upper(), key.upper())
print('После: ', vernam)
vernam2 = decrypt2(vernam, key.upper())
print('До: ', vernam2)