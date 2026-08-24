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
        
        s_list = list(s)
        t_list = list(t)
        
        L, i = 0, 0
        while i < len(t_list):
            for R in range(len(s_list)):
                if s_list[R] == t_list[i]:
                    i += 1
                    L = R+1
                if i >= len(t_list):
                    break
            return len(t) - i
        return 0