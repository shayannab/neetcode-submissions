class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r=0, len(numbers)-1 
        currentSum =0
        while l<r:
            currentSum= numbers[l]+numbers[r]
            if currentSum==target:
                return [l+1,r+1]
            elif currentSum < target:
                l=l+1
            else:
                r=r-1