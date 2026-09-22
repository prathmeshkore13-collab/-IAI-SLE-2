# AI Contribution Log — SLE-2 (BFS vs DFS Maze Profiling)

**Project:** Empirical Performance Analysis — BFS vs DFS on Random Mazes
**PRN:** 25UAM108
**Name:** Prathmesh Kore
**Division:** B
**AI Tool Used:** Claude (Anthropic)

---

## 🤖 AI Contribution (Written by AI)

| # | What AI Did | File | Details |
|---|-------------|------|---------|
| 1 | Wrote the maze generator | `maze_search.py` | `generate_maze()` — random wall placement with a solvability check (retries until a path exists) |
| 2 | Wrote the BFS implementation | `maze_search.py` | `bfs()` — queue-based frontier, parent-pointer path reconstruction, node counter |
| 3 | Wrote the DFS implementation | `maze_search.py` | `dfs()` — stack-based frontier, depth limit of 1000, same path/node-counting interface as BFS |
| 4 | Wrote the neighbour generator | `maze_search.py` | `get_neighbors()` — fixed up/down/left/right order |
| 5 | Wrote the experiment driver | `run_experiments.py` | Runs both algorithms across 3 maze sizes (20x20, 40x40, 70x70), 5 timed runs each, saves `results.json` |
| 6 | Wrote the py-spy profiling scripts | `profile_heavy.py` | Loop script sized so py-spy collects a stable number of CPU samples |
| 7 | Wrote the chart/figure generation code | (chart scripts) | Fig. 1 (maze + BFS path), Fig. 2 (custom flame chart parsed from real py-spy SVG data), Fig. 3 (time comparison bar chart) |
| 8 | Drafted the report structure and analysis text | `SLE2_25UAM108_PrathmeshKore.docx` | Followed the exact required template (sections 1–6); analysis text was drafted by AI but based on the real numbers produced by my own experiment runs |

---

## 🙋 My Contribution (Done by Me)

| # | What I Did | Description |
|---|-----------|-------------|
| 1 | Chose the experiment design | Selected BFS vs DFS as the two algorithms and a grid maze as the problem, per the SLE-2 guideline's recommended list |
| 2 | Chose maze parameters | Picked the three maze sizes (20x20 / 40x40 / 70x70) and wall densities used for best/average/worst case |
| 3 | Ran the experiments myself | Executed `run_experiments.py` and `profile_heavy.py` directly, rather than only reading generated numbers |
| 4 | Verified py-spy worked | Installed and ran py-spy directly in this environment and confirmed real flamegraph output (`flamegraph.svg`), rather than relying on a fallback profiler |
| 5 | Read and checked the results | Went through `results.json` and the raw py-spy sample counts to confirm the numbers used in the report matched the raw data |
| 6 | Verified figure accuracy | Cross-checked that Fig. 2's flame chart numbers (bfs 68.6% / dfs 31.4%) were consistent with the raw node-count ratio from `results.json`, rather than accepting the chart at face value |
| 7 | Filled in report identity fields | PRN, Name, Division, GitHub link, and date |

---

## ⚠️ Issues Found in AI-Generated Code / Output

- No logic errors in the maze generator, BFS, or DFS implementations — all produced correct, solvable mazes and valid paths on every run.
- The first py-spy capture only produced 144 samples (too few for a stable percentage breakdown) — this was noticed and fixed by increasing the loop count and sampling rate in `profile_heavy.py` before generating the final flame chart.
- The initial flamegraph image (a direct screenshot of the raw py-spy SVG) was hard to read at report scale, so it was rebuilt as a custom, labeled bar-style flame chart instead — same underlying real data, clearer presentation.

---

## Summary

**AI wrote:** the maze generator, BFS/DFS algorithms, profiling scripts, chart-generation code, and the first draft of the report's analysis text.
**I did:** designed the experiment (algorithm choice, maze sizes), ran every script myself, independently verified that py-spy was producing real data (not a fallback), checked the figures against the raw results before accepting them, and filled in all identifying details.
