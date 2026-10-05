class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for y in range(i+1,len(nums)):
                if (nums[y] + nums[i]) == target:
                    return [i,y]
        return []