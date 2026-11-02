class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence_length = defaultdict(int)
        
        max_length = 0
        for num in nums: 
            if not sequence_length[num]:
                sequence_length[num] = sequence_length[num - 1] + sequence_length[num + 1] + 1
                sequence_length[num - sequence_length[num - 1]] = sequence_length[num]
                sequence_length[num + sequence_length[num + 1]] = sequence_length[num]
                max_length = max(max_length, sequence_length[num])
        
        return max_length