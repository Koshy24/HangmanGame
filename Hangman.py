
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
import random



print("Welcome to Hangman \nBegin by choosing a category")
print(HANGMANPICS[0])
category = input("Games, Movies, or Country names: ")


games = ['fortnite', 'overwatch', 'grand theft auto', 'elden ring', 'apex legends', 'call of duty', 'hitman',
         'spiderman', 'armoured core', 'battlefield', 'minecraft']
movies = ['shawshank', 'matrix', 'grown ups', 'murder mystery', 'lawrence of arabia', 'pirates of caribbean',
          'inside out', 'toy story']
country = ['canada', 'united states of america', 'india','england', 'switzerland', 'germany', 'italy', 'spain',
           'france', 'russia']


if category == 'movies':
    y = 0
    print(HANGMANPICS[y])
    chosen_word = (random.choice(movies))
    spaces = '_'*len(chosen_word)
    print(spaces)
    blank_list = list(spaces)

    ltr_wrd = input("do you want to guess a letter or word? (ENTER LETTER OR WORD): ")
    if ltr_wrd == 'letter':
        chosen_word = list(chosen_word)
        while y < 6:
            print(HANGMANPICS[y])
            guess = input("enter letter (P.S: Press SPACE to separate words): ")
            x = 0
            correct_guess = False
            for letter in chosen_word:
                if guess.lower() == chosen_word[x]:
                    blank_list[x] = guess.lower()
                    correct_guess = True
                x += 1
            if correct_guess == False:
                print("Wrong guess")
                y += 1

            blank = "".join(blank_list)
            print(blank)
            if blank_list == chosen_word:
                print("CORRECT!")
                break
            if y == 6:
                print(f"GAME OVER! The correct answer is {''.join(chosen_word)}")


    if ltr_wrd == "word":
        while y < 6:
            guess = input("Guess a word: ")
            y += 1
            print(HANGMANPICS[y])
            if guess.lower() == chosen_word:
                print('CORRECT!')
                break
            else:
                print('try again :(')
                print(spaces)
            if y == 3:
                print(f"The word starts with the letter {chosen_word[0]}")
            if y == 5:
                print(f"The final letter of the word is {chosen_word[-1]}")
            if y == 6:
                print(f"Whoops, ran out of tries! The answer was {chosen_word}")

if category == 'country':
    y = 0
    print(HANGMANPICS[y])
    chosen_word = random.choice(country)
    spaces = '_' * len(chosen_word)
    print(spaces)
    blank_list = list(spaces)

    ltr_wrd = input("do you want to guess a letter or a word? (ENTER LETTER OR WORD): ")
    if ltr_wrd == 'letter':
        chosen_word = list(chosen_word)
        while y < 6:
            print(HANGMANPICS[y])
            guess = input("enter letter (P.S: Press SPACE to separate words): ")
            x = 0
            correct_guess = False
            for letter in chosen_word:
                if guess.lower() == chosen_word[x]:
                    blank_list[x] = guess.lower()
                    correct_guess = True
                x += 1
            if correct_guess == False:
                print("Wrong guess")
                y += 1

            blank = "".join(blank_list)
            print(blank)
            if blank_list == chosen_word:
                print("CORRECT!")
                break
            if y == 6:
                print(f"GAME OVER! The correct answer is {''.join(chosen_word)}")

    if ltr_wrd == "word":
        while y < 6:
            guess = input("Guess a word: ")
            y += 1
            print(HANGMANPICS[y])
            if guess.lower() == chosen_word:
                print('CORRECT!')
                break
            else:
                print('try again :(')
                print(spaces)
            if y == 3:
                print(f"The word starts with the letter {chosen_word[0]}")
            if y == 5:
                print(f"The final letter of the word is {chosen_word[-1]}")
            if y == 6:
                print(f"Whoops, ran out of tries! The answer was {chosen_word}")





if category == 'games':
    y = 0
    print(HANGMANPICS[y])
    chosen_word = random.choice(games)
    spaces = '_' * len(chosen_word)
    print(spaces)
    blank_list = list(spaces)

    ltr_wrd = input("do you want to guess a letter or a word? (ENTER WORD OR LETTER): ")
    if ltr_wrd == 'letter':
        chosen_word = list(chosen_word)
        while y < 6:
            print(HANGMANPICS[y])
            guess = input("enter letter (P.S: Press SPACE to separate words): ")
            x = 0
            correct_guess = False
            for letter in chosen_word:
                if guess.lower() == chosen_word[x]:
                    blank_list[x] = guess.lower()
                    correct_guess = True
                x += 1
            if correct_guess == False:
                print("Wrong guess")
                y += 1

            blank = "".join(blank_list)
            print(blank)
            if blank_list == chosen_word:
                print("CORRECT!")
                break
            if y == 6:
                print(f"GAME OVER! The correct answer is {''.join(chosen_word)}")

    if ltr_wrd == "word":
        while y < 6:
            guess = input("Guess a word: ")
            y += 1
            print(HANGMANPICS[y])
            if guess.lower() == chosen_word:
                print('CORRECT!')
                break
            else:
                print('try again :(')
                print(spaces)
            if y == 3:
                print(f"The word starts with the letter {chosen_word[0]}")
            if y == 5:
                print(f"The final letter of the word is {chosen_word[-1]}")
            if y == 6:
                print(f"Whoops, ran out of tries! The answer was {chosen_word}")







