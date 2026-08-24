class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest_element = -1

        new_arr = arr[:]

        for i in range(len(arr)-1,-1,-1):
            temp = new_arr[i]
            new_arr[i] = biggest_element
            if temp > biggest_element:
                biggest_element = temp
        return new_arr