class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sub_result = [] 

        words_structure = []

        for i in range(len(strs)):
            # sclect word , strs[i]
        
            words_structure.append(self.resturcture(strs[i]))
        
        # match word structure with other word structure
        for  _word  in  words_structure:

            temp_word = []
            for word_s in strs:

                if _word == self.resturcture(word_s):
                    temp_word.append(word_s)
        
            if temp_word not in sub_result:
                sub_result.append(temp_word )
        return sub_result

    def resturcture(self,word):
        w_struct = {}

        for char in word:
            if char in w_struct:
                w_struct[char] += 1
            else:
                w_struct[char] = 1
        return w_struct