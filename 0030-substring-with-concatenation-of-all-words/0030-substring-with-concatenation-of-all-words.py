class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word = defaultdict(int)
        for i in words:
            word[i]+=1
        substr_len = len(words)*len(words[0])
        word_len = len(words[0])
        res = []
        for i in range(len(s)-substr_len+1):
            seen = defaultdict(int)
            for j in range(i,i+substr_len,word_len):
                wo = s[j:j+word_len]
                if wo in word:
                    seen[wo]+=1
                    if seen[wo]>word[wo]:
                        break
                else:
                    break
            else:
                res.append(i)
        return res
        
        