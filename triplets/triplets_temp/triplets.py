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

def three_sum(nums):
    modified_nums = modify_array(nums)
    print("Modified array:", modified_nums)
    result = []
    for i in range(len(modified_nums) - 2):
        if i > 0 and modified_nums[i] == modified_nums[i - 1]:
            continue
        find_triplet_for_index(modified_nums, i, result)
    return result

