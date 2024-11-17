class Board:
    def __init__(self):
        self._grid = [[" " for _ in range(3)] for _ in range(3)]
        self._terminated = False
    
    def print_board(self):
        for row in self._grid:
            print(row)
    
    def add_mark(self, Row, Column, Mark):
        if Row < 0 or Row > 2 or Column < 0 or Column > 2:
            print(f"Not a valid coordinate ({Row}, {Column})")
            return False 

        if self._grid[Row][Column] != " ":
            print("Cannot place marker on occupied cell.")
            return False
        else:
            self._grid[Row][Column] = Mark
            if self.get_status() != "ongoing":
                self._terminated = True

            return True
    
    def get_actions(self):
        actions = []
        for row in range(3):
            for column in range(3):
                if self._grid[row][column] == " ":
                    actions.append([row, column])
        return actions
    
    def get_turn(self):
        Xcount = 0
        Ocount = 0
        for row in range(3):
            for column in range(3):
                if self._grid[row][column] == "X":
                    Xcount += 1
                if self._grid[row][column] == "O":
                    Ocount += 1
        if Xcount > Ocount:
            return "O"
        else:
            return "X"

    def get_status(self):
        numOfEmptyCells = 0
        # Check rows
        for row in self._grid:
            if row.count("X") == 3:
                return "X"
            if row.count("O") == 3:
                return "O"
            numOfEmptyCells += row.count(" ")
        if numOfEmptyCells == 0:
            return "draw"

        # Check columns
        for columnIndex in range(3):
            columnSequence = ""
            for rowIndex in range(3):
                columnSequence += self._grid[rowIndex][columnIndex]
            if columnSequence == "XXX":
                return "X"
            if columnSequence == "OOO":
                return "O"
        
        # Top Left -> Bottom right
        sequence = ""
        for i in range(3):
            sequence += self._grid[i][i]
        if sequence == "XXX":
            return "X"
        if sequence == "OOO":
            return "O"
        
        # Top right -> Bottom Left
        sequence = self._grid[0][2] + self._grid[1][1] + self._grid[2][0] 
        if sequence == "XXX":
            return "X"
        if sequence == "OOO":
            return "O"

        return "ongoing"
    
    def is_terminated(self):
        return self._terminated