def three_sum(nums):
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
