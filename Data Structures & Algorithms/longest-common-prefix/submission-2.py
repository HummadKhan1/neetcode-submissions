class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        parameters: arr of strings strs.
        return: longest common prefix of all the strings or empty string if None.
        Really asking: sort the array. compare first and last elements only. 
        Constraints: could only be one element in arr. Element could be empty.
        Variables: sorted_s, first_element, last_element, prefix.
        '''
        if len(strs) < 2:
            return strs[0]
        sorted_s = sorted(strs)
        first_element = sorted_s[0]
        last_element = sorted_s[-1]
        prefix = ""

        if first_element > last_element:
            bigger = first_element
            smaller = last_element
        else:
            bigger = last_element
            smaller = first_element

        for i in range(len(first_element)):
            if bigger[i] == smaller[i]:
                prefix += bigger[i]
            else:
                break
        return prefix