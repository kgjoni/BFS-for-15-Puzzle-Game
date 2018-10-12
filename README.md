# BFS-for-15-Puzzle-Game

Write a program which performs breadth first search to find the solution to any given
board position for 15 puzzle

Input
The input should be given in form of sequence of numbered tiles for initial board configuration,
‘0’ indicating the empty space (see example below)

Output
1. Moves
2. Number of Nodes expanded
3. TIme Taken
4. Memory Used

Example
Input: 1 0 2 4 5 7 3 8 9 6 11 12 13 10 14 15
Moves: RDLDDRR
Number of Nodes expanded: 2642
TIme Taken: 42ms
Memory Used: 8624kb

Unsolvable puzzle
There can be some puzzle for which the solved state cannot be reached
If the solution doesn’t exist, display the message “solution cannot be found”
Input: 1 2 3 4 5 6 7 8 9 10 11 12 13 15 14
Solution cannot be found

Hint
Check for repeated state to avoid “out of memory” error
