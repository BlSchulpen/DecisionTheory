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
      if self.horizontal_win(colour) or self.vertical_win(colour):
        is_done = True
    return is_done

  def diagonal_win(self) -> bool:
    #getting all diagonals
    x = self._state.width
    y = self._state.height
    return False

  def diagonal_spots_lt(self):
    lines = [] 
    x = self._state.width
    y = self._state.height

    for str_row in range(y):
      line =  []
      for i_round in range(str_row):
        x_spot = (str_row - i_round)
        y_spot = (str_row  + i_round)
        line.append(self._state.get_grid()[x_spot][str_row])

      # line.append
      #   self._state.get_grid()[0][i] 

    

# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python

  # Code Quality should be fixed
  def vertical_win(self,colour) -> bool:
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

  def horizontal_win(self,colour) -> bool:
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

  def get_reward(self):
    pass

  def get_transition_prob(self, action):
    pass