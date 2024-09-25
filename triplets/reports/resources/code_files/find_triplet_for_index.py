def find_triplet_for_index(nums, i, result):
    l, r = i + 1, len(nums) - 1
    while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s > 0:
            r -= 1
        elif s < 0:
            l += 1
        else:
            result.append((nums[i], nums[l], nums[r]))
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            l += 1
            r -= 1
