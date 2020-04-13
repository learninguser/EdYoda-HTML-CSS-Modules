class SumEqualsZero:
    def __init__(self, nums):
        self.nums = nums

    def threeSum(self, nums):
        ans = []
        for idx in range(len(nums)):
            for idy in range(idx + 1 , len(nums)):
                for idz in range(idy + 1, len(nums)):
                    if nums[idx] + nums[idy] + nums[idz] == 0:
                        ans.append([nums[idx], nums[idy], nums[idz]])
        return ans

threesum = SumEqualsZero([-2,-1,0,1,2,3,5])
print(threesum.threeSum([0]))