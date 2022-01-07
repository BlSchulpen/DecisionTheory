from typing import Optional
from numpy.lib.function_base import select
from .BoxState import BoxState
from .Players import Players
from .FourInARowState import FourInARowState
from .FourInARowRenderer import FourInARowRenderer
import numpy as np

def player_from_box_state(box_state: BoxState) -> Optional[Players]:
  match box_state:
    case BoxState.EMPTY : return None
    case BoxState.RED   : return Players.RED
    case BoxState.YELLOW: return Players.YELLOW

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

  def get_possible_actions(self, state = None):
    if state is None:
      state = self._state
    possible_states = [] 
    for i in range(self._state.width):
      highest = self._get_highest_possible(i)
      if highest != False:
        possible_states.append(highest)
    return possible_states

  def is_done(self) -> bool:
    winner = self._state.get_winner()
    return winner != None

  def get_reward(self):
    pass

  def get_transition_prob(self, action):
    pass

  # Possible actions methods

  def _get_highest_possible(self,x):
    for j in range(self._state.height):
      if self._state.get_grid()[x][j] == BoxState.EMPTY:
        return (x,j)
    return False
