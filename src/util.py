from typing import Optional
from src.BoxState import BoxState
from src.Players import Players

def player_from_box_state(box_state: BoxState) -> Optional[Players]:
  match box_state:
    case BoxState.EMPTY : return None
    case BoxState.RED   : return Players.RED
    case BoxState.YELLOW: return Players.YELLOW

def box_state_from_player(player: Players) -> BoxState:
  match player:
    case Players.RED   : return BoxState.RED
    case Players.YELLOW: return BoxState.YELLOW
