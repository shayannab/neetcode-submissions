class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):       
            seen = set()
            for j in range(9):   
                val = board[i][j]
                if val == ".":    
                    continue
                if val in seen:
                    return False
                seen.add(val)
        for j in range(9):
            seen=set()
            for i in range(9):
                val= board[i][j]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)  
        for box_row in range(3):      
            for box_col in range(3):  
                seen = set()
                for i in range(3):    
                    for j in range(3): 
                        val = board[box_row*3 + i][box_col*3 + j]    
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)      
        return True