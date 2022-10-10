def find_duplicate(nums):
    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] and nums[i] > 0:
            return nums[i]
    return False
