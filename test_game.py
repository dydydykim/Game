from game import Game
import pytest

def test_game():
     game = Game()
     with pytest.raises(TypeError):
         game.guess(None)