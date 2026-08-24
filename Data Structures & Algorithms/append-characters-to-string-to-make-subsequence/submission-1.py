class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        '''
        parameters: string s, string t.
        return: min number of characters
        Really asking: subsequence problem. Usually means two pointers.
        Constraints: 
        variables: L, R, and i pointers, numChar, 
        How to solve: Establish variables, create while loop which runs until end of t. L outside of while loop. R resets in for loop.
        '''
        
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t) - j