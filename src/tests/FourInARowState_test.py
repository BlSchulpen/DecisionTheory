from unittest import TestCase, main
from .. import FourInARowState
from src import FourInARowEnv, FourInARowRandomAgent, Players, render_multiple_states, BoxState, FourInARowRenderer, FourInARowValueIterationAgent
from copy import deepcopy

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


if __name__ == '__main__':
  main()