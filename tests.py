from game import Board, Cell

cells = [1,1,1,0,0,0]
height, width = 2,3
board = Board(cells, height, width)

def test_board():
    assert board.columns[0] == [1,0]
    assert board.columns[1] == [1,0]
    assert board.columns[2] == [1,0]
    assert board.rows[0] == [1,1,1]
    assert board.rows[1] == [0,0,0]
    print 'test_board pass'

def test_cell():
    living = Cell(1, None, 0, 0)
    dead = Cell(0, None, 0, 0)
    assert living.alive
    assert not dead.alive
    cell = board.get(1,1)
    assert cell.neighbors() == [1, 0, 1, 1, 0]
    print 'test_cell pass'

if __name__ == "__main__":
    test_board()
    test_cell()
