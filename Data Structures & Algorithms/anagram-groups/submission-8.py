class Solution:

    
    def groupAnagrams(self,strs):
        sortedwords_words = {}

        for word in strs:
            key = str(sorted(word))
            if sortedwords_words.get(key) is not None:
                sortedwords_words[key].append(word)
            else:
                sortedwords_words[key] = [word]
        return list(sortedwords_words.values())