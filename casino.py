from random import randint


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
