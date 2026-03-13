from functools import reduce

def demo_map(nums):
    """Return list of squares of nums using map."""
    return list(map(lambda x: x * x, nums))

def demo_filter(nums):
    """Return list of even numbers using filter."""
    return list(filter(lambda x: x % 2 == 0, nums))
 
def demo_sum_of_squares(nums):
    """Return sum of squares of nums using map and reduce."""
    return reduce(lambda a, b: a + b, map(lambda x: x * x, nums), 0)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Original:", numbers)
    print("Squares (map):", demo_map(numbers))
    print("Evens (filter):", demo_filter(numbers))
    print("Sum of squares:", demo_sum_of_squares(numbers))
