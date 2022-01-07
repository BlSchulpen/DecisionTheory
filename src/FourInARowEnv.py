from numpy.lib.function_base import select
from src.BoxState import BoxState
from .Players import Players
from .FourInARowState import FourInARowState
from .FourInARowRenderer import FourInARowRenderer
import numpy as np
from copy import copy

class FourInARowEnv:
  _state   : FourInARowState
  _renderer: FourInARowRenderer

  def __init__(self, width: int = 7, height: int = 6, first_turn: Players = Players.RED) -> None:
    self._state    = FourInARowState(width=width, height=height, first_turn=first_turn)
    self._renderer = FourInARowRenderer(self._state)
    self.__possible_states = []
  self._calculate_possible_states(self._state)


  def calculate_possible_states(self, state):
    # pass
      actions = self.get_possible_actions(state)
      for action in actions:
          new_state = copy(state)
          if self.nr_state(state,BoxState.RED) == self.nr_state(state,BoxState.YELLOW):  
              new_state.get_grid()[action[0]][action[1]] =BoxState.RED 
          else: 
              new_state.get_grid()[action[0]][action[1]] =BoxState.YELLOW 
          self.__possible_states.append(new_state)
          if not self.is_done(new_state):
              self._calculate_possible_states(new_state)
  
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
    return self.__possible_states

  def get_possible_actions(self, state = None):
    if state is None:
      state = self._state
    possible_states = [] 
    for i in range(self._state.width):
      highest = self._get_highest_possible(i)
      if highest != False:
        possible_states.append(highest)
    return possible_states

  def is_done(self, state = None) -> bool:
    if state == None:
      state = self._state
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

    # https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python  
  def _get_all_diagonals(self):
    x = self._state.width
    y = self._state.height

    a = np.arange(x*y).reshape(x,y) # a = matrix like the grid but with numbers instead of BoxStates
    diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])] # get the diagonals (array of arrays with numbers that are diagnoal (1ste diagonal line))
    diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1)) # add second diagonal line

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

# Possible actions methods

  def _get_highest_possible(self,x):
    for j in range(self._state.height):
      if self._state.get_grid()[x][j] == BoxState.EMPTY:
        return (x,j)
    return False