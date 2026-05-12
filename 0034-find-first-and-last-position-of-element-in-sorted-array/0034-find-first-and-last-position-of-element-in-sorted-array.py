class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        right=-1
        left=-1
        for i in range(len(nums)):
            if(nums[i]==target):
                if right==-1:
                    right=i
                left=i
        return[right,left]
        