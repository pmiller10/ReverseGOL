from game import Board

def test_board():
    cells = [1,1,1,0,0,0]
    height, width = 2,3
    board = Board(cells, height, width)
    assert board.columns[0] == [1,0]
    assert board.columns[1] == [1,0]
    assert board.columns[2] == [1,0]
    assert board.rows[0] == [1,1,1]
    assert board.rows[1] == [0,0,0]
    print 'test_board pass'

if __name__ == "__main__":
    test_board()
