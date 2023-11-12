# import random

# # create list of fave list
# fave_fruits = ["watermelon", "banana", "kiwi", "guava", "apple"]

# # use random module to pick a fruit
# word_list= fave_fruits
# word = random.choice(word_list)

# # create guess input function
# guess = input("Enter a single letter: ")

# if len(guess) == 1 and guess.isalpha():
#     print("Good Guess!")
# else:
#     print("Ooops! That is not a valid input")

# print(word)

# REFACTOR CODE ABOVE

import random

# list of fave fruits
fave_fruits = ["watermelon", "banana", "kiwi", "guava", "appple"]

def select_a_fruit(fruit_list):
    """Picks a random a fruit"""
    return random.choice(fruit_list)

def validate_one_letter_input(user_input):
    """validation for a single letter input"""
    return len(user_input) == user_input.isalpha()

# main input function 
def main():
    word = select_a_fruit(fave_fruits)

    guess = input("Enter one letter: ")

    if validate_one_letter_input(guess):
        print("Good Guess")
    else:
        print("Oooops! That is not a valid input")
    
    return word
 
 # intialise function
if __name__ == "__main__":
    word_selected = main()
    print("The randomly selectd word is:", word_selected)