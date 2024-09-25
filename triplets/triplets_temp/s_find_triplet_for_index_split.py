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
