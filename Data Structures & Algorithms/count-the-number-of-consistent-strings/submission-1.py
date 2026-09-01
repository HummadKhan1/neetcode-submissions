from collections import Counter
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        '''
        parameters: distinct char str: allowed, arr of str: words.
        returns: NUMBER OF consistent strings in the arrau words.
        Really asking: Hashmap Counter proble. Check if the characters in words[i] exist in count_allowed and count_allowed[i] > words[i].
        Constraints: 
        '''
        count = Counter(allowed)
        res = 0

        for word in words:
            consistent = True
            unique = set(word)
            for u in unique:
                if u not in count:
                    consistent = False
                    break
            if consistent:
                res += 1
        return res