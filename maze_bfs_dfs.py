import random
import time
from collections import deque


# ---------------------------------------
# Maze Generation
# ---------------------------------------

def generate_maze(rows, cols, wall_probability=0.25):
    while True:
        maze = []

        for r in range(rows):
            row = []
            for c in range(cols):
                if random.random() < wall_probability:
                    row.append(1)       # Wall
                else:
                    row.append(0)       # Free cell
            maze.append(row)

        # Start and goal
        maze[0][0] = 0
        maze[rows - 1][cols - 1] = 0

        if _is_solvable(maze, (0, 0), (rows - 1, cols - 1)):
            return maze
        # otherwise loop again and generate a fresh maze


def _is_solvable(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    visited = set()
    visited.add(start)

    queue = deque()
    queue.append(start)

    while queue:
        r, c = queue.popleft()

        if (r, c) == goal:
            return True

        for neighbor in get_neighbors(maze, (r, c)):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


# ---------------------------------------
# Get Valid Neighbours
# ---------------------------------------

def get_neighbors(maze, cell):
    rows = len(maze)
    cols = len(maze[0])

    r, c = cell

    # Fixed order: Up, Down, Left, Right
    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    neighbors = []

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if maze[nr][nc] == 0:
                neighbors.append((nr, nc))

    return neighbors


# ---------------------------------------
# BFS Algorithm
# ---------------------------------------

def bfs(maze, start, goal):

    queue = deque()
    queue.append((start, [start]))

    visited = set()
    visited.add(start)

    nodes_expanded = 0

    while queue:

        current, path = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        for neighbor in get_neighbors(maze, current):

            if neighbor not in visited:
                visited.add(neighbor)

                queue.append(
                    (neighbor, path + [neighbor])
                )

    return None, nodes_expanded


# ---------------------------------------
# DFS Algorithm
# ---------------------------------------

def dfs(maze, start, goal, depth_limit=1000):

    stack = []
    stack.append((start, [start], 0))

    visited = set()
    visited.add(start)

    nodes_expanded = 0

    while stack:

        current, path, depth = stack.pop()
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        if depth >= depth_limit:
            continue

        for neighbor in get_neighbors(maze, current):

            if neighbor not in visited:
                visited.add(neighbor)

                stack.append(
                    (neighbor,
                     path + [neighbor],
                     depth + 1)
                )

    return None, nodes_expanded


# ---------------------------------------
# Run One Test
# ---------------------------------------

def run_test(rows, cols):

    maze = generate_maze(rows, cols)

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    # BFS timing
    start_time = time.perf_counter()

    bfs_path, bfs_nodes = bfs(
        maze,
        start,
        goal
    )

    bfs_time = time.perf_counter() - start_time

    # DFS timing
    start_time = time.perf_counter()

    dfs_path, dfs_nodes = dfs(
        maze,
        start,
        goal
    )

    dfs_time = time.perf_counter() - start_time

    print("\n-----------------------------")
    print(f"Maze Size: {rows} x {cols}")
    print("-----------------------------")

    print("\nBFS")
    print("Time:", round(bfs_time * 1000, 4), "ms")
    print("Nodes Expanded:", bfs_nodes)

    if bfs_path:
        print("Path Length:", len(bfs_path) - 1)
    else:
        print("No path found")

    print("\nDFS")
    print("Time:", round(dfs_time * 1000, 4), "ms")
    print("Nodes Expanded:", dfs_nodes)

    if dfs_path:
        print("Path Length:", len(dfs_path) - 1)
    else:
        print("No path found")


# ---------------------------------------
# Main Program
# ---------------------------------------

if __name__ == "__main__":

    print("BFS vs DFS Maze Path-Finding")
    print("============================")

    # 20 x 20 maze
    run_test(20, 20)

    # 40 x 40 maze
    run_test(40, 40)

    # 70 x 70 maze
    run_test(70, 70)
