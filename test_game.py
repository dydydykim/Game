from game import Game
import pytest


@pytest.fixture
def game():
    return Game()


def assert_type_error(game, guess_number):
    with pytest.raises(TypeError):
        game.guess(guess_number)

@pytest.mark.parametrize("invalid_input", [None, "12", "1234", "123s", "121"])
def test_exception_when_input_type_is_wrong(game, invalid_input):
    assert_type_error(game, invalid_input)