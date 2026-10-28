class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        count = [[] for i in range(len(nums) + 1)]
        for num, fre in freq.items():
            count[fre].append(num)
        
        ans = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                ans.append(num) 

                if len(ans) == k:
                    return ans