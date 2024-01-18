import base64
import os
import PIL
from PIL import Image, ImageSequence
from time import sleep


binary_base = [1, 2, 4, 8, 16, 32, 64, 128]

morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
                   ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
                   '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'}


def cypher(message):
    cypher_words = []
    for letter in message:
        cypher_letter = format(ord(letter), 'b')
        cypher_words.append(cypher_letter)

    return ' '.join(cypher_words)
def initialze_pixelarr(img, width, height):
    L = []
    for i in range(height):
        M = []
        for j in range(width):
            M.append(img.getpixel((j,i)))
        L.append(M)
    return L
def convert_to_average_brightness_matrix(L, width, height):
    HW = []
    for i in range(height):
        W = []
        for j in range(width):
            average = (L[i][j][0] + L[i][j][1] + L[i][j][2])/3
            W.append(average)
        HW.append(W)

    return HW

def convert_to_luminosity_matrix(L, width, height):
    HW = []
    for i in range(height):
        W = []
        for j in range(width):
            luminosity = (0.21*L[i][j][0] + 0.72*L[i][j][1] + 0.07*L[i][j][2])
            W.append(luminosity)
        HW.append(W)

    return HW

def convert_to_lightness_matrix(L, width, height):
    HW = []
    for i in range(height):
        W = []
        for j in range(width):
            lightness = (max(L[i][j][0], L[i][j][1], L[i][j][2]) + max(L[i][j][0], L[i][j][1], L[i][j][2]))/2
            W.append(lightness)
        HW.append(W)

    return HW


def assign_ascii(B, width, height):
    ascii_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    ascii_length = len(ascii_characters)

    aspect_ratio_correction = 0.55 
    A = []
    for i in range(height):
        W = []
        for j in range(width):
            try:
                avg = B[i][j]
                index = int(avg / (255 / (ascii_length - 1)) * aspect_ratio_correction)
                W.append(ascii_characters[index])
            except:
                print(index)
                break
        A.append(W)

    return A



def decipher(message):
    words = message.split(' ')
    decipher_message = []
    for word in words:
        word = str(word)
        sumatory = 0
        for value, letter in enumerate(word[::-1]):
            if int(letter) == 1:
                sumatory += binary_base[value]
        decipher_letter = chr(sumatory)
        decipher_message.append(decipher_letter)

    return "".join(decipher_message)
 
def rot1(text):
    return rotate(text, 1)

def rot2(text):
    return rotate(text, 2)

def rot3(text):
    return rotate(text, 3)

def rot4(text):
    return rotate(text, 4)

def rot5(text):
    return rotate(text, 5)

def rot6(text):
    return rotate(text, 6)

def rot7(text):
    return rotate(text, 7)

def rot8(text):
    return rotate(text, 8)

def rot9(text):
    return rotate(text, 9)

def rot10(text):
    return rotate(text, 10)

def rot11(text):
    return rotate(text, 11)

def rot12(text):
    return rotate(text, 12)

def rot13(text):
    return rotate(text, 13)

def rot14(text):
    return rotate(text, 14)

def rot15(text):
    return rotate(text, 15)

def rot16(text):
    return rotate(text, 16)

def rot17(text):
    return rotate(text, 17)

def rot18(text):
    return rotate(text, 18)

def rot19(text):
    return rotate(text, 19)

def rot20(text):
    return rotate(text, 20)

def rot21(text):
    return rotate(text, 21)

def rot22(text):
    return rotate(text, 22)

def rot23(text):
    return rotate(text, 23)

def rot24(text):
    return rotate(text, 24)

def rot25(text):
    return rotate(text, 25)


def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char == ' ':
            morse_code += ' '
        else:
            morse_code += morse_code_dict.get(char, '') + ' '
    return morse_code
def morse_to_text(morse_code):
    morse_code = morse_code.strip()
    morse_code_words = morse_code.split('   ')
    decoded_text = ''
    
    for morse_word in morse_code_words: 
        morse_chars = morse_word.split(' ')
        for morse_char in morse_chars:
            decoded_text += next((char for char, code in morse_code_dict.items() if code == morse_char), ' ')
        decoded_text += ' '

    return decoded_text.strip()

def text_to_unicode_escape(text):
    unicode_result = [f"\\u{ord(char):04x}" for char in text]
    return ''.join(unicode_result)

