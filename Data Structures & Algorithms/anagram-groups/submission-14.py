class Solution:

    
    def groupAnagrams(self,strs):
        sortedwords_words = {}

        for word in strs:
            key = tuple(sorted(word))
            if key in sortedwords_words:
                sortedwords_words[key].append(word)
            else:
                sortedwords_words[key] = [word]
        return list(sortedwords_words.values())