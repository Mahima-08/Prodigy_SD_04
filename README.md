### README for Sudoku Solver Program

---

# Sudoku Solver Program

This Python program is designed to solve any valid Sudoku puzzle automatically. It uses the **Backtracking Algorithm** to explore possible solutions and find the correct arrangement of numbers for the puzzle. The program accepts an unsolved Sudoku puzzle from the user, processes it, and outputs the solved grid.

---

## Features

- **User-Friendly Input**: The program allows users to input an unsolved Sudoku grid row by row. Empty cells are represented by `0`.
- **Backtracking Algorithm**: A reliable and efficient algorithm is used to solve the puzzle by exploring and validating possible solutions recursively.
- **Input Validation**: Ensures that the user provides a valid 9x9 grid with numbers ranging from 0 to 9.
- **Formatted Output**: Displays both the unsolved and solved grids in a clear and readable format.
- **Error Handling**: If the puzzle is unsolvable, the program notifies the user accordingly.

---

## How to Use

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-repository/sudoku-solver.git
   cd sudoku-solver
   ```

2. **Run the Program**:
   Make sure you have Python installed. Execute the script using:
   ```bash
   python sudoku_solver.py
   ```

3. **Input Your Sudoku Puzzle**:
   - The program will prompt you to enter the puzzle row by row.
   - Enter 9 numbers separated by spaces for each row.
   - Use `0` to represent empty cells.

4. **View the Results**:
   - The program will display your unsolved puzzle and then output the solved grid.
   - If no solution exists, a message will notify you.

---

## Example

### Input:
```
Row 1: 5 3 0 0 7 0 0 0 0
Row 2: 6 0 0 1 9 5 0 0 0
Row 3: 0 9 8 0 0 0 0 6 0
Row 4: 8 0 0 0 6 0 0 0 3
Row 5: 4 0 0 8 0 3 0 0 1
Row 6: 7 0 0 0 2 0 0 0 6
Row 7: 0 6 0 0 0 0 2 8 0
Row 8: 0 0 0 4 1 9 0 0 5
Row 9: 0 0 0 0 8 0 0 7 9
```

### Output:
**Unsolved Sudoku:**
```
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
```

**Solved Sudoku:**
```
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

---

## Algorithm

This program utilizes **Backtracking**, a depth-first search approach, to solve Sudoku. The algorithm works as follows:

1. **Find Empty Cells**: Look for cells with a value of `0`.
2. **Try Numbers**: Attempt placing numbers `1-9` in the empty cell.
3. **Validate**: Check if the number is valid (no conflicts in row, column, or 3x3 grid).
4. **Recursive Call**: Move to the next empty cell and repeat.
5. **Backtrack**: If no number fits, backtrack and try the next possible number.

---

