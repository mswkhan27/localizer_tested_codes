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
c[15] += 1
l, r = i + 1, len(nums) - 1
while l < r:
    c[6] += 1
    s = nums[i] + nums[l] + nums[r]
    if s > 0:
        c[7] += 1
        r -= 1
    elif s < 0:
        c[8] += 1
        l += 1
    else:
        c[9] += 1
        result.append((nums[i], nums[l], nums[r]))
        while l < r and nums[l] == nums[l + 1]:
            c[10] += 1
            l += 1
        while l < r and nums[r] == nums[r - 1]:
            c[11] += 1
            r -= 1
        l += 1
        r -= 1
c[16] += 1
modified_nums = modify_array(nums)
print("Modified array:", modified_nums)
result = []
for i in range(len(modified_nums) - 2):
    c[12] += 1
    if i > 0 and modified_nums[i] == modified_nums[i - 1]:
        c[13] += 1
        continue
    find_triplet_for_index(modified_nums, i, result)
return result
