import numpy as np
from computer import Computer
from board import Board

class Game:
    def __init__(self, PlayVsComputer = False, ComputerMark = "X"):
        self._turn = 0
        self._board = Board()
        self._game_finished = False
        self._play_computer = PlayVsComputer
        self._computer_mark = ComputerMark
        self._computer = Computer(ComputerMark)
    def start(self):
        while(True):
            self._board.print_board()
            Mark = "X" if self._turn % 2 == 0 else "O"

            if not self._play_computer:
                if Mark == "X":
                    playerInput = input("PlayerX select spot:")
                    row, column = playerInput.split(" ")
                    success = self._board.add_mark(int(row)-1, int(column)-1, Mark)
                    while not success: # No do-while in python unfortunately :(
                        print("Please choose valid action")
                        playerInput = input("PlayerX select spot:")
                        row, column = playerInput.split(" ")
                        success = self._board.add_mark(int(row)-1, int(column)-1, Mark)
                else:
                    playerInput = input("PlayerO select spot:")
                    row, column = playerInput.split(" ")
                    success = self._board.add_mark(int(row)-1, int(column)-1, Mark)
                    while not success: 
                        print("Please choose valid action")
                        playerInput = input("PlayerO select spot:")
                        row, column = playerInput.split(" ")
                        success = self._board.add_mark(int(row)-1, int(column)-1, Mark)
            else:
                if Mark == self._computer_mark:
                    row, column = self._computer.get_action(self._board)
                    success = self._board.add_mark(int(row), int(column), self._computer_mark)
                    while not success: 
                        print("Please choose valid action")
                        row, column = self._computer.get_action(self._board)
                        success = self._board.add_mark(int(row), int(column), self._computer_mark)
                else:
                    playerInput = input("Player select spot:")
                    row, column = playerInput.split(" ")
                    success = self._board.add_mark(int(row)-1, int(column)-1, Mark)
                    while not success: 
                        print("Please choose valid action")
                        playerInput = input("Player select spot:")
                        row, column = playerInput.split(" ")
                        success = self._board.add_mark(int(row)-1, int(column)-1, Mark)

            status = self._board.get_status()

            self._turn += 1

            if status == "ongoing":
                continue
            elif status == "X":
                print("X won!")
            elif status == "O":
                print("O won!")
            
            self._board.print_board()
            break
        
        def get_turn(self):
            return "X" if self._turn % 2 == 0 else "O"

        self._game_finished = True
            