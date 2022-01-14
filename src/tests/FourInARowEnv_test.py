
from unittest import TestCase, main
from src import FourInARowEnv, Players,  BoxState
from src.agents import FourInARowRandomAgent
from copy import deepcopy

class Test_FourInARowEnv(TestCase):

  def test_get_reward_win(self):
    # Arrange 
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )

    expected_reward = 1
    state = deepcopy(env._state)
    state._grid = [
      [BoxState.RED   , BoxState.RED ],
      [BoxState.RED, BoxState.RED ]
    ]

    # Act 
    actual_reward = env.get_reward_for_state(state, Players.RED)
  
    # Assert
    self.assertEqual(actual_reward, expected_reward)



  def test_get_reward_lose(self):
    # Arrange 
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )
    
    expected_reward = -1
    state = deepcopy(env._state)
    state._grid = [
      [BoxState.YELLOW   , BoxState.YELLOW ],
      [BoxState.YELLOW, BoxState.YELLOW ]
    ]

    # Act 
    actual_reward = env.get_reward_for_state(state, Players.RED)
  
    # Assert
    self.assertEqual(actual_reward, expected_reward)


  def test_get_reward_neutral(self):
    # Arrange 
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )
    
    expected_reward = 0
    state = deepcopy(env._state)
    state._grid = [
      [BoxState.RED   , BoxState.EMPTY ],
      [BoxState.YELLOW, BoxState.EMPTY ]
    ]

    # Act 
    actual_reward = env.get_reward_for_state(state, Players.RED)
  
    # Assert
    self.assertEqual(actual_reward, expected_reward)


  def test_is_done(self):
    # Arrange 
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )
    state = deepcopy(env._state)
    state._grid = [
    [BoxState.RED   , BoxState.YELLOW ],
    [BoxState.YELLOW, BoxState.YELLOW ]
        ]

    # act
    env._state = state
    done = env.is_done()
    
    
    # Assert
    self.assertTrue(done)



  def test_step(self):
    # Arrange 
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )
    env._state._grid = [
    [BoxState.RED   , BoxState.EMPTY ],
    [BoxState.EMPTY, BoxState.EMPTY ]
        ]

    expected_grid =  [
    [BoxState.RED   , BoxState.RED ],
    [BoxState.EMPTY, BoxState.EMPTY ]
        ]

    # act
    env.step(0)

    actual_grid = env._state._grid

    # Assert
    self.assertEqual(expected_grid, actual_grid)


  def test_get_possible_states_after_action(self):
      # arrange 
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )
    env._state._grid = [
    [BoxState.EMPTY   , BoxState.EMPTY ],
    [BoxState.EMPTY, BoxState.EMPTY ]
        ]



      # act 
    expected_nr = 2
    actual_nr = len(env.get_possible_states_after_action(env._state,0))
    
    # assert
    self.assertEquals(expected_nr,actual_nr)

  def test_get_possible_states_after_action_none(self):
      # arrange 
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )
    env._state._grid = [
    [BoxState.YELLOW   , BoxState.EMPTY ],
    [BoxState.RED, BoxState.EMPTY ]
        ]



      # act 
    expected_nr = 0
    actual_nr = len(env.get_possible_states_after_action(env._state,0))
    
    # assert
    self.assertEquals(expected_nr,actual_nr)

if __name__ == '__main__':
  main()
