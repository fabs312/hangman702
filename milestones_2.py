import random

# create list of fave list
fave_fruits = ["watermelon", "banana", "kiwi", "guava", "apple"]
# use random module to pick a fruit
word = random.choice(fave_fruits)

guess = input("Enter a single letter: ")
print(word)

