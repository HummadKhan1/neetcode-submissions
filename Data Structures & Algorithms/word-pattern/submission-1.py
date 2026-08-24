class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_dict = {}
        word_dict = {}

        words = s.split()
        if len(words) != len(pattern):
            return False
        print(words)
        for i in range(len(words)):
            if pattern[i] in p_dict and words[i] in word_dict:
                if p_dict[pattern[i]] != words[i] or word_dict[words[i]] != pattern[i]:
                    return False
            else:
                if pattern[i] in p_dict and words[i] not in word_dict:
                    return False
                if pattern[i] not in p_dict and words[i] in word_dict:
                    return False
                p_dict[pattern[i]] = words[i]
                word_dict[words[i]] = pattern[i]

        return True