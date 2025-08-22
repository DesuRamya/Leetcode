class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        length=len(target)
        steps=target[0]
        for i in range(1,length):
            if target[i]>target[i-1]:
                steps+=abs(target[i]-target[i-1])
            print(steps)
        return steps