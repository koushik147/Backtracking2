class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
         
        self.m = len(board) # creating for the length of board
        self.n = len(board[0]) # creating for the length of board of 0th index
        self.word = word
        self.board = board
        
        if len(board) > self.m*self.n: # if length of board is greater than m and n the return false
            return False
        
        self.dirs = [[0,1],[1,0],[0,-1],[-1,0]] # declaring the directions array
        
        for i in range(self.m): # run until the board and check the word of 0 is equal to board value then call the dfs function recursively
            for j in range(self.n):
                if self.word[0] == self.board[i][j]:
                    if self.dfs(i,j,0):
                        return True
                    
        return False
    
    def dfs(self,i,j,index):
        
        if index == len(self.word): # if index is equal to length of word
            return True
        
        if i<0 or i==self.m or j<0 or j==self.n or self.board[i][j] == "#": # if i is less than 0 and m and j is less than 0 and equal to n and board value equal to #
            return False
        
        if self.board[i][j] == self.word[index]: # if board value is equal to word of index
            self.board[i][j]="#" # setting board value to #
            for x,y in self.dirs: # for in directions
                nr = x+i
                nc = y+j
                if self.dfs(nr,nc,index): # if calling dfs function recursively with nr and nc then return true
                    return True
                
            self.board[i][j] = self.word[index] # set board value with word of index
        return False
            
            
            