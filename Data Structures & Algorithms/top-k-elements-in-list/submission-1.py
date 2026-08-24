class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize hashmap
        num_dict = {}
        # create empty lists equal to length of nums + 1
        freq = [[] for i in range(len(nums) + 1)]
        result = []
        # count number of occurences of each number and put in hashmap
        for n in nums:
            num_dict[n] = num_dict.get(n, 0)+1
        # swap key and values and put them in freq list
        for key, value in num_dict.items():
            freq[value].append(key)
        #iterating backwards append from freq list into result list
        for i in range(len(freq)-1,0,-1):
            for value in freq[i]:
                result.append(value)
                if len(result) == k:
                    return result
        #stop when length of result list is equal to k