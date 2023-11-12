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
    
    # while loop block
    while True:
        guess = input("Enter one letter: ")
    
        if validate_one_letter_input(guess):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    return word
 
 # intialise function
if __name__ == "__main__":
    word_selected = main()
    print("The randomly selectd word is:", word_selected)