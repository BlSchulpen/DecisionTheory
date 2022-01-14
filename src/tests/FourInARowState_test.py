from unittest import TestCase, main
from src import FourInARowState, FourInARowEnv, Players, BoxState
from ..agents import FourInARowRandomAgent

class Test_FourInARowState(TestCase):
  #================================================================================
  # Column full test
  #================================================================================

  def test_is_column_full_empty(self):
    # Arrange
    state = FourInARowState(width=2, height=2)

    # Assert
    self.assertEqual(False, state.is_column_full(0))


  def test_is_column_full_full(self):
    # Arrange
    state = FourInARowState(width=2, height=2)
    # Act
    state._grid = [
      [BoxState.RED   , BoxState.RED ],
      [BoxState.RED, BoxState.RED ]
    ]    
    
    # Assert
    self.assertEqual(True, state.is_column_full(0))



  def test_horizonal_win(self):
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )

    env._state._grid = [
      [BoxState.RED   , BoxState.EMPTY ],
      [BoxState.RED, BoxState.EMPTY ]
    ]

  
    expected_winner = Players.RED
    actual_winner = env._state._check_horizontal_win()

    # Assert
    self.assertEqual(expected_winner, actual_winner)




  def test_vertical_win(self):
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.YELLOW
    )

    env._state._grid = [
      [BoxState.YELLOW   , BoxState.YELLOW ],
      [BoxState.EMPTY, BoxState.EMPTY ]
    ]

  
    expected_winner = Players.YELLOW
    actual_winner = env._state._check_vertical_win()

    # Assert
    self.assertEqual(expected_winner, actual_winner)


  def test_diagonal_win(self):
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.YELLOW
    )

    env._state._grid = [
      [BoxState.YELLOW   , BoxState.EMPTY ],
      [BoxState.EMPTY, BoxState.YELLOW ]
    ]

  
    expected_winner = Players.YELLOW
    actual_winner = env._state._check_diagonal_win()

    # Assert
    self.assertEqual(expected_winner, actual_winner)

  def test_get_winner_diagonal_win(self):
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.YELLOW
    )

    env._state._grid = [
      [BoxState.YELLOW   , BoxState.EMPTY ],
      [BoxState.EMPTY, BoxState.YELLOW ]
    ]

  
    expected_winner = Players.YELLOW
    actual_winner = env._state.get_winner()

    # Assert
    self.assertEqual(expected_winner, actual_winner)


  def test_get_winner_vertical_win(self):
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.YELLOW
    )

    env._state._grid = [
      [BoxState.YELLOW   , BoxState.YELLOW ],
      [BoxState.EMPTY, BoxState.EMPTY ]
    ]

  
    expected_winner = Players.YELLOW
    actual_winner = env._state.get_winner()

    # Assert
    self.assertEqual(expected_winner, actual_winner)

#get_winner

#_check_vertical_win
if __name__ == '__main__':
  main()
