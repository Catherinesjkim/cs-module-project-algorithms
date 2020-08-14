'''
Input: an integer [16, 10, 6, 3]
Returns: an integer
Fibonacci sequence: 
'''
#5 - Module 3: A First-Pass Solution

# Empty the Most Jars Algo: the monster reduces the number of distinct jars by as many as he can for each move
# Binary Algo: the monster takes 2^k cookies from all jars that contain at least 2^k cookies for k as large as possible

# Plan - UPER
# s = set of the numbers of the cookies in the jars
# the Cookie Monster number of S, CM(S), is the minimum number of moves Cookie Monster must use to empty all of the jars in S
# CM(S) = n  - Cookie Monster folows an optimal procedure
# after he performs move n, all jars are empty
# therefor, each jar may be represented as the sum of some moves
# For all |S| = m, [log2(m+1) <= CM(S) <= m
# 1. we challenge our monster to empty a set of jars containing cookies in the Fibonacci sequence Xn+2= Xn+1 + Xn
# a jar with 0 cookies and 2 jars containing 1 cookie are irrelevant, so our smallest jar will contain F2 cookies
# When S = {F2,...,Fm}, then CM(S) = [m/2]
# each term starting with the n-th is the sum of the previous n terms 
# in the 3-nacci sequence, aka Tribonacci, each term after the third is the sum of the previous three terms

def eating_cookies(n):
    # if we eat less than 1 cookie
    r = -1
    if n < 0:
        r = 0
        
    # else if
    elif n == 0:
        r = 1
    # otherwise eating all 5 cookies
    else: 
        r = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return r
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")



"""
You are climbing a staircase. It takes n steps to reach the top.

Each time, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Copy
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Copy
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
We are not solving the problem now— we are crafting a plan for solving it.

First, let’s break the problem into smaller objectives that we can then tackle one at a time:

Decide if we should use recursion to solve the problem by looking for clues in the problem description.
Find similar problems that we’ve already solved and analyze those problems to see if they help us solve this problem.
Draw a diagram for a small input and study the diagram to help understand any potential solutions.
If we use recursion, discover the base case or base cases.
If we use recursion, discover the recursive case.
Write out our algorithm as pseudocode.
Change each line of pseudocode into actual code.
Test out our code and see if it is returning the outputs that we would expect.
The list above is an excellent start of sub-objectives that we can begin working on right away. Remember, as we solve the sub-objectives, we should be prepared to change our original plan. We should allow every new piece of information or understanding to mold and inform our original plan as we move forward.

Challenge
Refer to this leetcode.com problem called “Fibonacci Number”. Write out a detailed plan of how you would solve the problem. Remember, we aren’t solving the problem now, we are just practicing the P part of the UPER process.

"""
