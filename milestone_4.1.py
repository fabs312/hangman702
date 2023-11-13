import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        print(f"The mystery word has {self.num_letters} characters")
        print(self.word_guessed)

def check_guess(self, guess):
    letter = letter.lower()
    if guess in self.word:
        print(f"Good guess! {guess} is in the word.")
        for i in range(len(self.word)):
            if self.word[i] == guess:
                self.word_guessed[i] = guess
        self.num_letters -= 1
    else:
        self.num_lives -= 1
        print(f"Sorry, {letter} is not in the word. Try again")
    
def ask_for_input(self):
    while True:
        guess = input("Enter one letter: ").lower()
        if len(guess) !=1:
            print("Invalid letter. Please, enter one single letter.")
        elif guess in self.list_of_letters:
            print("You already tried that letter!")
        else:
            self.list_letters.append(guess)
            self.check_guess(guess)
            break
 
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_for_input()
    if game.num_letters == 0:
        print("You won")
    else:
        print(f"You lost. The word was {game.word}")

 # intialise game
if __name__ == "__main__":
    word_list = ["watermelon", "banana", "kiwi", "guava", "appple"]
    play_game(word_list)