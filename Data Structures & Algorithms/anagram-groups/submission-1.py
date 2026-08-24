class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}

        for s in strs:
            sorted_word = str(list(sorted(s)))
            if sorted_word not in group_dict:
                group_dict[sorted_word] = [s]
            else:
                group_dict[sorted_word].append(s)
        return list(group_dict.values())