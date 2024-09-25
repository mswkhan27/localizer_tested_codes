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

def find_triplet_for_index(nums, i, result):
    Count.incC(15)
    l, r = i + 1, len(nums) - 1
    while l < r:
        Count.incC(6)
        s = nums[i] + nums[l] + nums[r]
        if s > 0:
            Count.incC(7)
            r -= 1
        elif s < 0:
            Count.incC(8)
            l += 1
        else:
            Count.incC(9)
            result.append((nums[i], nums[l], nums[r]))
            while l < r and nums[l] == nums[l + 1]:
                Count.incC(10)
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                Count.incC(11)
                r -= 1
            l += 1
            r -= 1

def three_sum(nums):
    Count.incC(16)
    modified_nums = modify_array(nums)
    print("Modified array:", modified_nums)
    result = []
    for i in range(len(modified_nums) - 2):
        Count.incC(12)
        if i > 0 and modified_nums[i] == modified_nums[i - 1]:
            Count.incC(13)
            continue
        find_triplet_for_index(modified_nums, i, result)
    return result

