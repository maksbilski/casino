from random import randint
from collections import Counter


class Casino:
    def __init__(self, player_list):
        '''
        Constructor method.
        '''
        self._player_list = player_list

    def roll_dice(self):
        '''
        '''
        return randint(1, 6)

    def roll_dice_four_times(self):
        dice_rolls = []
        for times in range(0, 4):
            dice_rolls.append(self.roll_dice())
        return dice_rolls

    def play(self):
        for player in self._player_list:
            player.set_dice_layout(self.roll_dice_four_times())
            player.set_score(player.calculate_score())

    def indicate_winner(self):
        return max(self._player_list, key=lambda player: player.score())


class Player:
    def __init__(self, name):
        '''
        Constructor method
        '''
        self._name = name
        self._dice_layout = None
        self._score = 0

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    def set_dice_layout(self, new_dice_layout):
        self._dice_layout = new_dice_layout

    def set_score(self, new_score):
        self._score = new_score

    def score_if_numbers_are_even(self):
        for number in self._dice_layout:
            if number % 2 != 0:
                return 0
        return sum(self._dice_layout) + 2

    def score_if_numbers_are_odd(self):
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
        possible_score_values = self.scores_based_on_duplicates()
        possible_score_values.append(self.score_if_numbers_are_odd())
        possible_score_values.append(self.score_if_numbers_are_even())
        return max(possible_score_values)
