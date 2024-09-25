from src.utils import Count 

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
