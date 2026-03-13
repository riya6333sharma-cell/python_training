from typing import List
def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
print(contains_duplicate([1,2,3,4,5,1]))  
print(contains_duplicate([1,2,3,4,5]))