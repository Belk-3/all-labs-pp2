# 1. Convert grams to ouncesa
a = int(input())
def grams_to_ounces(grams):
    result = 28.3495231 * grams
    print(f"{grams} grams is {result} ounces")
    return result
grams_to_ounces(a)