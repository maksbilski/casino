from casino import PlayerAlreadyAddedError, PlayerNotInCasinoError
from casino import Casino, Player # NOQA
from pytest import MonkeyPatch, raises # NOQA


def test_player_create():
    player1 = Player('Mark')
    assert player1.name == 'Mark'


def test_player_set_score():
    player1 = Player('Mark')
    player1.set_score(20)
    assert player1._score == 20


def test_player_set_dice_layout():
    player1 = Player('Mark')
    player1.set_dice_layout([2, 4, 6, 4])
    assert player1._dice_layout == [2, 4, 6, 4]


def test_score_if_numbers_are_even1():
    player1 = Player('Mark')
    player1.set_dice_layout([2, 4, 4, 6])
    assert player1.score_if_numbers_are_even() == 18


def test_score_if_numbers_are_even2():
    player1 = Player('Mark')
    player1.set_dice_layout([2, 2, 2, 2])
    assert player1.score_if_numbers_are_even() == 10


def test_score_if_numbers_are_even3():
    player1 = Player('Mark')
    player1.set_dice_layout([4, 2, 6, 6])
    assert player1.score_if_numbers_are_even() == 20


def test_score_if_numbers_are_even4():
    player1 = Player('Mark')
    player1.set_dice_layout([4, 2, 6, 5])
    assert player1.score_if_numbers_are_even() == 0


def test_score_if_numbers_are_odd1():
    player1 = Player('Mark')
    player1.set_dice_layout([3, 5, 1, 3])
    assert player1.score_if_numbers_are_odd() == 15


def test_score_if_numbers_are_odd2():
    player1 = Player('Mark')
    player1.set_dice_layout([5, 5, 5, 5])
    assert player1.score_if_numbers_are_odd() == 23


def test_score_if_numbers_are_odd3():
    player1 = Player('Mark')
    player1.set_dice_layout([1, 1, 5, 5])
    assert player1.score_if_numbers_are_odd() == 15


def test_score_if_numbers_are_odd4():
    player1 = Player('Mark')
    player1.set_dice_layout([1, 2, 5, 5])
    assert player1.score_if_numbers_are_odd() == 0


def test_scores_based_on_numbers_times_of_occurence1():
    player1 = Player('Mark')
    player1.set_dice_layout([2, 2, 5, 5])
    assert player1.scores_based_on_numbers_times_of_occurence() == [4, 10]


def test_scores_based_on_numbers_times_of_occurence2():
    player1 = Player('Mark')
    player1.set_dice_layout([3, 3, 3, 5])
    assert player1.scores_based_on_numbers_times_of_occurence() == [12]


def test_scores_based_on_numbers_times_of_occurence3():
    player1 = Player('Mark')
    player1.set_dice_layout([5, 5, 5, 5])
    assert player1.scores_based_on_numbers_times_of_occurence() == [30]


def test_scores_based_on_numbers_times_of_occurence4():
    player1 = Player('Mark')
    player1.set_dice_layout([1, 1, 1, 1])
    assert player1.scores_based_on_numbers_times_of_occurence() == [6]


def test_calculate_score1():
    player1 = Player('Mark')
    player1.set_dice_layout([1, 1, 1, 1])
    assert player1.calculate_score() == 7


def test_calculate_score2():
    player1 = Player('Mark')
    player1.set_dice_layout([1, 2, 5, 5])
    assert player1.calculate_score() == 10


def test_calculate_score3():
    player1 = Player('Mark')
    player1.set_dice_layout([3, 3, 3, 5])
    assert player1.calculate_score() == 17


def test_calculate_score4():
    player1 = Player('Mark')
    player1.set_dice_layout([5, 5, 5, 5])
    assert player1.calculate_score() == 30


def test_calculate_score_zero_output():
    player1 = Player('Mark')
    player1.set_dice_layout([4, 2, 6, 5])
    assert player1.calculate_score() == 0


def test_casino_create():
    player1 = Player('Mark')
    player2 = Player('Joe')
    player3 = Player('Jacob')
    casino1 = Casino([player1, player2, player3])
    assert casino1._player_list == [player1, player2, player3]


def test_casino_is_draw():
    player1 = Player('Mark')
    player2 = Player('Joe')
    player3 = Player('Mark')
    player4 = Player('Joe')
    player1.set_score(16)
    player2.set_score(20)
    player3.set_score(30)
    player4.set_score(30)
    casino1 = Casino([player1, player2, player3, player4])
    assert casino1.is_draw()


