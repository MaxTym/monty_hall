from monty_hall import *


def test_not_changing_door_chances():
    assert game(1000) in range(250, 400)


def test_changing_door_chances():
    assert game_change_door(1000) in range(550, 700)
