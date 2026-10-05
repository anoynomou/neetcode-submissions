class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        for f in range(len(nums)):
            for s in range(f+1,len(nums)):
                for t in range(s+1,len(nums)):
                    data =sorted([nums[f],nums[s],nums[t]])
                    if sum(data) ==0:
                        if data not in results :
                            results.append(data)
                    
        return results