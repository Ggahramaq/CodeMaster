import base64
import os
import PIL
from PIL import Image, ImageSequence
from time import sleep
from colorama import Fore
import time
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

        command = str(input(f'''{Fore.RED}
                     ____           _      __  __           _            
                    / ___| ___   __| | ___|  \/  | __ _ ___| |_ ___ _ ___
                    | |   / _ \ / _` |/ _ \ |\/| |/ _` / __| __/ _ \  __|
                    | |__| (_) | (_| |  __/ |  | | (_| \__ \ ||  __/ |   
                    \____\___/ \__,_|\___|_|  |_|\__,_|___/\__\___||_|   
                            
                                                                {Fore.CYAN}By{Fore.RESET} {Fore.YELLOW}Ggahramaq{Fore.RESET}

            {Fore.GREEN}CodeMaster{Fore.RESET} - многофункциональный инструмент. Пожалуйста выберите что-нибудь ниже (1/3)
            
            [{Fore.MAGENTA}1{Fore.RESET}] - {Fore.YELLOW}Encoder{Fore.RESET}
            [{Fore.MAGENTA}2{Fore.RESET}] - {Fore.YELLOW}Decoder{Fore.RESET}
            [{Fore.MAGENTA}3{Fore.RESET}] - {Fore.YELLOW}Генератор в ASСII{Fore.RESET}

            [{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Выбор: {Fore.RESET} '''))

        if command == '1':
            choice = str(input(f'''

            [{Fore.MAGENTA}>{Fore.RESET}] Выберите тип кода (1/5):
           
            [{Fore.MAGENTA}1{Fore.RESET}] - {Fore.YELLOW}Двоичный код{Fore.RESET}
            [{Fore.MAGENTA}2{Fore.RESET}] - {Fore.YELLOW}Base64{Fore.RESET}
            [{Fore.MAGENTA}3{Fore.RESET}] - {Fore.YELLOW}Rot(rotate){Fore.RESET}
            [{Fore.MAGENTA}4{Fore.RESET}] - {Fore.YELLOW}Азбука морзе{Fore.RESET}
            [{Fore.MAGENTA}5{Fore.RESET}] - {Fore.YELLOW}Unicode{Fore.RESET}

            [{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Выбор: {Fore.RESET}'''))
            
            if choice == '1':
                message = str(input(f'[{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Введите текст: {Fore.RESET}'))
                if not is_english(message):
                    print(f"[{Fore.MAGENTA}!{Fore.RESET}] {Fore.YELLOW}Только на английском!{Fore.RESET}")
                    time.sleep(2)
                else:
                    cypher_message = cypher(message)
                    print(f"[{Fore.YELLOW}RESULT{Fore.RESET}] - {cypher_message}")
                    time.sleep(2)

            elif choice == '2':
                encode_text = input(f'[{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Введите текст: {Fore.RESET}')
                if not is_english(encode_hash):
                    print(f"[{Fore.MAGENTA}!{Fore.RESET}] {Fore.YELLOW}Только на английском!{Fore.RESET}")
                    time.sleep(2)
                    
                else:
                    encode_hash = base64.b64encode(encode_text.encode('UTF-8')).decode('ascii')

                    print(f"[{Fore.YELLOW}RESULT{Fore.RESET}] - {encode_hash}")
                    time.sleep(2)

            elif choice == '3':

                input_text = input(f'[{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Введите текст: {Fore.RESET}')
                if not is_english(input_text):
                    print(f"[{Fore.MAGENTA}!{Fore.RESET}] {Fore.YELLOW}Только на английском!{Fore.RESET}")
                    time.sleep(2)
                else:
                    for shift in range(1, 26):
                        encrypted_text = rotate(input_text, shift)
                        print(f"{Fore.YELLOW}ROT{shift}:{Fore.RESET} {encrypted_text}")
                        time.sleep(2)


            elif choice == '4':
                morse_input = str(input(f'[{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Введите текст: {Fore.RESET}'))
                if not is_english(morse_input):
                    print(f"[{Fore.MAGENTA}!{Fore.RESET}] {Fore.YELLOW}Только на английском!{Fore.RESET}")
                    time.sleep(2)
                else:
                    morse_result = text_to_morse(morse_input)
                    print(f"[{Fore.YELLOW}RESULT{Fore.RESET}] - {morse_result}")
                    time.sleep(2)


            elif choice == '5':
                input_text = str(input(f'[{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Введите текст: {Fore.RESET}'))
                if not is_english(input_text):
                    print(f"[{Fore.MAGENTA}!{Fore.RESET}] {Fore.YELLOW}Только на английском!{Fore.RESET}")
                    time.sleep(2)
                else:
                    unicode_result = text_to_unicode_escape(input_text)
                    print(f"[{Fore.YELLOW}RESULT{Fore.RESET}] - {unicode_result}")
                    time.sleep(2)


            else:
                print(f'[{Fore.MAGENTA}!{Fore.RESET}] {Fore.YELLOW}Команда не найденна!{Fore.RESET}')
                time.sleep(2)

        elif command == '2':
            choice = str(input(f'''

            [{Fore.MAGENTA}>{Fore.RESET}] Выберите тип кода (1/5):
           
            [{Fore.MAGENTA}1{Fore.RESET}] - {Fore.YELLOW}Двоичный код{Fore.RESET}
            [{Fore.MAGENTA}2{Fore.RESET}] - {Fore.YELLOW}Base64{Fore.RESET}
            [{Fore.MAGENTA}3{Fore.RESET}] - {Fore.YELLOW}Rot(rotate){Fore.RESET}
            [{Fore.MAGENTA}4{Fore.RESET}] - {Fore.YELLOW}Азбука морзе{Fore.RESET}
            [{Fore.MAGENTA}5{Fore.RESET}] - {Fore.YELLOW}Unicode{Fore.RESET}

            [{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Выбор: {Fore.RESET}'''))
            if choice == '1':
                message = str(input(f'[{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Введите Двоичный код: {Fore.RESET}'))
                decipher_message = decipher(message)
                print(f'[{Fore.YELLOW}RESULT{Fore.RESET}] - {decipher_message}')
                time.sleep(2)

            elif choice == '2':
                decode_text = input(f'[{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Введите код base64: {Fore.RESET}')
                decode_hash = base64.b64decode(decode_text)
                decodeit = decode_hash.decode('UTF-8')


                print(f'[{Fore.YELLOW}RESULT{Fore.RESET}] - {decodeit}')
                time.sleep(2)

            elif choice == '3':
                rot_number = int(input(f'[{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Введите номер ROT (1-25): {Fore.RESET}'))
                if 1 <= rot_number <= 25:
                    rot_text = input(f"Введите ROT код: {rot_number}: ")
                    decoded_text = decode_rot(rot_text, rot_number)
                    print(f"[{Fore.YELLOW}RESULT{Fore.RESET}] - ", decoded_text)
                    time.sleep(2)
                else:
                    print(f"[{Fore.YELLOW}!{Fore.RESET}] Номер ROT должен быть от 1 до 25.")
                    time.sleep(2)

            elif choice == '4':
                input_text = str(input(f'[{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Введите текст из азбуки морзе: {Fore.RESET}'))
                decoded_text = morse_to_text(input_text)
                print(f"[{Fore.YELLOW}RESULT{Fore.RESET}] - ", decoded_text)
                time.sleep(2)

            elif choice == '5':
                unicode_input = str(input(f'[{Fore.MAGENTA}>{Fore.RESET}] {Fore.GREEN}Введите unicode текст: {Fore.RESET}'))
                decoded_text = unicode_escape_to_text(unicode_input)
                print(f"[{Fore.YELLOW}RESULT{Fore.RESET}] - ", decoded_text)
                time.sleep(2)

            else:
                print(f"[{Fore.MAGENTA}!{Fore.RESET}] {Fore.YELLOW}Команда не найденна!{Fore.RESET}")
                time.sleep(2)
            
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
            print(f'[{Fore.MAGENTA}!{Fore.RESET}] {Fore.YELLOW}Команда не найденна!{Fore.RESET}')
            time.sleep(2)


run()
