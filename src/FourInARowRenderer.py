from .BoxState import BoxState
from .FourInARowState import FourInARowState

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

    top_line = f"┌{'┬'.join(['───' for _ in range(width)])}┐\r\n"
    horizontal_line = f"├{'┼'.join(['───' for _ in range(width)])}┤"
    bottom_line = f"\r\n└{'┴'.join(['───' for _ in range(width)])}┘"

    background = f'\r\n{horizontal_line}\r\n'.join([
      '│' + '│'.join([
        f' {self._get_character_for_box(w, height - h - 1)} ' for w in range(width)
      ]) + '│' for h in range(height)
    ])

    return f'{top_line}{background}{bottom_line}'

  def render_multiple_states(states: list[FourInARowState], columns: 3) -> str:
    pass
