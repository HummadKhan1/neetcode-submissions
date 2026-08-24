class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # traverse backwards
        # keep track of biggest number
        # replace current number with biggest number.
        new_arr = arr[:]
        biggest_num = -1
        for i in range(len(arr)-1,-1,-1):
            if i == len(arr)-1:
                new_arr[i] = biggest_num
                biggest_num = arr[i]
                continue
            new_arr[i] = biggest_num
            if arr[i] > biggest_num:
                biggest_num = arr[i]
        return new_arr