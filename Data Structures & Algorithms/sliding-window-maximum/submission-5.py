

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()  # store indices
        res = []
        l = 0

        for r in range(len(nums)):
            # 1. Maintain monotonic decreasing order of values
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # 2. Remove indices that are out of bounds of the current window
            if l > q[0]:
                q.popleft()

            # 3. Add to result once the window has reached size k
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

        return res