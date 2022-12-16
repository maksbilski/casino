from casino import Casino # NOQA
from pytest import MonkeyPatch # NOQA


def test_roll_dice(monkeypatch):
    def return_one():
        return 1
    monkeypatch.setattr(Casino, 'roll_dice', return_one)
    assert Casino.roll_dice() == 1
