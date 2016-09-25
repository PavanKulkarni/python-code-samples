def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        new_board = []
        for row in board:
             new_board.append(list(row))
        board = new_board
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                tmp = board[i][j]
                board[i][j] = 'T'
                if isValid(i, j, board, tmp):
                    board[i][j] = tmp
                else:
                    return False
        return True
        
def isValid(x, y, board, tmp):
    for i in range(9):
        if board[i][y] == tmp:
            return False
    for i in range(9):
        if board[x][i] == tmp:
            return False
    for i in range(3):
        for j in range(3):
            print x, y
            if board[(x/3)*3+i][(y/3)*3+j] == tmp:
                return False
    return True


if __name__=='__main__':
    board = [".4.......","..8......","...1..7..",".........","...3...6.",".....6.9.","....1....","......2..","...8....."]
    for i in board:
       print i
    print isValidSudoku(board)
