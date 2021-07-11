import numpy as np, copy

class Sudoku:
    def __init__(self):
        # global variables
        self.possible_values = [[set([1,2,3,4,5,6,7,8,9]) for _ in range(0, 9)] for _ in range(0, 9)]
        self.final_values = np.full((9,9),0)
        self.no_of_cell_filled = 0
    
    
    def is_goal(self):
        if self.no_of_cell_filled == 81:
            return True
    
    
    def get_final_state(self):
        if self.is_goal():
            return self.final_values
        else:
            return np.full((9,9),-1)
    
    
    def set_value(self, row, col, assigned_value):
        self.final_values[row][col] = assigned_value
        # to create a variable that can store the previous state before discarding value
        possible_values_last = copy.deepcopy(self.possible_values)
        
        self.possible_values[row][col].discard(assigned_value)
        
        # to ensure it does not contain the same number horizontally
        for diff_col in range(0, 9):
            if diff_col != col:
                self.possible_values[row][diff_col].discard(assigned_value)
        
        # to ensure it does not contain the same number vertically
        for diff_row in range(0, 9):
            if diff_row != row:
                self.possible_values[diff_row][col].discard(assigned_value)
            
        # to ensure it does not contain the same number in submatrix
        if row < 3:
            adjusted_row = 0
        elif row < 6:
            adjusted_row = 3
        elif row < 9:
            adjusted_row = 6
        
        if col < 3:
            adjusted_col = 0
        elif col < 6:
            adjusted_col = 3
        elif col < 9:
            adjusted_col = 6
            
        for i in range(0, 3):
            for j in range(0, 3):
                if (adjusted_row + i != row) or (adjusted_col + j != col):
                    self.possible_values[adjusted_row + i][adjusted_col + j].discard(assigned_value)
        
        # keep tracking of the cell that has been filled
        self.no_of_cell_filled += 1
        
        return possible_values_last
    
    
    def remove_assignment(self, row, col, tried_value, possible_values_last):
        """
        from pseudocode:,
        remove {var = value} and inferences from assignment
        This method reset and change possible values back to its previous state
        """
        self.final_values[row][col] = 0

        # change back to the previous possible value state
        self.possible_values = copy.deepcopy(possible_values_last)
        
        # as the previous move leads to failure
        self.no_of_cell_filled -= 1
        
    
    def load_puzzle(self, sudoku):
        for row in range(0, 9):
            for col in range(0, 9):
                if sudoku[row][col] != 0:
                    if sudoku[row][col] in self.possible_values[row][col]:
                        insert_value = sudoku[row][col]
                        self.set_value(row, col, insert_value)
                    else:
                        return False
        return True
                    
    
    def pick_zero(self):
        for row in range(0, 9):
            for col in range(0 ,9):
                if self.final_values[row][col] == 0:
                    empty_cell = [row, col]
                    return empty_cell
