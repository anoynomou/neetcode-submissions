class Solution:

    
    def groupAnagrams(self,strs):
        sortedwords_words = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            sortedwords_words[key].append(word)
        return list(sortedwords_words.values())