# Practical 02 - A* Search Algorithm

## Aim
To implement A* Search Algorithm for solving a game search problem.

---

## Theory

A* (A-Star) Algorithm is an informed search algorithm used for path finding and graph traversal.

It finds the shortest path between source and destination nodes using:

- Actual cost function g(n)
- Heuristic function h(n)

The evaluation function is:

f(n) = g(n) + h(n)

Where:
- g(n) = cost from start node to current node
- h(n) = estimated cost from current node to goal node
- f(n) = total estimated cost

A* always selects the path with minimum cost.

---

## Applications
- Game AI
- Path finding
- GPS Navigation
- Robotics
- Maze solving

---

## Algorithm
1. Start from source node
2. Add source node to open list
3. Select node with lowest f(n)
4. Check goal node
5. Expand neighboring nodes
6. Update path cost
7. Repeat until goal is reached