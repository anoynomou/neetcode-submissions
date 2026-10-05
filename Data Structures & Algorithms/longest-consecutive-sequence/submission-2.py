class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        long_seq = 0 
        for num in nums:
            value = num
            rng = 1

            for i in range(len(nums)):
                value += 1
                if rng > long_seq:
                    long_seq = rng

                if value  in nums:
                    rng += 1 
                else:
                    break

        return long_seq
        