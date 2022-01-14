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



  def test_box_from_player_state(self):
    # arrange
    expected_player = Players.YELLOW

    # act
    actual_box_state = util.player_from_box_state(BoxState.YELLOW)
    
    # assert
    self.assertEqual(actual_box_state, expected_player)



  def test_get_other_player(self):
    # arrange
    expected_player = Players.YELLOW

    # act
    actual_player = util.get_other_player(Players.RED)
    
    # assert
    self.assertEqual(actual_player, expected_player)