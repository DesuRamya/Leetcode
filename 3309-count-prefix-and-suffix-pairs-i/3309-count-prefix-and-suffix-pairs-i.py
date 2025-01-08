class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1,str2):
            if str2.startswith(str1) and str2.endswith(str1):
                return True
            return False
        c,n=0,len(words)
        for i in range(n):
            for j in range(i+1,n):
                s1=words[i]
                s2=words[j]
                if len(words[i])>len(words[j]):
                    continue
                if isPrefixAndSuffix(words[i],words[j]):
                    c+=1
        return c