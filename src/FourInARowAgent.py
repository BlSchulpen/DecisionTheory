from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from .FourInARowEnv import FourInARowEnv

class FourInARowAgent:
  env: 'FourInARowEnv'

  def __init__(self, env: 'FourInARowEnv') -> None:
    self.env = env

  def get_move(self) -> int:
    pass
