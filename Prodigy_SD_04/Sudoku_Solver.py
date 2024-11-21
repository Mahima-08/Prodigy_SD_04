def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def is_safe(grid, row, col, num):
    # Check if num is not in the current row
    if num in grid[row]:
        return False

    # Check if num is not in the current column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check if num is not in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                # Try all possible numbers (1-9)
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num  # Tentatively assign num
                        if solve_sudoku(grid):  # Recursive step
                            return True
                        grid[row][col] = 0  # Backtrack

                return False  # Trigger backtracking if no number works

    return True  # Puzzle solved

def input_sudoku():
    print("Enter your Sudoku puzzle row by row (use 0 for empty cells):")
    grid = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").split()))
                if len(row) == 9 and all(0 <= num <= 9 for num in row):
                    grid.append(row)
                    break
                else:
                    print("Invalid input. Please enter 9 numbers between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    return grid

# Get Sudoku puzzle from the user
puzzle = input_sudoku()

print("\nUnsolved Sudoku Puzzle:")
print_grid(puzzle)

if solve_sudoku(puzzle):
    print("\nSolved Sudoku Puzzle:")
    print_grid(puzzle)
else:
    print("\nNo solution exists for the given puzzle.")
