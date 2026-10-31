class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_product = [0] * length
        right_product = [0] * length
        excluded_product = [0] * length

        left_product[0] = nums[0]

        for i in range(1, length): 
            left_product[i] = nums[i] * left_product[i - 1] 

        right_product[length - 1] = nums[length - 1] 

        for i in range(length - 2, 0, -1):
            right_product[i] = nums[i] * right_product[i + 1]

        excluded_product[0] = right_product[1]
        excluded_product[length - 1] = left_product[length - 2]
        for i in range(1, length - 1):
            excluded_product[i] = left_product[i - 1] * right_product[i + 1]

        return excluded_product

        