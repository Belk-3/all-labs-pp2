# 7. Check if list contains a 3 next to a 3
def has_33(nums):
    result = any(nums[i] == 3 and nums[i + 1] == 3 for i in range(len(nums) - 1))
    print(f"Has 33: {result}")
    return result