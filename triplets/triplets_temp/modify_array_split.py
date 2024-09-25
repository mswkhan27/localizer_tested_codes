def modify_array(nums):
    c[14] += 1
    nums.sort()
    i = 0
    while i < len(nums):
        c[1] += 1
        if i > 0 and nums[i] == nums[i - 1]:
            c[2] += 1
            if nums[i] >= 0:
                c[3] += 1
                nums[i] += 1
            else:
                c[4] += 1
                nums[i - 1] -= 3 #mistake
            i = 0
            nums.sort()
        else:
            c[5] += 1
            i += 1
    return nums
