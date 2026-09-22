# SLE-2: Profiling Report — BFS vs DFS on Random Mazes

**Course:** 02AML204 – Introduction to Artificial Intelligence
**PRN:** 25UAM108
**Name:** Prathmesh Kore
**Division:** B

## Objective
Extends the SLE-1 chatbot work into an empirical performance analysis task.
Instead of relying on theoretical Big-O alone, this measures real execution
time, nodes expanded, and path quality for BFS and DFS across three maze
sizes (best / average / worst case).

## Problem
Randomly generated grid mazes (20x20, 40x40, 70x70), each regenerated with
new random walls until a path from the top-left start to bottom-right goal
is guaranteed to exist.

## Algorithms Compared
- **BFS (Breadth-First Search)** — uninformed, explores level by level, guarantees the shortest path.
- **DFS (Depth-First Search)**, depth-limited to 1000 — uninformed, explores as deep as possible before backtracking, no shortest-path guarantee.

## Tools Used
- `time.perf_counter()` — precise per-run timing (5 runs per algorithm per maze)
- A manual node counter — nodes expanded (states popped off the frontier)
- `py-spy` — real CPU flamegraph (captured directly, no fallback needed)
- `matplotlib` — maze visualization and time-comparison chart

## Project Structure
```
sle2/
├── maze_search.py         # Maze generator + BFS/DFS implementations
├── run_experiments.py     # Runs both algorithms across 3 maze sizes
├── profile_heavy.py       # Longer loop used only for py-spy sampling
├── results.json           # Raw measured results + maze data
├── fig1_maze.png          # Maze with BFS shortest path highlighted
├── fig3_time_chart.png    # Avg time comparison across test cases
├── flamegraph.svg         # Interactive py-spy flamegraph
└── README.md
```

## How to Run
```
cd sle2
python run_experiments.py
```
Prints a live comparison across all three mazes and saves `results.json`.

To reproduce the py-spy flamegraph:
```
py-spy record -o flamegraph.svg --rate 150 -- python profile_heavy.py
```

## Results Summary
| Test Case | BFS Time (ms) | BFS Nodes | BFS Path | DFS Time (ms) | DFS Nodes | DFS Path |
|---|---|---|---|---|---|---|
| Best (20x20) | 0.2969 | 312 | 39 | 0.1765 | 169 | 77 |
| Average (40x40) | 1.0254 | 1,212 | 79 | 0.7718 | 674 | 167 |
| Worst (70x70) | 4.2612 | 3,617 | 139 | 2.8732 | 1,951 | 333 |

BFS always found the true shortest path; DFS was consistently faster and
expanded fewer nodes at every maze size, but its path was 2.0x–2.4x longer
every time. Full analysis is in `SLE2_25UAM108_PrathmeshKore.docx`.

## AI Contribution
Claude (Anthropic) generated the maze generator, BFS/DFS implementation,
profiling scripts, and charts. All scripts were run and verified
independently on real py-spy output, and the justification was written
based on the actual measured numbers. See the report's AI Contribution
Note section for full details.
