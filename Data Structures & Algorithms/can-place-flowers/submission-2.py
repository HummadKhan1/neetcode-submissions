class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_list = [0] + flowerbed + [0]

        for i in range(1,len(new_list)-1):
            if new_list[i] == 0 and new_list[i-1] == 0 and new_list[i+1] == 0:
                new_list[i] = 1
                n -= 1
        if n <= 0:
            return True
        return False