'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# 4 - Module 3: A First-Pass Solution
# Find the maximum for each and every contiguous subarray of size k

# Approach: run a nested loop, the outer loop which will mark the starting point of the subarray of length k, the inner loop will run from the starting index to index+k, k elements from starting index and print the maximum element among these k elements

# Algo:
# 1. Create a nested loop, the outer loop from starting index to n-k th elements. The inner loop will run for k iterations
# 2. Create a variable to store the maximum of k elements traversed by the inner loop
# 3. Find the maximum of k elements traversed by the inner loop
# 4. Print the maximum element in every iteration of outer loop

# method to find the maximum for each and every contiguous subarray of s of size k
def sliding_window_max(arr, k):
    max = 0
    x = []
    # create a nested loop, the outer loop from starting index to nums - k th elements
    for i in range(len(arr) - k + 1): 
        max = arr[i]
        # The inner loop will run for k iterations
        # create a variable to store the maximum of k elements traversed by the inner loop
        for j in range(1, k):
            if arr[i + j] > max:
                # find the maximum of k elements traversed by the inner loop
                max = arr[i + j]
        # print the maximum element in every iteration of outer loop
        x.append(max)
        
    return x

# Driver method
if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
