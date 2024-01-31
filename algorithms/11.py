from __future__ import annotations


def depth_first_search(
    possible_board: list[int],
    diagonal_right_collisions: list[int],
    diagonal_left_collisions: list[int],
    boards: list[list[str]],
    n: int,
) -> None:
    """
    >>> boards = []
    >>> depth_first_search([], [], [], boards, 4)
    >>> for board in boards:
    ...     print(board)
    ['. Q . . ', '. . . Q ', 'Q . . . ', '. . Q . ']
    ['. . Q . ', 'Q . . . ', '. . . Q ', '. Q . . ']
    """

    # Get next row in the current board (possible_board) to fill it with a queen
    row = len(possible_board)

    # If row is equal to the size of the board it means there are a queen in each row in
    # the current board (possible_board)
    if row == n:
        # We convert the variable possible_board that looks like this: [1, 3, 0, 2] to
        # this: ['. Q . . ', '. . . Q ', 'Q . . . ', '. . Q . ']
        boards.append([". " * i + "Q " + ". " * (n - 1 - i) for i in possible_board])
        return

    # We iterate each column in the row to find all possible results in each row
    for col in range(n):
        # We apply that we learned previously. First we check that in the current board
        # (possible_board) there are not other same value because if there is it means
        # that there are a collision in vertical. Then we apply the two formulas we
        # learned before:
        #
        # 45º: y - x = b or 45: row - col = b
        # 135º: y + x = b or row + col = b.
        #
        # And we verify if the results of this two formulas not exist in their variables
        # respectively.  (diagonal_right_collisions, diagonal_left_collisions)
        #
        # If any or these are True it means there is a collision so we continue to the
        # next value in the for loop.
        if (
            col in possible_board
            or row - col in diagonal_right_collisions
            or row + col in diagonal_left_collisions
        ):
            continue

        # If it is False we call dfs function again and we update the inputs
        depth_first_search(
            [*possible_board, col],
            [*diagonal_right_collisions, row - col],
            [*diagonal_left_collisions, row + col],
            boards,
            n,
        )


def n_queens_solution(n: int) -> None:
    boards: list[list[str]] = []
    depth_first_search([], [], [], boards, n)

    # Print all the boards
    for board in boards:
        for column in board:
            print(column)
        print("")

    print(len(boards), "solutions were found.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    n_queens_solution(4)