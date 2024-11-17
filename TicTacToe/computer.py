import random
from board import Board
import copy
import time

class Computer:
    def __init__(self, Mark):
        self._mark = Mark
        self._player_mark = "O" if Mark == "X" else "X"
    def utility(self, Board):
        status = Board.get_status()
        if status == self._mark:
            return 1
        if status == self._player_mark:
            return -1
        return 0

    def get_action(self, Board):
        
        # Min max the board
        print("Computer thinking...")
        maxUtility = -99999
        possibleActions = Board.get_actions()
        for action in possibleActions:
            newBoard = copy.deepcopy(Board)
            newBoard.add_mark(action[0], action[1], self._mark)
            utility = self.min_utility(newBoard)
            if utility > maxUtility:
                maxUtility = utility
                bestAction = action

        return bestAction[0], bestAction[1]

    def min_utility(self, Board):
        if Board.is_terminated():
            return self.utility(Board)
        v = 999999
        for action in Board.get_actions():
            newBoard = copy.deepcopy(Board)
            newBoard.add_mark(action[0], action[1], newBoard.get_turn())
            v = min(v, self.max_utility(newBoard))
        return v

    def max_utility(self, Board):
        if Board.is_terminated():
            return self.utility(Board)
        v = -999999
        for action in Board.get_actions():
            newBoard = copy.deepcopy(Board)
            newBoard.add_mark(action[0], action[1], newBoard.get_turn())
            v = max(v, self.min_utility(newBoard))
        return v

