class Board:

    def __init__(self, cells, height, width):
        # convert integers to cell objects
        cells = [Cell(c, None, None, self) for c in cells]
        total = height * width
        assert len(cells) == total

        # populate the rows
        rows = []
        pointer = 0
        for h in range(height):
            row = []
            for w in range(width):
                cell = cells[pointer]
                cell.row = h
                row.append(cell)
                pointer += 1
            rows.append(row)

        # populate the columns
        columns = []
        start = 0
        for w in range(width):
            column = cells[start::width]
            for c in column: c.column = w
            columns.append(column)
            start += 1

        self.rows = rows
        self.columns = columns
        self.cells = cells
        self.height, self.width = height, width

    def mutate(self):
        """
        Must set the next generation before mutating to it.
        Otherwise, you'll get dynamic evolutions where the mutations
        will vary based on which cells you started with.
        """
        for c in self.cells:
            c.set_next_generation()
        for c in self.cells:
            c.mutate()

    def back(self):
        pass

    def get(self, column, row):
        return self.columns[column][row]

    def neighbors(self, column, row):
        """
        Return the 8 neighbors for a cell.
        Takes as input the row and column
        index for the given cell.
        """
        neighbor_columns = [column-1, column, column+1]
        neighbor_rows = [row-1, row, row+1]

        # make sure they don't exceed the boundaries of the board
        neighbor_columns = [c for c in neighbor_columns if c >= 0 and c < self.width]
        neighbor_rows = [r for r in neighbor_rows if r >= 0 and r < self.height]

        neighbors = []
        for c in neighbor_columns:
            for r in neighbor_rows:
                # make sure that it doesn't include the requested cell as a neighbor of itself
                if not (c == column and r == row):
                    cell = self.get(c,r)
                    neighbors.append(cell)
        return neighbors

    def __repr__(self):
        return "\n".join([str(r) for r in self.rows])
        


class Cell:

    def __init__(self, alive, column, row, board):
        self.alive = alive
        self.next_generation = alive
        self.board = board
        self.column = column
        self.row = row

    def neighbors(self):
        return self.board.neighbors(self.column, self.row)

    def living_neighbors(self):
        living = 0
        for n in self.neighbors():
            if n.alive: living += 1
        return living

    def set_next_generation(self):
        living = self.living_neighbors()
        if self.alive:
            if living <= 1:
                self.next_generation = 0
            elif living >= 4:
                self.next_generation = 0
        elif not self.alive:
            if living >= 3:
                self.next_generation = 1

    def mutate(self):
        self.alive = self.next_generation

    def __eq__(self, other):
        return self.alive == other

    def __repr__(self):
        return str(self.alive)
