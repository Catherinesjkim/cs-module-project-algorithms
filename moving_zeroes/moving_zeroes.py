'''
Input: a List of integers
Returns: a List of integers
'''
#2 - Module 3: A First-Pass Solution
# traverse the given array 'arr' from left to right
# while traversing, maintain count of non-zero elements in array
# let the count be 'count' 
# for every non-zero arr[i], put the element at 'arr[count]' and increment 'count'. 
# after complete traversal, all non-zero elements have already been shifted to front end and 'count' is set as index of first 0
# now all we need to do is that run a loop which makes all elements zero from 'count' till end of the array

# function which pushes all zeros to the end of an array
def moving_zeroes(arr):
    # count stores index of next avaialable position
    zero_counter = 0 # Count for non-zero elements
    mock_arr = arr.copy()
    
    if len(arr) == 0:
        return arr
    
    # traverse the array - access each and every element of the array for a specific purpose like counting
    for i in mock_arr:
        # if current element is non-zero,
        if i ==0:
            # then replace the element at index 'count' with this element
            # here count is incremented
            arr.remove(i)
            arr.append(i)
            zero_counter += 1
            
    return arr


# move all zeros present in the list to the end
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
