from random import randint
from collections import Counter

NUMBER_OF_ROLLS = 4
SCORE_MULITPLIERS = {
    2: 2,
    3: 4,
    4: 6
}


class PlayerNotInCasinoError(Exception):
    '''
    Exception class representing an error that is raised
    when you want to remove a player that isn't in the casino.
    '''
    def __init__(self):
        super().__init__("You can't remove that player because he is not in the casino.") # NOQA


class PlayerAlreadyAddedError(Exception):
    '''
    Exception class representing an error that is raised
    when you want to add a player to the casino that was already added
    '''
    def __init__(self):
        super().__init__("You can't add this player. He is already in the casino.") # NOQA


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
        self._player_list = player_list

    def add_player(self, new_player):
        '''
        Method for adding players to the casino.
        '''
        if new_player in self._player_list:
            raise PlayerAlreadyAddedError
        self._player_list.append(new_player)

    def remove_player(self, removed_player):
        '''
        Method for removing players from the casino.
        '''
        try:
            self._player_list.remove(removed_player)
        except ValueError:
            raise PlayerNotInCasinoError

    def roll_dice(self):
        '''
        Method for returning a random number.
        It represents a dice roll in the casino.

        :return: Number representing number of dots on a dice
        :rtype: int
        '''
        return randint(1, 6)

    def roll_dice_multiple_times(self):
        '''
        Method that repeats the roll_dice method four times

        :return: A list containing four dice roll values
        :rtype: list
        '''
        dice_rolls = []
        for _ in range(0, NUMBER_OF_ROLLS):
            dice_rolls.append(self.roll_dice())
        return dice_rolls

    def play(self):
        '''
        This method is supposed to initiate a dice game between the players.
        It sets each players _dice_layout and _score attribute accordingly
        to the output of roll_dice_four_times method.
        '''
        for player in self._player_list:
            player.set_dice_layout(self.roll_dice_multiple_times())
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
        # This situation is a draw so there is no winner
        # That's why this method returns None object if this situation occurs
        score_list = [player.score for player in self._player_list]
        highest_score = max(score_list)
        if Counter(score_list)[highest_score] > 1:
            return None
        return max(self._player_list, key=lambda player: player.score)


class Player:
    '''
    This is a class representing a player that plays in the casino

    :param name: Name of the player
    :type name: string
    '''
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
        if all(number % 2 == 0 for number in self._dice_layout):
            return sum(self._dice_layout) + 2
        return 0

    def score_if_numbers_are_odd(self):
        '''
        Method for checking if all numbers in the dice layout
        are odd and calculating according score if they all are odd.

        :return: according score
        :rtype: int
        '''
        if all(number % 2 != 0 for number in self._dice_layout):
            return sum(self._dice_layout) + 3
        return 0

    def scores_based_on_numbers_times_of_occurence(self):
        '''
        Method for calculating according score values for situations,
        when a certain value appears 2, 3 or 4 times in a dice_layout

        :return: A list of score values that are resembling
            the patterns that occur in the dice layout
        :rtype: list
        '''
        dice_number_count = dict(Counter(self._dice_layout))
        score_values = []
        for number, count in dice_number_count.items():
            if count in [2, 3, 4]:
                score_values.append(number * SCORE_MULITPLIERS[count])
        return score_values

    def calculate_score(self):
        '''
        A method that uses scores_based_on_duplicates(),
        score_if_numbers_are_odd(), score_if_numbers_are_even() methods
        to generate all posible score outcomes and selects the highest one.

        :return: Highest possible score value
        :rtype: int
        '''
        possible_score_values = self.scores_based_on_numbers_times_of_occurence() # NOQA
        possible_score_values.append(self.score_if_numbers_are_odd())
        possible_score_values.append(self.score_if_numbers_are_even())
        return max(possible_score_values)
