from typing import Optional
import numpy as np

from .util import box_state_from_player, get_other_player, player_from_box_state
from .BoxState import BoxState
from .Players import Players

FourInARowGrid = list[list[BoxState]]

class FourInARowState:
  width         : int
  height        : int
  _grid         : FourInARowGrid
  _turn         : Players
  _first_turn   : Players
  _win_condition: int

  def _check_for_four_in_a_row(self, x: int, y: int) -> bool:
    state = self._grid[x][y]

    if state == BoxState.EMPTY:
      return False

  def _create_grid(self) -> None:
    self._grid = [
      [BoxState.EMPTY for _ in range(self.height)]
      for _ in range(self.width)
    ]

  def _check_section_for_win(self, section: list[BoxState]) -> Optional[Players]:
    count = 0
    count_owner: Optional[Players] = None
    for item in section:
      match player_from_box_state(item):
        case None:
          count = 0
          count_owner = None
        case player if player == count_owner:
          count += 1
          if count == self._win_condition:
            return player
        case _:
          count = 1
          count_owner = player
  
  def _check_vertical_win(self) -> Optional[Players]:
    for col in range(self.width):
      result = self._check_section_for_win(self._grid[col])
      if result != None:
        return result
    return None

  def _check_horizontal_win(self) -> Optional[Players]:
    for row in range(self.height):
      section = [self._grid[col][row] for col in range(self.width)]
      result = self._check_section_for_win(section)
      if result != None:
        return result
    return None

  # Not very pretty...
  def _check_diagonal_win(self) -> Optional[Players]:
    flipped = np.fliplr(self._grid)
    for i in range(self.width):
      result = self._check_section_for_win(np.diagonal(self._grid, i))
      if result != None:
        return result

      result_flipped = self._check_section_for_win(np.diagonal(flipped, i))
      if result_flipped != None:
        return result_flipped

    for i in range(self.height):
      result = self._check_section_for_win(np.diagonal(self._grid, -i))
      if result != None:
        return result

      result_flipped = self._check_section_for_win(np.diagonal(flipped, -i))
      if result_flipped != None:
        return result_flipped

    return None

  def _get_column_height(self, column: int) -> int:
    if column >= self.width:
      raise Exception(f'given column ({column}) outside of playing field {self.width}')
    
    for row in range(self.height):
      if self._grid[column][row] == BoxState.EMPTY:
        return row
    return self.height

  def __init__(self, width: int = 7, height: int = 6, first_turn: Players = Players.RED, win_condition: int = 4) -> None:
    self.width          = width
    self.height         = height
    self._turn          = first_turn
    self._first_turn    = first_turn
    self._win_condition = win_condition

    self._create_grid()

  def reset(self) -> None:
    self._create_grid()
    self._turn = self._first_turn

  def get_grid(self) -> FourInARowGrid:
    return self._grid

  def get_winner(self) -> Optional[Players]:
    horizontal_winner = self._check_horizontal_win()
    vertical_winner = self._check_vertical_win()
    diagonal_winner = self._check_diagonal_win()

    if horizontal_winner != None:
      return horizontal_winner
    if vertical_winner != None:
      return vertical_winner
    if diagonal_winner != None:
      return diagonal_winner
    
    return None

  def is_column_full(self, column: int) -> bool:
    return self._get_column_height(column) >= self.height

  def place_chip(self, column: int) -> None:
    height = self._get_column_height(column)
    if height >= self.height:
      raise Exception(f'column {column} already filled')

    self._grid[column][height] = box_state_from_player(self.get_player_turn())
    self._turn = get_other_player(self._turn)
    
  def get_player_turn(self) -> Players:
    return self._turn

  def is_full(self) -> bool:
    for column in self._grid:
      for chip in column:
        if chip != BoxState.EMPTY:
          return False
    return True
