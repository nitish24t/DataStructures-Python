"""
Link : https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1


"""


class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    # code here
    def knapSack(self,W, wt, val, n):
        # Base case
        if W == 0 or n == 0:
            return 0
            
        # if Weight of item is > total W --> Skip that item
        if wt[n-1] > W:
            return self.knapSack(W, wt, val, n-1)
        else:
            add_item = val[n-1] + self.knapSack(W - wt[n-1], wt, val, n-1)
            skip_item = self.knapSack(W, wt, val, n-1)
            return max(add_item, skip_item)
            
           
          
"""
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or dont pick it (0-1 property).

Example 1:

Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3
Example 2:

Input:
N = 3
W = 3
values[] = {1,2,3}
weight[] = {4,5,6}
Output: 0

"""
