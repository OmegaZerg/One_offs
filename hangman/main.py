print('######___Hang Man___######')
print('||||||||||||||||||||||||||')
#Define hangmans
def hang_man1():
    print('#########')
    print('##      |')
    print('##')
    print('##')
    print('##')
    print('##')
    print('##')
def hang_man2():
    print('#########')
    print('##      |')
    print('##      O')
    print('##')
    print('##')
    print('##')
    print('##')
def hang_man3():
    print('#########')
    print('##      |')
    print('##      O')
    print('##      |')
    print('##')
    print('##')
    print('##')
def hang_man4():
    print('#########')
    print('##      |')
    print('##      O')
    print('##      |\\')
    print('##')
    print('##')
    print('##')
def hang_man5():
    print('#########')
    print('##      |')
    print('##      O')
    print('##     /|\\')
    print('##')
    print('##')
    print('##')
def hang_man6():
    print('#########')
    print('##      |')
    print('##      O')
    print('##     /|\\')
    print('##       \\')
    print('##')
    print('##')
def hang_man7():
    print('#########')
    print('##      |')
    print('##      O')
    print('##     /|\\')
    print('##     / \\')
    print('##')
    print('##')
def player_guess():
    print("Guess a letter for the word:")
    guess = input()
    return guess

#Define hard-coded list of words, variables required, and import required libraries
word_list = ["Skyscraper", "Apartment", "Neighborhood", "Playground", "Aquarium"]
import random
pick_word = random.choice(word_list)
blank_word = ""
test_blank = []
guess_count = 0
guess = ""

#Begin Game
hang_man1()
for char in pick_word:
    blank_word += "_ "
    test_blank.append("_ ")
print(f"The random word is: {pick_word}")
print(f"The blank word is: {blank_word}")
print(f"The blank test is: {test_blank}")
hang_man7()