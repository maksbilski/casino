from casino import Casino, Player # NOQA
from pytest import MonkeyPatch # NOQA



def test_player_create():
    player1 = Player('Mark')
    assert player1.name == 'Mark'


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


def test_scores_based_on_duplicates1():
    player1 = Player('Mark')
    player1.set_dice_layout([2, 2, 5, 5])
    assert player1.scores_based_on_duplicates() == [4, 10]


def test_scores_based_on_duplicates2():
    player1 = Player('Mark')
    player1.set_dice_layout([3, 3, 3, 5])
    assert player1.scores_based_on_duplicates() == [12]


def test_scores_based_on_duplicates3():
    player1 = Player('Mark')
    player1.set_dice_layout([5, 5, 5, 5])
    assert player1.scores_based_on_duplicates() == [30]


def test_scores_based_on_duplicates4():
    player1 = Player('Mark')
    player1.set_dice_layout([1, 1, 1, 1])
    assert player1.scores_based_on_duplicates() == [6]


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


def test_roll_dice(monkeypatch):
    def return_one():
        return 1
    monkeypatch.setattr(Casino, 'roll_dice', return_one)
    assert Casino.roll_dice() == 1


def test_play(monkeypatch):
    def return_one():
        return 1
    monkeypatch.setattr(Casino, 'roll_dice', return_one)
    player1 = Player('Mark')
    player2 = Player('Joe')
    players = [player1, player2]
    casino1 = Casino(players)
    Casino.play()
    assert player1.score