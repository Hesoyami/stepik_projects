# Hangman
import random
#list of possible words in game
word_list = ['subway', 'vodka', 'voodoo', 'topaz', 'microwave', 'jumbo', 'fishhook', 'crypt', 'puppy', 'rhythm', 'wizard', 'buffalo', 'polka', 'oxygen']

def get_word(): # Function randomly choice word from list
    return random.choice(word_list)

def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()
    
def display_hangman(tries): # Function for hangman display 
    stages = [  # Final stage: head, body, 2 hands, 2 legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, body, 2 hands, 1 leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, body, 2 hands
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, body, hand
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head and body
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # Start stage
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # string with symbols _ for eachone char in word
    guessed = False                    # signal value
    guessed_letters = []               
    guessed_words = []                 
    tries = 6                          # tries number
    print('Let`s play Hangman!')
    print(display_hangman(tries))
    print(word_completion)
    while True:
        word_input = input('Enter a char or word entirely: ').upper()
        if not word_input.isalpha():
            print('Wrong input, try again')
            continue
        if word_input in guessed_letters or word_input in guessed_words:
            print('That char or word has already been suggested')
            continue
        if len(word_input) > 1:
            if word_input == word:
                print('Congratulation! You guessed whole word!')
                break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print(f'Wrong, tries left : {tries}')
                print(display_hangman(tries))
                print_word(word, guessed_letters)
                if tries == 0:
                    print(f'Game over! You couldn`t guess a word : {word}')
                    break
                continue
    
    
    
        if word_input in word:
            guessed_letters.append(word_input)
            for c in word:
                if c not in guessed_letters:
                    print('Good! You guess a letter')
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:    
                print_word(word, guessed_letters)
                print('Congratulation! You guessed whole word!')
                break
        else:
            guessed_letters.append(word_input)
            tries -= 1
            print(f'Wrong, tries left :{tries}')
            print(display_hangman(tries))
            print_word(word, guessed_letters)
        if tries == 0:
            print(f'Game over! You couldn`t guess a word : {word}')
            break     
        
play(get_word().upper()) 