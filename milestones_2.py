import random

# create list of fave list
fave_fruits = ["watermelon", "banana", "kiwi", "guava", "apple"]

# use random module to pick a fruit
word_list= fave_fruits
word = random.choice(word_list)

# create guess input function
guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good Guess!")
else:
    print("Ooops! That is not a valid input")

print(word)


