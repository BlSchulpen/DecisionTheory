from unittest import TestCase, main
from src import  util
from copy import deepcopy
from src.BoxState import BoxState
from src.Players import Players

class Test_FourInARowState(TestCase):
  def test_player_from_boxstate(self):
    # arrange
    expected_player = BoxState.RED

    # act
    actual_box_state = util.box_state_from_player(Players.RED)
    
    # assert
    self.assertEqual(actual_box_state, expected_player)


        

    # def box_state_from_player(player: Players) -> BoxState:
    # match player:
    #     case Players.RED   : return BoxState.RED
    #     case Players.YELLOW: return BoxState.YELLOW

    # def get_other_player(player: Players) -> Players:
    # match player:
    #     case Players.RED   : return Players.YELLOW
    #     case Players.YELLOW: return Players.RED
