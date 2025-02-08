# 10. Get unique elements from a list
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    print(f"Unique elements: {unique_list}")
    return unique_list