from lib2to3.pgen2.pgen import generate_grammar
from tracemalloc import start
from unittest import result
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from .FourInARowEnv import FourInARowEnv
from src.agents import FourInARowRandomAgent
from src.agents import FourInARowValueIterationAgent
from src.agents import FourInARowSemiRandomAgent
from src.agents import FourInARowBruteForceAgent
import time
from .Players import Players
from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 



from enum import Enum
class WinType(Enum):
    WIN = 1
    TIE = 2
    LOSE = 3

class FourInARowGameResults:
    wins: int
    ties: int
    loses: int
    agent: str

    def __init__(self,wins:int,ties:int,loses:int,agent: str) -> None:
        self.wins = wins
        self.loses = loses
        self.ties = ties
        self.agent = agent

class FourInARowGraphCreator:
    value_iterator_agent: FourInARowValueIterationAgent
    random_agent: FourInARowRandomAgent
    semi_random_agen: FourInARowSemiRandomAgent
    brute_for_agent: FourInARowBruteForceAgent
    nr_games: int

    def __init__(self) -> None:
        self.nr_games = 20

    def setup_game(self,opponent) -> FourInARowEnv:
        env = FourInARowEnv(
            yellow_agent  = opponent,
            width         = 3,
            height        = 3,
            win_condition = 3,
            first_turn    = Players.RED
        )
        return env


    def play_game(self, player_type,opponent_type) -> WinType:
        env = FourInARowEnv(
            yellow_agent  = opponent_type,
            width         = 3,
            height        = 3,
            win_condition = 3,
            first_turn    = Players.RED
            )

        agent = player_type(env)
        states = []
        states.append(deepcopy(env.get_state()))
        while not env.is_done():
            env.step(agent.get_move())
            states.append(deepcopy(env.get_state()))
        if env._state.get_winner() == Players.RED:
            return WinType.WIN
        elif env._state.get_winner() == Players.YELLOW:
            return WinType.LOSE
        return WinType.TIE


    def plot_acc(self,players_to_meassure, name,opponent_type):
        scores = []

        for player in players_to_meassure:
            game_result = FourInARowGameResults(0,0,0,player.__name__)
            for i in range(self.nr_games):
                end_state = self.play_game(player,opponent_type)
                if end_state == WinType.WIN:
                    game_result.wins +=1
                elif end_state== WinType.LOSE:
                    game_result.loses +=1
                else:
                    game_result.ties +=1
            scores.append(game_result)
        self.generate_graph(scores,name)


    def generate_graph(self, results:list[FourInARowGameResults], name: str) -> None:        
        # create data
        x = []
        for item in results:
            name_fixed = item.agent.removeprefix('FourInARow')
            name_fixed= name_fixed.removesuffix('Agent')    
            x.append(name_fixed)

        wins = [] 
        ties = []
        loses = [] 
        for result in results:
            wins.append(result.wins)
            ties.append(result.ties)
            loses.append(result.loses)


        y1 = np.array(wins)
        y2 = np.array(ties)
        y3 = np.array(loses)
        plt.figure(facecolor='#94F008')

        # plot bars in stack manner
        plt.bar(x, y1, color='g')
        plt.bar(x, y2, bottom=y1, color='y')
        plt.bar(x, y3, bottom=y1+y2, color='r')

        plt.xlabel("Agents")
        plt.ylabel("Score")
        plt.legend(["Wins", "Ties", "Loses"])
        plt.title(name)

        plt.show()


    def meassure_preformance(self,player,opponent):
        start_time = time.time()
        self.play_game(player,opponent)
        return (time.time() - start_time)

    def plot_preformance(self,players_to_meassure):
        names = []
        execution_time = []

        for player in players_to_meassure:
            name_fixed = player.__name__.removeprefix('FourInARow')
            name_fixed= name_fixed.removesuffix('Agent')    
            names.append(name_fixed)
            player_exe_time= []
            for i in range(self.nr_games):
                exe_time = self.meassure_preformance(player,FourInARowRandomAgent)
                player_exe_time.append(exe_time)
            execution_time.append(player_exe_time)
        self.generate_line_graph_preformance(execution_time,names)



    def generate_line_graph_preformance(self,y_values,names:list[str]):
        x = []
        for i in range(self.nr_games):
            x.append(i)

        plt.figure(facecolor='#94F008')

        # plot lines
        for i in range(len(y_values)):
            plt.plot(x,y_values[i], label=names[i])

        plt.xlabel("Game number")
        plt.ylabel("Time (ms)")
        plt.legend()
        plt.show()

    def win_ration(self,nr_games, nr_wins) -> float:
        return (100*nr_wins)/nr_games

