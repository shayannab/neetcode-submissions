class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]

        while l <= r:
            # if this portion is already sorted, leftmost is minimum
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            mid = (l + r) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1   # min is in right half
            else:
                r = mid - 1   # min is in left half

        return result