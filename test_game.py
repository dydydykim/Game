from game import Game
import pytest

@pytest.fixture
def game():
    return Game()

def assert_type_error(game, guessNumber):
    try:
        game.guess(guessNumber)
        pytest.fail()
    except TypeError:
        pass

def test_exception_when_input_type_is_wrong(game):
    assert_type_error(game, None)
    assert_type_error(game, "12")
    assert_type_error(game, "1234")
    assert_type_error(game, "123s")

