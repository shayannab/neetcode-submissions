class Solution:
    def trap(self, height: List[int]) -> int:
        prefix= [0]*len(height)
        suffix= [0]*len(height)
        water = 0
        for i in range (0,len(height)):
            prefix[i] = max(prefix[i-1] if i > 0 else 0, height[i])
        for j in range(len(height)-1, -1, -1):
            suffix[j] = max(suffix[j+1] if j < len(height)-1 else 0, height[j])
        for i in range(len(height)):
            h = min(prefix[i], suffix[i]) - height[i]
            if h > 0: water += h
        return water