class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        freq = sorted(counts, key=lambda x: counts[x], reverse=True)
        return freq[:k]