class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.result = [] # definng the result array
        self.backtrack(s,0,[]) # calling the backtrack function with arguments
        return self.result # returning the result array
    
    def backtrack(self,s,pivot,path): 
        if pivot == len(s): # if pivot is equal to length of string
            self.result.append(path[:]) # appending the path array in the result array by shallow copying
            return 
        
        for i in range(pivot,len(s)):
            subStr = s[pivot:i+1] # Creating the sub string  from pivot to i+1
            if self.isPalindrome(subStr): # if substr is palindrome then append the substr in the path
                path.append(subStr)
                self.backtrack(s,i+1,path) # recursively calling the backtrack function with i+1
                path.pop() # popping the path array
                
    def isPalindrome(self,s):
        left = 0 #. setting the left pointer in start of the array
        right = len(s)-1 # setting the right pointer in the end of the array
        
        while left<right: # run until left is lesser than right
            if s[left] == s[right]: # if left is equal to right
                left+=1 # increment the left pointer by 1
                right-=1 # decrement the right pointer by 1
            else:
                return False
        
        return True