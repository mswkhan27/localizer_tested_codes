from src.utils import Count 

def modify_array(nums):
    Count.incC(14)
    nums.sort()
    i = 0
    while i < len(nums):
        Count.incC(1)
        if i > 0 and nums[i] == nums[i - 1]:
            Count.incC(2)
            if nums[i] >= 0:
                Count.incC(3)
                nums[i] += 1
            else:
                Count.incC(4)
                nums[i - 1] -= 3 #mistake
            i = 0
            nums.sort()
        else:
            Count.incC(5)
            i += 1
    return nums
