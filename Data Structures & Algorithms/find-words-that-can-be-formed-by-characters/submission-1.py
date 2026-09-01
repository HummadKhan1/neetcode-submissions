from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        for word in words:
            word_count = defaultdict(int)
            good = True
            for c in word:
                word_count[c] += 1
                if c not in count or word_count[c] > count[c]:
                    good = False
                    break
            if good:
                res += len(word)
        return res