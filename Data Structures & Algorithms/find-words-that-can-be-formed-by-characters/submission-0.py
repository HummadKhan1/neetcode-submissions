from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        '''
        parameters: arr of string: words, string: chars.
        return: sum of lengths of all good strings.
        '''
        chars_dict = Counter(chars)
        res = 0
        for word in words:
            word_count = Counter(word)
            unique = set(word)
            possible = True
            for c in unique:
                if c not in chars_dict:
                    possible = False
                    break
                else:
                    if chars_dict[c] - word_count[c] < 0:
                        possible = False
                        break
            if possible == True:
                res += len(word)
        return res