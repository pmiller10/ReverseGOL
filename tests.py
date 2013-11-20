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

def test_mutate():
    board.mutate()
    assert board.cells == [0, 1, 0, 0, 1, 0] # generation 2
    board.mutate()
    assert board.cells == [0, 0, 0, 0, 0, 0] # generation 3
    print 'test_mutate pass'

if __name__ == "__main__":
    test_board()
    test_cell()
    test_mutate()
