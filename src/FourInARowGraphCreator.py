import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from .FourInARowEnv import FourInARowEnv
from .FourInARowRandomAgent import FourInARowRandomAgent
from .FourInARowValueIterationAgent import FourInARowValueIterationAgent
from .FourInARowSemiRandomAgent import FourInARowSemiRandomAgent
from .FourInARowMinMaxAgent import FourInARowMinMaxAgent

from .Players import Players
from copy import deepcopy

import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

#TODO add graph preformance (time)
#TODO add graphs win ratio

class FourInARowGraphCreator:
    value_iterator_agent: FourInARowValueIterationAgent
    random_agent: FourInARowRandomAgent
    semi_random_agen: FourInARowSemiRandomAgent
    min_max_agen: FourInARowMinMaxAgent

    def __init__(self) -> None:
        pass 
        # self.random_agent = FourInARowRandomAgent
        # self.semi_random_agen = FourInARowSemiRandomAgent
        # self.setup_value_iterator_agent()
        # self.setup_min_max_agent()


    def setup_game(self,opponent) -> FourInARowEnv:
        env = FourInARowEnv(
            yellow_agent  = opponent,
            width         = 3,
            height        = 3,
            win_condition = 3,
            first_turn    = Players.RED
        )
        return env

    #TODO add new graphs to also show ties + loses
    def ratio_value(self, main_type,opponent_type) -> None:
        nr_games = 1
        nr_wins = 0 
        for i in range(nr_games): #TODO frist test graph generation
            env = self.setup_game(FourInARowRandomAgent)
            value_iterator = FourInARowMinMaxAgent(env)
            while not env.is_done():
                env.step(value_iterator.get_move())
            if env._state.get_winner() == Players.RED:
                nr_wins +=1
      

    def generate_graph(self, nr_games: int, min_max_wins:int, value_it_wins:int) -> None:
        data = [["Min-max agent", self.win_ration(nr_games,min_max_wins)], ["Value iteration agent", self.win_ration(nr_games,value_it_wins)] ]
        df = pd.DataFrame(data, columns=['agent_type', 'win-ratio'])

        fig1, ax1 = plt.subplots(figsize=(10,5))
        ax1.set_title('Agents win ratio')
        ax1.bar(np.arange(len(df)), df['win-ratio'])
        ax1.set_xticks(np.arange(len(df)))
        ax1.set_xticklabels(df['agent_type'])
        plt.show()
        rnd_big =random.getrandbits(64)
        plt.savefig(str(rnd_big) + '.png')

    def win_ration(self,nr_games, nr_wins) -> float:
        return (100*nr_wins)/nr_games