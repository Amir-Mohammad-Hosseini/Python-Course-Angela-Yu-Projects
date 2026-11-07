import random
word_list = ["ardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

random_word = random.choice(word_list)
print("Random word", random_word)

blanks_list = []

for index in range(len(random_word)):
    blanks_list.append("_")

print("Blanks list", blanks_list)

remaining_guesses = len(blanks_list)
lives = len(stages) - 1

while lives > 0 and "_" in blanks_list:
    guess_letter = input("Guess a letter: ").lower()
    index = 0
    guessed_true = False
    for char in random_word:
        if (char == guess_letter):
            blanks_list[index] = guess_letter
            guessed_true = True
        index += 1
    if not guessed_true :
        lives -=1
        print(stages[lives])
    print(blanks_list)

is_still_blank = True
if "_" in blanks_list :
    is_still_blank = False
    print("You lose.")
else:
    print("You won.")