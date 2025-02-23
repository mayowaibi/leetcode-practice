class RandomizedSet:
    # TC: O(1) for each op, SC: O(2n) for arr and map = O(n)
    def __init__(self):
        self.valueToIndex = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.valueToIndex:
            return False
        
        self.nums.append(val)
        self.valueToIndex[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valueToIndex:
            return False
        
        idx = self.valueToIndex[val]
        lastVal = self.nums[-1]

        # swap val to be removed with last val in arr
        self.nums[idx] = lastVal
        self.nums[-1] = val

        # update idx of last val in hashmap
        self.valueToIndex[lastVal] = idx

        # remove val from arr and hashmap
        self.nums.pop()
        del self.valueToIndex[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()