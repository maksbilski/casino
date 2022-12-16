from random import randint
from collections import Counter


class Casino:
    def __init__(self, player_list):
        '''
        Constructor method.
        '''
        self._player_list = player_list

    def roll_dice(self):
        return randint(1, 6)


class Player:
    def __init__(self, name):
        '''
        Constructor method
        '''
        self._name = name
        self._dice_layout = None
        self._score = None

    @property
    def name(self):
        return self._name

    def score_if_numbers_are_odd(self):
        for number in self._dice_layout:
            if number % 2 != 0:
                return 0
        return sum(self._dice_layout) + 2

    def score_if_numbers_are_even(self):
        for number in self._dice_layout:
            if number % 2 == 0:
                return 0
        return sum(self._dice_layout) + 3

    def scores_based_on_duplicates(self):
        dice_number_count = dict(Counter(self._dice_layout))
        score_values = []
        for number, count in dice_number_count.items():
            if count == 4:
                score_values.append(number * 6)
            if count == 3:
                score_values.append(number * 4)
            if count == 2:
                score_values.append(number * 2)
        return score_values

    def calculate_score(self):
        possible_score_values = []
        possible_score_values.append(self.scores_based_on_duplicates)
        possible_score_values.append(self.score_if_number_are_odd)
        possible_score_values.append(self.score_if_numbers_are_even)
        return max(possible_score_values)
