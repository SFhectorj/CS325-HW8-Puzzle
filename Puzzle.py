from collections import deque

def solve_puzzle(Board, Source, Destination):
    """
    :param Board: 2D list where '-' indicates empty cells and '#' indicates barriers.
    :param Source: Tuple (a, b) representing the starting coordinates.
    :param Destination: Tuple (x, y) representing the destination coordinates.
    :returns: None if no valid path, otherwise returns a list of tuples representing path.
    """
    # Directions for moving
    # (Left, Right, Up, Down)
    movement_directions = [(-1,0),(1, 0),(0, -1),(0, 1)]
    puzzle_rows, puzzle_columns = len(Board), len(Board[0])

    # Initialize BFS
    # Dequeue the current_cell and path_so_far
    queue = deque([(Source,[Source])])
    already_visited = set()
    already_visited.add(Source)

    # The search must now iterate the board using a loop
    while queue:
        current_cell, current_path = queue.popleft()

        # Check if current cell is at destination
        if current_cell == Destination:
            return current_path

        # Move to neighbor cells
        for direction_x, direction_y in movement_directions:
            neighbor_cell = (current_cell[0] + direction_x, current_cell[1] +direction_y)

            # Check for validity of neighbor
            # within bounds and empty cell and not already visited
            if 0 <= neighbor_cell[0] < puzzle_rows and 0 <= neighbor_cell[1] < puzzle_columns and Board[neighbor_cell[0]][neighbor_cell[1]] == '-' and neighbor_cell not in already_visited:
                already_visited.add(neighbor_cell)
                # update path
                queue.append((neighbor_cell, current_path + [neighbor_cell]))
    # No path was found
    return None
