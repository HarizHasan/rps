#!/usr/bin/env python3

# Imports the random class
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Creates a player that can perform random moves.
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Creates a human-controller player that takes input
# and validates correct responses.
class HumanPlayer(Player):
    def move(self):
        while True:
            playermove = input("Will you throw rock, "
                               "paper, or scissors?\n").lower()
            if playermove in moves:
                return playermove
            else:
                print("Sorry, I don't understand.")


# Creates a player that repeats the last move that the opponent did
class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


# Creates a player that starts with a random move,
# then cycles through the order rock, paper, scissors
class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move

    # Checks if no moves have been made yet, then either does a random move,
    # or progresses down the moves list and performs the next move
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            index = moves.index(self.my_move) + 1
            if index > 2:
                index = 0
            self.my_move = moves[index]
            return self.my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # Adding score variables.
        self.p1score = 0
        self.p2score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        # Checks against the beats function to see who wins,
        # increments the score of the player who wins, then prints that score.
        if beats(move1, move2) is True:
            self.p1score += 1
            print("Player 1 wins!")
        elif beats(move2, move1) is True:
            self.p2score += 1
            print("Player 2 wins!")
        else:
            print("Tie!")
        print(f"Score: {self.p1score}-{self.p2score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start! First to 3 wins!")
        round = 0
        # Plays until either player reaches 3 wins
        while self.p1score < 3 and self.p2score < 3:
            round += 1
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        # Announces who wins based on who's score reached 3
        if self.p1score == 3:
            print("Player 1 wins!")
        elif self.p2score == 3:
            print("Player 2 wins!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