def test_casino_add_player():
    player1 = Player('Mark')
    player2 = Player('Joe')
    player3 = Player('Jacob')
    casino1 = Casino([player1, player2])
    casino1.add_player(player3)
    assert casino1._player_list == [player1, player2, player3]


def test_casino_add_player_error():
    player1 = Player('Mark')
    player2 = Player('Joe')
    player3 = Player('Jacob')
    casino1 = Casino([player1, player2, player3])
    with raises(PlayerAlreadyAddedError):
        casino1.add_player(player3)


def test_casino_remove_player():
    player1 = Player('Mark')
    player2 = Player('Joe')
    player3 = Player('Jacob')
    casino1 = Casino([player1, player2, player3])
    casino1.remove_player(player3)
    assert casino1._player_list == [player1, player2]


def test_casino_remove_player_error():
    player1 = Player('Mark')
    player2 = Player('Joe')
    player3 = Player('Jacob')
    casino1 = Casino([player1, player2])
    with raises(PlayerNotInCasinoError):
        casino1.remove_player(player3)


def test_roll_dice(monkeypatch):
    def return_one():
        return 1
    monkeypatch.setattr(Casino, 'roll_dice', return_one)
    assert Casino.roll_dice() == 1


def test_play1(monkeypatch):
    def return_one(argument):
        return 1
    monkeypatch.setattr(Casino, 'roll_dice', return_one)
    player1 = Player('Mark')
    player2 = Player('Joe')
    players = [player1, player2]
    casino1 = Casino(players)
    casino1.play()
    assert player1._dice_layout == [1, 1, 1, 1]
    assert player2._dice_layout == [1, 1, 1, 1]


def test_play2(monkeypatch):
    def return_list1(argument):
        return [3, 5, 6, 4]
    monkeypatch.setattr(Casino, 'roll_dice_multiple_times', return_list1)
    player1 = Player('Mark')
    player2 = Player('Joe')
    players = [player1, player2]
    casino1 = Casino(players)
    casino1.play()
    assert player1._dice_layout == [3, 5, 6, 4]
    assert player2._dice_layout == [3, 5, 6, 4]


def test_play3(monkeypatch):
    def return_list1(argument):
        return [6, 6, 6, 2]
    monkeypatch.setattr(Casino, 'roll_dice_multiple_times', return_list1)
    player1 = Player('Mark')
    player2 = Player('Joe')
    players = [player1, player2]
    casino1 = Casino(players)
    casino1.play()
    assert player1._dice_layout == [6, 6, 6, 2]
    assert player2._dice_layout == [6, 6, 6, 2]


def test_indicate_winner(monkeypatch):
    def monkey_play(argument):
        casino1._player_list[0]._dice_layout = [3, 5, 1, 5]  # score = 17
        casino1._player_list[1]._dice_layout = [6, 6, 6, 6]  # score = 36
        casino1._player_list[2]._dice_layout = [1, 3, 3, 3]  # score = 13
        casino1._player_list[3]._dice_layout = [4, 4, 4, 4]  # score = 24
    player1 = Player('Mark')
    player2 = Player('Joe')
    player3 = Player('Mark')
    player4 = Player('Joe')
    players = [player1, player2, player3, player4]
    casino1 = Casino(players)
    monkeypatch.setattr(Casino, 'play', monkey_play)
    casino1.play()
    assert casino1.indicate_winner() == player2


def test_indicate_winner_draw(monkeypatch):
    def monkey_play(argument):
        casino1._player_list[0]._dice_layout = [3, 5, 1, 5]  # score = 17
        casino1._player_list[1]._dice_layout = [6, 6, 6, 6]  # score = 36
        casino1._player_list[2]._dice_layout = [1, 3, 3, 3]  # score = 13
        casino1._player_list[3]._dice_layout = [6, 6, 6, 6]  # score = 36
    player1 = Player('Mark')
    player2 = Player('Joe')
    player3 = Player('Mark')
    player4 = Player('Joe')
    players = [player1, player2, player3, player4]
    casino1 = Casino(players)
    monkeypatch.setattr(Casino, 'play', monkey_play)
    casino1.play()
    assert not casino1.indicate_winner()
