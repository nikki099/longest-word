"""Game module for the Longest Word game.

This module contains the Game class that implements the core functionality
of the Longest Word game, including grid generation and word validation.
"""

import random
import string

# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]  # 9 random letters


    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
