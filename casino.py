from random import randint
from collections import Counter


class NoPlayersError(Exception):
    def __init__(self):
        super().__init__("You can't create a casino without any players in it")


class Casino:
    '''
    This is  a class representing a casino.

    :raises NoPlayersEror: You can't create a casino without any players in it
    :param player_list: A list containing instances of the Player class
    :type player_list: list
    '''
    def __init__(self, player_list):
        '''
        Constructor method.
        '''
        if not player_list:
            raise NoPlayersError
        self._player_list = player_list

    def roll_dice(self):
        '''
        Method for returning a random number.
        It represents a dice roll in the casino.

        :return: Number representing number of dots on a dice
        :rtype: int
        '''
        return randint(1, 6)

    def roll_dice_four_times(self):
        '''
        Method that repeats the roll_dice method four times

        :return: A list containing four dice roll values
        :rtype: list
        '''
        dice_rolls = []
        for _ in range(0, 4):
            dice_rolls.append(self.roll_dice())
        return dice_rolls

    def play(self):
        '''
        This method is supposed to initiate a dice game between the players.
        It sets each players _dice_layout and _score attribute accordingly
        to the output of roll_dice_four_times method.
        '''
        for player in self._player_list:
            player.set_dice_layout(self.roll_dice_four_times())
            player.set_score(player.calculate_score())

    def indicate_winner(self):
        '''
        Method for indicating the winner.

        :return: player with the biggest score
        :rtype: :class: Player
        '''
        # This next 4 lines are handling a situation when
        # 2 or more players have the same score and their scores
        # are the highest out of all players.
        score_list = [player.score for player in self._player_list]
        highest_score = max(score_list)
        if Counter(score_list)[highest_score] > 1:
            return None
        return max(self._player_list, key=lambda player: player.score)


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
        '''
        Getter for the _name attribute

        :return: name of the player
        :rtype: string
        '''
        return self._name

    @property
    def score(self):
        '''
        Getter for the _score attribute

        :return: score of the player
        :rtype: int
        '''
        return self._score

    def set_dice_layout(self, new_dice_layout):
        '''
        Setter for the _dice_layout attribute
        '''
        self._dice_layout = new_dice_layout

    def set_score(self, new_score):
        '''
        Setter for the _dice_layout attribute
        '''
        self._score = new_score

    def score_if_numbers_are_even(self):
        '''
        Method for checking if all numbers in the dice layout
        are even and calculating according score if they all are even.

        :return: according score
        :rtype: int
        '''
        for number in self._dice_layout:
            if number % 2 != 0:
                return 0
        return sum(self._dice_layout) + 2

    def score_if_numbers_are_odd(self):
        '''
        Method for checking if all numbers in the dice layout
        are odd and calculating according score if they all are odd.

        :return: according score
        :rtype: int
        '''
        for number in self._dice_layout:
            if number % 2 == 0:
                return 0
        return sum(self._dice_layout) + 3

    def scores_based_on_duplicates(self):
        '''
        Method for calculating according values for situations,
        when a certain value appears 2, 3 or 4 times in a dice_layout

        :return: A list of score values that are resembling
            the patterns that occur in the dice layout
        :rtype: list
        '''
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
        '''
        A method that uses scores_based_on_duplicates(),
        score_if_numbers_are_odd(), score_if_numbers_are_even() methods
        to generate all posible score outcomes and selects the highest one.

        :return: Highest possible score value
        :rtyep: int
        '''
        possible_score_values = self.scores_based_on_duplicates()
        possible_score_values.append(self.score_if_numbers_are_odd())
        possible_score_values.append(self.score_if_numbers_are_even())
        return max(possible_score_values)
