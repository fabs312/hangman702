import random

# Class and attributes
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list # parameter 
        self.num_lives = num_lives # paramater
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.list_letters = []
        print(f'The mystery word has {len(self.word)} characters')
        self.game_over = False

# Methods
    def check_letter(self, letter):
        letter = letter.lower()
        if letter in self.word:
            print(f'You guessed correctly!')
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter + ' '
        else:
            self.num_lives -= 1
    
    def ask_letter(self):
        while True:
            letter = input('type quit or guess a letter: ').lower()
            if letter == 'quit':
                self.game_over = True
                break
            elif len(letter) != 1:
                print('Please, enter just one character.')
            elif letter in self.list_letters:
                print(f'{letter} was already tried. Try again.')
            else:
                self.list_letters.append(letter)
                self.check_letter(letter)
                break

# Play game function
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)

    while not game.game_over:
        hidden_word = ''.join(game.word_guessed)
        print('Yout guessed letters: {}'.format(game.list_letters))
        print('Word to guess: {}'.format(hidden_word))
        print('Lives: {}'.format(game.num_lives))
        game.ask_letter()

        if game.num_lives <= 0:
            print(f'You lost! The word was: {game.word}')
            game.game_over = True
        elif ''.join(game.word_guessed).replace(" ", "") == game.word.replace(" ", ""):
            print(f'Congratulations, you guessed it correctly! The word was {game.word}')
            game.game_over = True

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)


