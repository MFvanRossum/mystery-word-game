import random

class Game:
    def __init__(self):
        self.player = Player("Player")
        self.selected_word = []
        self.hidden_word = []

    def choose_word(self):
        with open("sample-words.txt", "r") as f:
            data = f.read()
            word_list = [word for word in data.split()]
            word = random.choice(word_list)
            word_len = len(word)
            selected_word = list(word)
            print(selected_word)
            hidden_word = ["_"] * word_len
            print(" " .join(hidden_word))

    def play_game(self):
        Game().choose_word()
    



class Player:
    def __init__(self, name):
        self.name = name 
        self.remaining_guesses = 8

    def __str__(self):
        return f"{self.name}"


Game().play_game()
