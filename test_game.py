import pytest
from game import Game

from game_result import GameResult


@pytest.fixture
def game():
    return Game()


def assert_type_error(game, guess_number):
    with pytest.raises(TypeError):
        game.guess(guess_number)


@pytest.mark.parametrize("invalid_input", [None, "12", "1234", "123s", "121"])
def test_exception_when_input_type_is_wrong(game, invalid_input):
    assert_type_error(game, invalid_input)


def test_return_solved_result_if_matched_number(game):
    game.question = "123"
    assert_matched_number(game.guess("123"), solved = True, strikes = 3, balls = 0)


def assert_matched_number(result, solved, strikes, balls):
    assert result is not None
    assert result.solved == solved
    assert result.strikes == strikes
    assert result.balls == balls


def test_return_solved_result_if_unmatched_number(game):
    game.question = "123"
    assert_matched_number(game.guess("456"), solved = False, strikes = 0, balls = 0)
