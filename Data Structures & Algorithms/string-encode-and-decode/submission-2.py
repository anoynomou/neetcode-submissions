class Solution:

    def encode(self, strs: List[str]) -> str:
        PRIME_NUMBER =9973
        if len(strs) == 0 : return "x0"
        encoded_str  = ""
        for i in range(len(strs)):
            word = strs[i]
            _enc_word = ""
            for j in range(len(word)):
                char = word[j]
                _enc_word += str(ord(char)*PRIME_NUMBER)
                _enc_word += ","  if j != len(word)-1 else ""
                

            encoded_str += _enc_word
            encoded_str += "%"  if i != len(strs)-1 else ""
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        PRIME_NUMBER =9973
        enc_strs = [ x  for x in s.split("%")]
        result =[]
        if s == 'x0': return []
        for x in enc_strs:
            _dec_word = x.split(",")
            word = ""
            for y in _dec_word:
                if len(y) > 0:
                    word+= chr(int(y)//PRIME_NUMBER)
                else:
                    word += ""
            result.append(word)   
        
        return result