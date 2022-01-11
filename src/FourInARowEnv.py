from typing import Optional
from numpy.lib.function_base import select
from .BoxState import BoxState
from .Players import Players
from .FourInARowState import FourInARowState
from .FourInARowRenderer import FourInARowRenderer
import numpy as np
from copy import copy

def player_from_box_state(box_state: BoxState) -> Optional[Players]:
  match box_state:
    case BoxState.EMPTY : return None
    case BoxState.RED   : return Players.RED
    case BoxState.YELLOW: return Players.YELLOW

class FourInARowEnv:
  _state   : FourInARowState
  _renderer: FourInARowRenderer

  def __init__(self, width: int = 7, height: int = 6, first_turn: Players = Players.RED) -> None:
    self._state    = FourInARowState(width=width, height=height, first_turn=first_turn)
    self._renderer = FourInARowRenderer(self._state)
    self._possible_states = []


  def calculate_possible_states(self, state):
    # pass
    actions = self.get_possible_actions(state)
    for action in actions:
      new_state = copy(state)
      if self.nr_state(state,BoxState.RED) == self.nr_state(state,BoxState.YELLOW):  
        new_state.get_grid()[action[0]][action[1]] =BoxState.RED 
      else: 
        new_state.get_grid()[action[0]][action[1]] =BoxState.YELLOW 
      self._possible_states.append(new_state)
      if not self.is_done(new_state):
        self.calculate_possible_states(new_state)
  
  def nr_state(self,state,given_state):
    nr_state = 0 
    for column in state.get_grid():
      for item in column:
        if item == given_state:
          nr_state +=1
    return nr_state

  def _calculate_transition(self, action):
    pass


  def reset(self) -> None:
    self._state.reset()

  def step(self, action):
    pass

  def render(self) -> str:
    return self._renderer.render()

  def get_possible_states(self):
    return self.calculate_possible_states(self._state)

  def get_possible_actions(self, state: FourInARowState = None) -> list[int]:
    if state is None:
      state = self._state
    return [column for column in range(state.width) if not state.is_column_full(column)]

  def place_chip(self, player: Players, column: int) -> None:
    self._state.place_chip(player, column)

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
