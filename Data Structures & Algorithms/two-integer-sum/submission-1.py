class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for index, num in enumerate(nums):
            pos[num] =  index

        for index, num in enumerate(nums):
            match = target - num

            try:
                if pos[match] != index:
                    return [index, pos[match]]
            except KeyError:
                continue