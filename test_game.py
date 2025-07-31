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
    result: GameResult = game.guess("123")

    assert result is not None
    assert result.solved == True
    assert result.strikes == 3
    assert result.balls == 0


def test_return_solved_result_if_unmatched_number(game):
    game.question = "123"
    result: GameResult = game.guess("456")

    assert result is not None
    assert result.solved == False
    assert result.strikes == 0
    assert result.balls == 0
