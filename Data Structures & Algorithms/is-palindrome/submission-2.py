class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = "".join(filter(lambda x : x.isalpha() or x.isnumeric() , s)).lower().split(" ")
        for word in words:
            if word[::-1] in words:
                return True
        return False