class Solution:
    def bitwiseComplement(self, n: int) -> int:
        nb=bin(n)[2:]
        res=""
        for i in nb:
            if i=="0":
                res+="1"
            else:
                res+="0"
        return int(res,2)