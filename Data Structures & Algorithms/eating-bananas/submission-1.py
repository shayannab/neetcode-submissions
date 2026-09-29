class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = max(piles)

        while l <= r:
            mid = (l + r) // 2
            
            # calculate total hours for k=mid
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid 
            
            if hours <= h:
                result = mid   # valid k, save it and try smaller
                r = mid - 1
            else:
                l = mid + 1    # too slow, try bigger k

        return result