import random

# list of fave fruits
fave_fruits = ["watermelon", "banana", "kiwi", "guava", "appple"]

def select_a_fruit(fruit_list):
    """Picks a random a fruit"""
    return random.choice(fruit_list)

def validate_one_letter_input(user_input):
    """validation for a single letter input"""
    return len(user_input) == 1 and user_input.isalpha()

def check_guess(guess, word):
    """Checks a letter in the guessed word"""
    guess = guess.lower() # convert guess to lower case
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again")
        return False

def ask_for_input():
    """Asks for invalid input and validates"""
    word = select_a_fruit(fave_fruits)
    
    # while loop block
    while True:
        guess = input("Enter one letter: ")
    
        if validate_one_letter_input(guess):
            if check_guess(guess, word):
                break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
 
 # intialise game
if __name__ == "__main__":
    ask_for_input()