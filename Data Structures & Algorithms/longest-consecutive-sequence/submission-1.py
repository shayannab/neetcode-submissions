class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start=[]
        longest = 0
        set_nums= set(nums)
        for i in set_nums:
            if i-1 not in set_nums:
                start.append(i)
        for s in start:
            length = 1
            current = s
            while current + 1 in set_nums:
                current += 1
                length += 1
            if length  > longest:
                longest = length
        return longest            
     
