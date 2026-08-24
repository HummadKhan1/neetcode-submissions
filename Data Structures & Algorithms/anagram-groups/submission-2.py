class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        parameters: arr of strings strs.
        return: arr.
        Really asking: grouping problem. hashmap used often in these cases.
        Constraints: 
        variables: group_dict, res.
        '''
        group_dict = {}

        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in group_dict:
                group_dict[sorted_s].append(s)
            else:
                group_dict[sorted_s] = [s]
        new_list = list(group_dict.values())
        return new_list