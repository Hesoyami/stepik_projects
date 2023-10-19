import random

# Function for check is input value equal y

def check_value(value_to_check):
    
    if value_to_check.lower() == 'y':
        return True
    return False

# Function for input password configuration values 

def input_check_password_config():
    global chars
    password_amount = int(input('Enter how many passwords do you want to generate: '))
    password_lenght = int(input('Enter password lenght: '))
    password_digits = input(f'Do you want add {digits} in password? y - Yes || n - No  : ')
    password_lower_letters = input(f'Do you want add {lower_letters} in password? y - Yes || n - No  : ')
    password_upper_letters = input(f'Do you want add {upper_letters} in password? y - Yes || n - No  : ')
    password_special_symbols = input(f'Do you want add {special_symbols} in password? y - Yes || n - No  : ')
    password_similar_symbols = input('Do you want exept similar symbols like [i,1,l,L,0,o] in password? y - Yes || n - No  : ')
    
    if check_value(password_digits):
        chars += digits
        
    if check_value(password_lower_letters):
        chars += lower_letters
        
    if check_value(password_upper_letters):
        chars += upper_letters
        
    if check_value(password_special_symbols):
        chars += special_symbols
        
    if check_value(password_similar_symbols):
        for char in 'il1Lo0O':
            chars = chars.replace(char,'')
            
    for _ in range(password_amount):
        generate_password(password_lenght, chars)
        
# generation password by random.choice        

def generate_password(password_lenght, chars):
    password = ''
    for _ in range(password_lenght):
        password += random.choice(chars)
    print(f'Genrated password - {password}')
    
# Strings constant for password generation 

digits = "0123456789"
lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_symbols = "!#$%&*+-=?@^"

chars = '' # Variable for possible chars in password

input_check_password_config()
