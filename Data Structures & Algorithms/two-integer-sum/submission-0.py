class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            # All the nums , nums[i]
            for j in range(len(nums)):
                # All the nums , nums[i]

                #Check if it matchs the condition 
                if nums[i] + nums[j] == target and i != j:
                    result = [j,i]
        return result
