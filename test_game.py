from game import Game
import pytest

@pytest.fixture
def game():
    return Game()

def test_exception_when_input_in_none(game):
     with pytest.raises(TypeError):
         game.guess(None)