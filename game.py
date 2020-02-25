import random

class Game:
    def __init__(self):
        self.player = Player("Player")
        self.selected_word = []
        self.hidden_word = []

    def play_game(self):
        with open("words.txt", "r") as f:
            data = f.read()
            print("Welcome to Mystery Word! Guess the correct letters to reveal the hidden word!""\n")
            print("There are 3 difficulties:""\n""(E)asy provides a word between 4-6 letters.""\n""(M)edium provides words between 7-8 letters.""\n""(H)ard provides words with 8 or more letters!""\n")
            diff = input("Choose a difficulty! ")
            diff = diff.lower()
            if diff == "e" or diff == "easy":
                word_list = [word for word in data.split() if len(word) > 3 and len(word) < 7]
                self.player.remaining_guesses = 10
                self.player.hint = 1
            elif diff == "m" or diff == "medium":
                word_list = [word for word in data.split() if len(word) > 6 and len(word) < 9]
                self.player.remaining_guesses = 8
                self.player.hint = 2
            elif diff == "h" or diff == "hard":
                word_list = [word for word in data.split() if len(word) > 8]
                self.player.remaining_guesses = 6
                self.player.hint = 3
            else: 
                print("Please select a valid difficulty.")
                Game().play_game()
            word = random.choice(word_list).lower()
            word_len = len(word)
            selected_word = list(word)
            hidden_word = ["_"] * word_len
            guess_list = []
            print(" " .join(hidden_word))
            print("\n")
            print(f"Your mystery word has {word_len} letters.")
            if self.player.hint != 0:
                print(f"Enter 'hint' if you need help! You have {self.player.hint} hints remaining.")
            while "_" in hidden_word:
                playing = True
                while playing:
                    guess = input("Guess a letter: ")
                    guess = guess.lower()
                    if guess.isalpha() and len(guess) == 1:
                        if guess in guess_list:
                            print("You have already guessed this letter! Try again!""\n")
                        elif guess in selected_word:
                            index_pos_list = self.get_index_pos(selected_word, guess)
                            choice_list = len(index_pos_list) * [guess,]
                            for (index, guess) in zip(index_pos_list, choice_list):
                                hidden_word[index] = guess
                            print(" ".join(hidden_word))
                            print("You got it!""\n")
                            guess_list.append(guess)
                        else:
                            self.player.remaining_guesses -= 1
                            print(f"Nope! The mystery word doesn't contain that letter! You have {self.player.remaining_guesses} incorrect guesses remaining!""\n")
                            guess_list.append(guess)
                    elif guess == "hint":
                        print(word)
                        if self.player.hint != 0:
                            self.show_hint(selected_word, guess_list)
                        else:
                            print("You are out of hints!""\n")
                    else:
                        print("Guesses must consist of single letters ONLY! Try again!""\n")
                    if self.player.remaining_guesses == 0:
                        self.game_over(word)
                    break
            playing = False
            self.you_win(word)



    def game_over(self, word):
        print(f"Sorry! You're out of guesses! The mystery word was '{word}'! Would you like to play again?""\n")
        play_again = input("Press R to play again! Press any other key to exit! ")
        play_again = play_again.lower()
        if play_again == "r":
            Game().play_game()
        else:
            print("\n""See you next time!")
            exit()

    def you_win(self, word):
        print(f"Hot damn! You guessed the mystery word: {word}! Congratulations, you big brain genius! Would you like to play again?""\n")
        play_again = input("Press R to play again! Press any other key to exit! ")
        play_again = play_again.lower()
        if play_again == "r":
            Game().play_game()
        else:
            print("\n""See you next time!")
            exit()

    def  get_index_pos(self, selected_word, guess):
        index_pos_list = []
        index_pos = 0
        while True:
            try:
                index_pos = selected_word.index(guess, index_pos)  
                index_pos_list.append(index_pos)
                index_pos += 1
            except:
                break
        return index_pos_list   

    def show_hint(self, selected_word, guess_list):
        hint = random.choice(selected_word)
        if hint not in guess_list:
            print(f"The mystery word containts the letter: {hint}""\n")
            self.player.hint -= 1
            print(f"You have {self.player.hint} hints remaining.""\n")
        else:
            self.show_hint(selected_word, guess_list)                 



            
    



class Player:
    def __init__(self, name):
        self.name = name 
        self.remaining_guesses = None
        self.hint = None

    def __str__(self):
        return f"{self.name}"


Game().play_game()
