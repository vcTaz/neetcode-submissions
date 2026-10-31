class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        NUM_ROWS = 9
        NUM_COLS = 9
        NUM_GRID = 9
        GRID_SIZE = 3

        rows = [(defaultdict(int)) for _ in range(NUM_ROWS)]
        cols = [(defaultdict(int)) for _ in range(NUM_COLS)]
        grids = [(defaultdict(int)) for _ in range(NUM_GRID)]

        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                cell_value = board[i][j]

                if cell_value.isdecimal():
                    rows[i][cell_value] += 1
                    if rows[i][cell_value] > 1:
                        return False

                    cols[j][cell_value] += 1
                    if cols[j][cell_value] > 1:
                        return False
                        
                    grid_index = GRID_SIZE * (i // GRID_SIZE) + (j // GRID_SIZE)

                    grids[grid_index][cell_value] += 1
                    if grids[grid_index][cell_value] > 1:
                        return False
        
        return True

            
