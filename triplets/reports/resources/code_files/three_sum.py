def three_sum(nums):
    modified_nums = modify_array(nums)
    print("Modified array:", modified_nums)
    result = []
    for i in range(len(modified_nums) - 2):
        if i > 0 and modified_nums[i] == modified_nums[i - 1]:
            continue
        find_triplet_for_index(modified_nums, i, result)
    return result
