class RandomizedSet:

    def __init__(self):
        self.data = []
        self.data_map = {}

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False
        i = self.data_map[val]
        self.data_map[self.data[-1]]=i
        del self.data_map[val]
        self.data[i] = self.data[-1]
        self.data.pop()
        return True

    def getRandom(self) -> int:
        ind = random.randint(0,len(self.data)-1)
        return self.data[ind]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()