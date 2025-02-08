# 8. Check if list contains 007 in order
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            print("Spy game: True")
            return True
    print("Spy game: False")
    return False
