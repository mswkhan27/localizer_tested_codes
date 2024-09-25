def modify_array(nums):
    nums.sort()
    i = 0
    while i < len(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            if nums[i] >= 0:
                nums[i] += 1
            else:
                nums[i - 1] -= 3 #mistake
            i = 0
            nums.sort()
        else:
            i += 1
    return nums
