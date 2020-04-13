class Sum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def twoSum(self):
        temp = [val for val in self.nums if val <= self.target]
        indices = []

        for idx in range(len(temp)):
            for idy in range(idx + 1, len(temp)):
                tI = []
                if temp[idx] + temp[idy] == self.target:
                    tI.extend([idx, idy])
                    indices.append(tuple(tI))

        indices = sorted(indices, key=lambda x: x[1])
        return indices

nums = (1,5,10,15,20,30)
target = 50
sum = Sum(nums, target)
print(sum.twoSum())