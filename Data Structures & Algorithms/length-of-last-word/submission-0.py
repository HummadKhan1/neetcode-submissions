class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_str = s[:]
        new_str = new_str.lstrip().rstrip()
        new_list = new_str.split()

        last_word = new_list[-1]
        print(last_word)
        return len(last_word)