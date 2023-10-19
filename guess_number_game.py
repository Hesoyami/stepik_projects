import random 
def is_valid(n):
    
    if n.isdigit() and 1 <= n <= 100:
        return True
    return False

guess_number = int(input('Enter new number: '))

number = random.randint(1,100)

attempts = 0
while True:
    if is_valid(guess_number) == False:
        print('Maybe try enter a number between 1 and 100?') 
        guess_number = int(input('Enter new number: '))
        continue
    if guess_number == number:
        print(f'That is right guess! Number {guess_number} found in {attempts} attempts')
        final_answer = input('Wanna play again? y - Yes n - NO : ')
        if final_answer.lower() == 'y':
            guess_number = int(input('Enter new number: '))
            right_border = int(input('Enter right border for random generator: '))
            number = random.randint(1,right_border)
            continue
        else:
            break
    if guess_number < number:
        print('Your number too small, try again')
        guess_number = int(input('Enter new number: '))
        left = middle + 1
        attempts += 1
    if guess_number > number:
        print('Your number too big, try again')
        guess_number = int(input('Enter new number: '))
        attempts += 1
print('Thanks for playing, see you later..')