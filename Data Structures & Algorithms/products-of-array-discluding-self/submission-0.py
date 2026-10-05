class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    #multilpy all other nums except current index in i 
                    product *= nums[j]
            res.append(product)
        return res
                