'''
Input: an integer
Returns: an integer
Fibonacci sequence: 
'''
#5 - Module 3: A First-Pass Solution

# Empty the Most Jars Algo: the monster reduces the number of distinct jars by as many as he can for each move
# Binary Algo: the monster takes 2^k cookies from all jars that contain at least 2^k cookies for k as large as possible

# Plan - UPER
# N = set of the numbers of the cookies in the jars
# the Cookie Monster number of N, CM(N), is the minimum number of moves Cookie Monster must use to empty all of the jars in N
# CM(N) = R  - Cookie Monster folows an optimal procedure
# after he performs move R, all jars are empty
# therefore, each jar may be represented as the sum of some moves
# For all |n| = m, [log2(m+1) <= CM(N) <= m

# 1. we challenge our monster to empty a set of jars containing cookies in the Fibonacci sequence Xn+2= Xn+1 + Xn
# a jar with 0 cookies and 2 jars containing 1 cookie are irrelevant, so our smallest jar will contain F2 cookies
# When N = {F2,...,Fm}, then CM(N) = [m/2]
# each term starting with the N-th is the sum of the previous n terms 

# n == number of cookies in the jar
# r == different ways of eating cookies in the jar
def eating_cookies(n):
    # if CM can eat less than 1 cookie
    r = -1
    
    if n < 0:
        r = 0
        
    # else if
    elif n == 0:
        r = 1
        
    # otherwise eating all 3 cookies
    else: 
        r = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return r
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")



