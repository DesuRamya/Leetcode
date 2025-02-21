class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        no=(n//2)+1 if n%2!=0 else n//2 
        ne=(n//2)
        mo=(m//2)+1 if m%2!=0 else m//2
        me=m//2
        # print(ne,no,me,mo)
        return no*me+ne*mo