def rotate(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def decode_rot(input_text, shift):
    decoded_text = ""
    for char in input_text:
        if char.isalpha():
            decoded_char = chr((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 + ord('a' if char.islower() else 'A'))
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text
def unicode_escape_to_text(unicode_str):
    decoded_text = bytes(unicode_str, 'utf-8').decode('unicode-escape')
    return decoded_text
def is_english(text):
    return all(ord(char) < 128 for char in text)



def run():

    while True:

        command = str(input('''

            Привет, это мой Python-мастерский декодер и энкодер! Пожалуйста выберите ниже (1/2)

            1 - энкодер
            2 - декодер
            3 - генератор в ASKII
        '''))

        if command == '1':
            choice = str(input('''

            Выберите тип кода:
           
            1 - Двоичный код
            2 - base64
            3 - rot(rotate)
            4 - азбука морзе
            5 - юникод

           '''))
            
            if choice == '1':
                message = str(input('Напишите текст: '))
                if not is_english(message):
                    print("Только на английском!")
                else:
                    cypher_message = cypher(message)
                    print(cypher_message)

            elif choice == '2':
                encode_text = input("Напишите текст: ")
                if not is_english(encode_hash):
                    print("Только на английском!")
                else:
                    encode_hash = base64.b64encode(encode_text.encode('UTF-8')).decode('ascii')

                    print(encode_hash)

            elif choice == '3':

                input_text = input("Напишите текст: ")
                if not is_english(input_text):
                    print("Только на английском!")
                else:
                    for shift in range(1, 26):
                        encrypted_text = rotate(input_text, shift)
                        print(f"ROT{shift}: {encrypted_text}")


            elif choice == '4':
                morse_input = str(input("Введите текст:"))
                if not is_english(morse_input):
                    print("Только на английском!")
                else:
                    morse_result = text_to_morse(morse_input)
                    print(f"Текст в морском коде: {morse_result}")


            elif choice == '5':
                input_text = str(input("Введите текст:"))
                if not is_english(input_text):
                    print("Только на английском!")
                else:
                    unicode_result = text_to_unicode_escape(input_text)
                    print(unicode_result)


            else:
                print('Команда не найденна!')

        elif command == '2':
            choice = str(input('''

            Выберите тип кода:
           
            1 - Двоичный код
            2 - base64
            3 - rot(rotate)
            4 - азбука морзе
            5 - юникод


'''))
            if choice == '1':
                message = str(input('Введите двоичный код: '))
                decipher_message = decipher(message)
                print(decipher_message)

            elif choice == '2':
                decode_text = input("Введите код base64:")
                decode_hash = base64.b64decode(decode_text)
                decodeit = decode_hash.decode('UTF-8')


                print(decodeit)

            elif choice == '3':
                rot_number = int(input("Введите номер ROT (1-25): "))
                if 1 <= rot_number <= 25:
                    rot_text = input(f"Введите ROT код: {rot_number}: ")
                    decoded_text = decode_rot(rot_text, rot_number)
                    print(f"Вот тебе декодированный ROT текст{rot_number}:", decoded_text)
                else:
                    print("Номер ROT должен быть от 1 до 25.")

            elif choice == '4':
                input_text = str(input("Напишите текст: "))
                decoded_text = morse_to_text(input_text)
                print("Расшифрованный текст:", decoded_text)

            elif choice == '5':
                unicode_input = str(input('Введите unicode текст:'))
                decoded_text = unicode_escape_to_text(unicode_input)
                print(decoded_text)

            else:
                print('Команда не найденна!')
            
        elif command == '3':
            image = Image.open("filename")
            w = image.width
            h = image.height
            wnew = 632
            hnew = int(h - ((w-wnew)/w)*h)

            if hnew>160:
                hnew = 160
                wnew = int(w - ((h-hnew)/h)*w)

            for img in ImageSequence.Iterator(image):
                img_resized = img.resize((wnew, hnew)).convert("RGB")

                pixel_matrix = initialze_pixelarr(img_resized, wnew, hnew)
                brightness_matrix = convert_to_lightness_matrix(pixel_matrix, wnew, hnew)

                ascii_art = assign_ascii(brightness_matrix, wnew, hnew)

                for elementw in ascii_art:
                    for elementh in elementw:
                        print(elementh, end="")
                    print()

                if isinstance(image, PIL.GifImagePlugin.GifImageFile):
                    os.system("cls")
                print()


                sleep(50)
   
        else:
            print('Команда не найденна!')


run()
