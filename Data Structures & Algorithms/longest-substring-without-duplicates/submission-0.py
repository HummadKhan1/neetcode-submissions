class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        L = 0
        longest_length = 0
        longest_substring = ""
        maxL, maxR = 0,0
        for R in range(len(s)):
            if s[R] in char_dict:
                L = max(L, char_dict[s[R]]+1)
            char_dict[s[R]] = R
            if R-L+1 > longest_length:
                longest_length = R-L+1
                maxL,maxR = L, R
        print(s[maxL:maxR])
        return longest_length