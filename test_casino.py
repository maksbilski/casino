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
    def return_one(argument):
        return 1
    monkeypatch.setattr(Casino, 'roll_dice', return_one)
    player1 = Player('Mark')
    player2 = Player('Joe')
    players = [player1, player2]
    casino1 = Casino(players)
    casino1.play()
    assert player1.score == 7
    assert player2.score == 7


def test_play1(monkeypatch):
    def return_one(argument):
        return 1
    monkeypatch.setattr(Casino, 'roll_dice', return_one)
    player1 = Player('Mark')
    player2 = Player('Joe')
    players = [player1, player2]
    casino1 = Casino(players)
    casino1.play()
    assert player1.score == 7
    assert player2.score == 7


def test_play2(monkeypatch):
    def return_list1(argument):
        return [3, 5, 6, 7]
    monkeypatch.setattr(Casino, 'roll_dice_four_times', return_list1)
    player1 = Player('Mark')
    player2 = Player('Joe')
    players = [player1, player2]
    casino1 = Casino(players)
    casino1.play()
    assert player1.score == 0
    assert player2.score == 0


def test_indicate_winner():
    player1 = Player('Mark')
    player2 = Player('Joe')
    player3 = Player('Mark')
    player4 = Player('Joe')
    player1.set_score(4)
    player2.set_score(42)
    player3.set_score(43)
    player4.set_score(54)
    players = [player1, player2, player3, player4]
    casino1 = Casino(players)
    assert casino1.indicate_winner() == player4


def test_indicate_winner_draw():
    player1 = Player('Mark')
    player2 = Player('Joe')
    player3 = Player('Mark')
    player4 = Player('Joe')
    player1.set_score(4)
    player2.set_score(42)
    player3.set_score(54)
    player4.set_score(54)
    players = [player1, player2, player3, player4]
    casino1 = Casino(players)
    assert not casino1.indicate_winner()
