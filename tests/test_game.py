import pytest
from game.main import get_winner, main
from unittest.mock import patch


def test_get_winner():
    assert get_winner("Rock", "Rock") is None
    assert get_winner("Rock", "Paper") == "Paper"
    assert get_winner("Paper", "Rock") == "Paper"


def test_get_winner_exception():
    with pytest.raises(KeyError):
        get_winner("Rock", "Rock")


def test_rules():
    assert get_winner("Rock", "Scissor") == "Rock"
    assert get_winner("Rock", "Paper") == "Paper"
    assert get_winner("Paper", "Scissor") == "Scissor"


def test_main_function():
    with patch('builtins.input', side_effect=["Rock", "Paper"]):
        output = main()
    assert output == 'Paper wins!'
