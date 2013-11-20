class Board:

    def __init__(self, cells, height, width):
        total = height * width
        assert len(cells) == total
        rows, columns = [], []

        # populate the rows
        pointer = 0
        for h in range(height):
            row = []
            for w in range(width):
                row.append(cells[pointer])
                pointer += 1
            rows.append(row)
        self.rows = rows

        # populate the columns
        start = 0
        for w in range(width):
            column = cells[start::width]
            columns.append(column)
            start += 1
        self.columns = columns

    def mutate(self):
        pass

    def back(self):
        pass

if __name__ == "__main__":
    pass
