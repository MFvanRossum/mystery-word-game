import random

class Game:
    def __init__(self):
        self.player = Player("Player")
        self.list = open("sample-words.txt", "r")
        words = self.list.read()
        print(words)



class Player:
    def __init__(self, name):
        self.name = name 
        self.remaining_guesses = 8

    def __str__(self):
        return f"{self.name}"


Game()