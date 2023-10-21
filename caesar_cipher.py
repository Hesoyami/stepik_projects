def is_valid_input(input_value):
    
    if input_value.isalnum():
        return input_value
    else:
        print('Wrong input value')
        return False
        

# strings with all possible chars for cipher

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
  
cipher_language = input(f'Choose language for cipher. || Russian - ru || or || English - en || : ').lower()
cipher_language = is_valid_input(cipher_language)
cipher_step = int(input(f'Enter step for cipher. For decrypt [num < 0] for encrypt [num > 0]: '))
text = input(f'Enter text for cipher : ')


def caesar_cipher(text):
        
        if cipher_language == 'en':
            alphabet_lower = list(eng_lower_alphabet)
            alphabet_upper = list(eng_upper_alphabet)
            alphabet_power = 26
        else:
            alphabet_lower = list(rus_lower_alphabet)
            alphabet_upper = list(rus_upper_alphabet)
            alphabet_power = 32
        for char in text:
            if char.isalpha():
                if char.isupper():
                    print(alphabet_upper[(alphabet_upper.index(char) + cipher_step) % alphabet_power], end='')
                else:
                    print(alphabet_lower[(alphabet_lower.index(char) + cipher_step) % alphabet_power], end='')
            else:
                print(char, end='')

caesar_cipher(text)