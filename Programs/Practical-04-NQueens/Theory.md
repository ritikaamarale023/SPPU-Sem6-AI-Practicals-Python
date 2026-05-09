# Practical 04 - N Queens Problem using Backtracking

## Aim
To implement a solution for Constraint Satisfaction Problem using Backtracking for N-Queens Problem.

---

## Theory

N-Queens Problem is a classic Constraint Satisfaction Problem in Artificial Intelligence.

The objective is to place N queens on an N×N chessboard such that:
- No two queens attack each other
- No two queens are in same row
- No two queens are in same column
- No two queens are on same diagonal

Backtracking is used to solve this problem recursively.

It places queens one by one and checks whether the current position is safe.

If not safe:
- Backtrack
- Remove previous queen
- Try another position

---

## Applications
- Artificial Intelligence
- Game solving
- Constraint satisfaction problems
- Scheduling problems

---

## Algorithm
1. Start placing queen from first row
2. Check safe position in column
3. Place queen if safe
4. Move recursively to next row
5. If solution fails, backtrack
6. Repeat until all queens are placed
