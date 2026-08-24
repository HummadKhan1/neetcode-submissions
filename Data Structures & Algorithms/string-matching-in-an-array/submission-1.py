class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        '''
        parameters: arr of strings: words.
        return: arr of substrings or an empty arr.
        Really asking: 
        '''
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res
         