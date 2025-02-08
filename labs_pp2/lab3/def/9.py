# 9. Compute volume of a sphere
import math
def sphere_volume(radius):
    result = (4/3) * math.pi * radius**3
    print(f"Volume of sphere with radius {radius}: {result}")
    return result
