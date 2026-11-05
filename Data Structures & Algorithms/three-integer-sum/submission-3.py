class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        solutions = set()
        nums.sort()

        for i in range(length):
             left = i + 1
             right = length - 1

             while left < right:
                if nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                else:
                    solution = (nums[left], nums[i], nums[right])

                    solutions.add(solution)
                    left += 1
                    right -= 1
        
        return [list(solution) for solution in solutions]