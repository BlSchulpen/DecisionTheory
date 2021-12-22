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
    self._grid[0][0] = BoxState.RED
    self._grid[1][0] = BoxState.RED
    self._grid[2][0] = BoxState.RED
    self._grid[3][0] = BoxState.RED

    # self.get_grid[0][0] = Players.RED
    # self.get_grid[(self.width - 1)][(self.height - 1)] = Players.YELLOW

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
