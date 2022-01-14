from typing import TYPE_CHECKING
from .Players import Players

if TYPE_CHECKING:
  from .FourInARowEnv import FourInARowEnv

class FourInARowAgent:
  env: 'FourInARowEnv'
  player: Players

  def __init__(self, env: 'FourInARowEnv', player: Players = Players.RED) -> None:
    self.env = env
    self.player = player

  def get_move(self) -> int:
    pass
