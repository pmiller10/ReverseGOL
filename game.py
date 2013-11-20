class Board:

    def __init__(self, cells, height, width):
        self.height, self.width = height, width
        total = height * width
        assert len(cells) == total
        cells = [Cell(c, 0, 0, self) for c in cells]
        rows, columns = [], []

        # populate the rows
        pointer = 0
        for h in range(height):
            row = []
            for w in range(width):
                cell = cells[pointer]
                cell.row = h
                row.append(cell)
                pointer += 1
            rows.append(row)
        self.rows = rows

        # populate the columns
        start = 0
        for w in range(width):
            column = cells[start::width]
            for c in column: c.column = w
            columns.append(column)
            start += 1
        self.columns = columns

    def mutate(self):
        pass

    def back(self):
        pass

    def get(self, column, row):
        return self.columns[column][row]

    def _neighbors(self, column, row):
        """
        Return the 8 neighbors for a cell.
        Takes as input the row and column
        index for the given cell.
        """
        neighbor_columns = [column-1, column, column+1]
        neighbor_rows = [row-1, row, row+1]
        neighbors = []
        for c in neighbor_columns:
            for r in neighbor_rows:
                # make sure it doesn't exceed the boundaries of the board
                # and that it doesn't include the requested cell as a neighbor of itself
                if c >= 0 and r >= 0 and c < self.width and r < self.height and not (c == column and r == row):
                    cell = self.get(c,r)
                    neighbors.append(cell)
        return neighbors
        


class Cell:

    def __init__(self, alive, column, row, board):
        self.alive = alive
        self.board = board
        self.column = column
        self.row = row

    def neighbors(self):
        return self.board._neighbors(self.column, self.row)

    def __eq__(self, other):
        return self.alive == other

    def __repr__(self):
        return str(self.alive)

    

if __name__ == "__main__":
    pass
