import math
from typing import Callable
from .BoxState import BoxState
from .FourInARowState import FourInARowState

# The rendering code is truly horrible, don't look at it too much.

class FourInARowRenderer:
  _state: FourInARowState

  def _get_character_for_box(self, x: int, y: int) -> str:
    state = self._state.get_grid()[x][y]

    if state == BoxState.RED:
      return 'R'
    elif state == BoxState.YELLOW:
      return 'Y'
    else:
      return ' '

  def __init__(self, state: FourInARowState) -> None:
    self._state = state

  def render(self) -> str:
    width, height = self._state.width, self._state.height

    top_line = f"┌{'┬'.join(['───' for _ in range(width)])}┐\n"
    horizontal_line = f"├{'┼'.join(['───' for _ in range(width)])}┤"
    bottom_line = f"\n└{'┴'.join(['───' for _ in range(width)])}┘"

    background = f'\n{horizontal_line}\n'.join([
      '│' + '│'.join([
        f' {self._get_character_for_box(w, height - h - 1)} ' for w in range(width)
      ]) + '│' for h in range(height)
    ])

    return f'{top_line}{background}{bottom_line}'

def render_multiple_states(states: list[FourInARowState], columns: 3, additional_info: Callable[[FourInARowState], str]) -> str:
  result = ''
  grids = [FourInARowRenderer(s).render().split('\n') + [' ' + l.ljust(s.width * 4, ' ') for l in additional_info(s).split('\n')] for s in states]

  for i in range(math.ceil(len(grids) / columns)):
    selection = grids[i * columns:i * columns + columns]
    lines = len(selection[0])

    for l in range(lines):
      result += ' '.join([s[l] for s in selection]) + '\n'

    result += '\n'

  return result
