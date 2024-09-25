from src.utils import Count 

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
