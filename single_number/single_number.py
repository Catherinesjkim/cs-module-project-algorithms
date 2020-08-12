'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
#1 - Module 3: A First-Pass Solution
# check every element if it appears once or not. 
# Once an element with a single occurrence is found, return it. Time complexity of this solution is O(n^2).

# add each number once and multiply the sum by 2, we will get twice the sum of each element of the array.
# then we will subtract the sum of the whole array from the twice_sum and get the required number (which appears once in the array).
# Array []: [a, a, b, b, c, c, d]
# Mathematical Equation: 2 * (a + b + c + d) - (a + a + b + b + c + c + d)
# Pseudocode: 2*(sum_of_array_without_duplicates) - (sum_of_array)

# set does not contian any dupe element, so we will be using the set
# find the element that only appears once
def single_number(arr):
    # applying the formula 
    return 2 * sum(set(arr)) - sum(arr)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
