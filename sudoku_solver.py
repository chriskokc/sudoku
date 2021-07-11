def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """

    my_puzzle = Sudoku()
    puzzle_is_loaded_successfully = my_puzzle.load_puzzle(sudoku)

    no_solution = np.full((9, 9), -1)

    if not puzzle_is_loaded_successfully:
        return no_solution

    depth_first_search(my_puzzle)
    solved_sudoku = my_puzzle.get_final_state()

    return solved_sudoku