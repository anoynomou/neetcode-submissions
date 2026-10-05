class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        _board_row = [[] for x in range (9)]
        _board_column= [[] for x in range (9)]
        _square = [[[] for i in range(3)] for i in range(3) ]
        for column in range(9):
            for row in range(9):
                # row by row
                r_value = board[column][row]
                if r_value in _board_row[column]:
                    return False   
                else:
                    if r_value.isdigit():
                        _board_row[column].append(r_value)
                         # check 3x3 box for duplicates 
                        if board[column][row] not in _square[column//3][row//3]:
                            _square[column//3][row//3].append(board[column][row])
                        else:
                            return False
                # column by column
                c_value = board[row][column]
    
                if c_value in _board_column[column]:
                    return False
                else:
                    if c_value.isdigit():
                        _board_column[column].append(c_value)
    
        return True