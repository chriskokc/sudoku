def depth_first_search(my_state=Sudoku()):
    if my_state.pick_zero() is not None:
        empty_row = my_state.pick_zero()[0]
        empty_col = my_state.pick_zero()[1]

        # avoid using changing possible values during the process of setting values to empty cells
        value_to_try = copy.deepcopy(my_state.possible_values[empty_row][empty_col])

        for value in value_to_try:
            possible_values_last = my_state.set_value(empty_row, empty_col, value)

            depth_first_search(my_state)

            # when all the cells have been filled and a result is obtained
            if my_state.is_goal():
                return my_state

            """
            from pseudocode:,
            remove {var = value} and inferences from assignment\n",

            if a value choice leads to failure:\n",
            then value assignments (including those made by inference) are removed from the current assignment\n",
            and a new value is tried.

            """
            # remove the tried value, backtrack and try another value
            my_state.remove_assignment(empty_row, empty_col, value, possible_values_last)
