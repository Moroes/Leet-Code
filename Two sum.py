from typing import *


class Solution():
    def twoSumm(nums: List[int], target: int) -> List[int]:
        for el in enumerate(nums):
            temp = target - el[1]
            for i in range(el[0] + 1, len(nums)):
                if nums[i] == temp:
                    return [el[0], i]


x = [1, 3, 5, 2, 4, 9]
target = 7

print(Solution.twoSumm(x, target))