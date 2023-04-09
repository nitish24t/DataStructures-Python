class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    # code here
    def knapSack(self,W, wt, val, n):
        # Base case
        if W == 0 or n == 0:
            return 0
        if matrix[n][W] != -1:
            return matrix[n][W]
            
        # if Weight of item is > total W --> Skip that item
        if wt[n-1] > W:
            matrix[n][W] = self.knapSack(W, wt, val, n-1)
            return matrix[n][W]
        else:
            add_item = val[n-1] + self.knapSack(W - wt[n-1], wt, val, n-1)
            skip_item = self.knapSack(W, wt, val, n-1)
            matrix[n][W] = max(add_item, skip_item)
            return matrix[n][W]
            
            
if __name__ == "__main__":
    ob = Solution()
    W = 50
    n = 3
    wt = [10, 20, 30]
    val = [60, 100, 120]
    matrix = [[-1 for x in range(W+1)] for i in range(n+1)]
    print(ob.knapSack(W,wt,val,n))
    print(matrix)
