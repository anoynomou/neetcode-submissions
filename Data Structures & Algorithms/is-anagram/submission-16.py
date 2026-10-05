class Solution:
    def isAnagram(self,str_x,str_t):
        if len(str_x) == len(str_t):
            for x in str_x:
                if str_x.count(x) == str_t.count(x):
                    pass
                else:
                    return False
            return True
        return False