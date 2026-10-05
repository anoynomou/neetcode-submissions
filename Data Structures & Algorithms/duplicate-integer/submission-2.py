class Solution:
    def hasDuplicate(self,numbers: list):
        second_array = []
        for num in numbers:
            if num in second_array:
                return True
            else:
                second_array.append(num)
        return False

