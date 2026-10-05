class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicate = False
        new_list = []
        for num in nums:
            if num not in new_list:
                new_list.append(num)
            else:
                has_duplicate = True
                break
        return has_duplicate