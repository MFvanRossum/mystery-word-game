import random

class Game:
    def __init__(self):
        self.player = Player("Player")
        self.selected_word = []
        self.hidden_word = []

    def play_game(self):
        with open("sample-words.txt", "r") as f:
            data = f.read()
            word_list = [word for word in data.split()]
            word = random.choice(word_list)
            word_len = len(word)
            selected_word = list(word)
            print("Welcome to Mystery Word! Guess the correct letters to reveal the hidden word!")
            print(selected_word)
            hidden_word = ["_"] * word_len
            guess_list = []
            print(" " .join(hidden_word))
            print("\n")
            print(f"Your mystery word has {word_len} letters.")
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



            
    



class Player:
    def __init__(self, name):
        self.name = name 
        self.remaining_guesses = 8

    def __str__(self):
        return f"{self.name}"


Game().play_game()
