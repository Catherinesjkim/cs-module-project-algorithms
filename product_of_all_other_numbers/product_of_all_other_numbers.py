'''
Input: a List of integers
Returns: a List of integers
'''
#3 - Module 3: A First-Pass Solution
# Naive solution: Create 2 extra space, i.e. 2 extra arrays to store the product of all the array elements from start, up to that index and another array to store the product of all the array elements from the end of the array to that index 
# To get the product excluding that index, multiply the prefix product up to index i-1 with the suffix product up to index i+1 
# Solve it without division operator in O(N) time
# fn to print product array for a given array 

# we can exclude the nums[j] (where j != i) from list first, then get the product of the rest
from functools import reduce
def product_of_all_other_numbers(arr):
    return [ reduce(lambda x, y: x * y, arr[:i] + arr[i+1:]) for i in range(len(arr))]


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
