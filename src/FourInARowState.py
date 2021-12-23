from typing import Optional
from .BoxState import BoxState
from .Players import Players

FourInARowGrid = list[list[BoxState]]

class FourInARowState:
  width      : int
  height     : int
  _grid      : FourInARowGrid
  _turn      : Players
  _first_turn: Players

  def _check_for_four_in_a_row(self, x: int, y: int) -> bool:
    state = self._grid[x][y]

    if state == BoxState.EMPTY:
      return False

  def _create_grid(self) -> None:
    self._grid = [
      [BoxState.EMPTY for _ in range(self.height)]
      for _ in range(self.width)
    ]
    # # just for testing
    # self._grid[0][5] = BoxState.RED
    # self._grid[1][4] = BoxState.RED
    # self._grid[2][3] = BoxState.RED
    # self._grid[3][2] = BoxState.RED
    # self._grid[4][1] = BoxState.RED
    # self._grid[5][0] = BoxState.RED
    # self._grid[6][0] = BoxState.RED


  def __init__(self, width: int = 7, height: int = 6, first_turn: Players = Players.RED) -> None:
    self.width  = width
    self.height = height
    self._turn   = first_turn
    self._first_turn = first_turn

    self._create_grid()

  def reset(self) -> None:
    self._create_grid()
    self._turn = self._first_turn

  def get_grid(self) -> FourInARowGrid:
    return self._grid

  def get_winner(self) -> Optional[Players]:
    pass
