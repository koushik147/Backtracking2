#TimeComplexity: O(n)
#SpaceComplexity: O(n)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [[False for i in range(n)] for j in range(n)] # creating the board with list comprehension
        self.result = [] # defining the result array
        self.backtrack(board,0) # calling recursively the backtrack function
        return self.result # returning the result array
 

    def backtrack(self,board,r):
        #base
        if r == len(board): # if r is equal to length of board
            #build output string 
            row = [] # creating the empty array
            for i in range(len(board)):
                stringBuilder = "" # creating variable for string building
                for j in range(len(board)):
                    if board[i][j]: # if there is a element in the board then add that queen to string builder
                        stringBuilder+="Q"
                    else:
                        stringBuilder+="." # else add the dot '.'
                row.append(stringBuilder) # appending the string builder in the row array
            self.result.append(row) # appending the row array in the result array
            return

        #logic
        for c in range(len(board)):
            if self.isSafe(board,r,c): # if checking to place a queen at a position is safe then return true
                board[r][c] = True

                self.backtrack(board,r+1) # calling the function recursively with r+1

            board[r][c] = False # else return false
        #return



    def isSafe(self,board,i,j):
        
        for r in range(0,i):
            if board[r][j]: # if board [i][j] is true then return false
                return False

        r = i # setting the row pointer to i
        c = j # setting the column pointer to j
        
        while r>=0 and c>=0: #left diagonal
            if board[r][c]:
                return False
            r-=1 # decrementing the r pointer by 1
            c-=1 # decrementing the c pointer by 1

        r = i # setting the row pointer to i
        c = j # setting the column pointer to j
        
        while r>=0 and c<len(board): #right diagonal
            if board[r][c]:
                return False
            r-=1 # decrementing the r pointer by 1
            c+=1 # incrementing the c pointer by 1

        return True
            
