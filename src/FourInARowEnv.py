from numpy.lib.function_base import select
from src.BoxState import BoxState
from .Players import Players
from .FourInARowState import FourInARowState
from .FourInARowRenderer import FourInARowRenderer
import numpy as np

class FourInARowEnv:
  _state   : FourInARowState
  _renderer: FourInARowRenderer

  def _calculate_possible_states(self):
    pass

  def _calculate_transition(self, action):
    pass

  def __init__(self, width: int = 7, height: int = 6, first_turn: Players = Players.RED) -> None:
    self._state    = FourInARowState(width=width, height=height, first_turn=first_turn)
    self._renderer = FourInARowRenderer(self._state)

  def reset(self) -> None:
    self._state.reset()

  def step(self, action):
    pass

  def render(self) -> str:
    return self._renderer.render()

  def get_possible_states(self):
    pass

  def get_possible_actions(self):
    pass


  def is_done(self) -> bool:
    is_done = False
    allowed_winners = [BoxState.RED,BoxState.YELLOW]
    for colour in allowed_winners:
      if self._horizontal_win(colour) or self._vertical_win(colour) or self._diagonal_win(colour):
        is_done = True
    return is_done


  def get_reward(self):
    pass

  def get_transition_prob(self, action):
    pass



# Is done methods

  # Code Quality should be fixed
  def _vertical_win(self,colour) -> bool:
    streak = 0 
    for i in range(self._state.width):
        for j in range(self._state.height):   
          if self._state.get_grid()[i][j] == colour:
            streak +=1
            if streak == 4:
              return True
          else:
            streak = 0
    return False

  def _horizontal_win(self,colour) -> bool:
    streak = 0 
    for i in range(self._state.height):
        for j in range(self._state.width):   
          if self._state.get_grid()[j][i] == colour:
            streak +=1
            if streak == 4:
              return True
          else:
            streak = 0
    return False

  def _diagonal_win(self,colour) -> bool:
    for diagonal in self._get_all_diagonals():
      if self._is_diag_valid(diagonal,colour):
        return True
    return False

  def _get_all_diagonals(self):
    x = self._state.width
    y = self._state.height

    a = np.arange(x*y).reshape(x,y)
    diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
    diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

    dia_arr = []
    for diagonal_ar in diags:
      new_line = []
      for spot in diagonal_ar:
        given_nr = spot 
        column_nr = given_nr // self._state.height
        row_nr = given_nr % self._state.height
        row_nr_fixed = (y-row_nr) -1
        new_line.append(self._state.get_grid()[column_nr][row_nr_fixed])
      dia_arr.append(new_line)
    return dia_arr

# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python

  def _is_diag_valid(self, diag, colour) -> bool:
    streak = 0 
    for spot in diag:
      if spot == colour:
        streak +=1
        if streak ==4:
          return True
      else:
        streak = 0
    return False
    