class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[0]*len(prices)

        min_val=prices[0]

        #dp[min_index]=min_val
        for i in range(1,len(prices)):
            min_val= min(min_val,prices[i])
            profit=prices[i]-min_val
            dp[i]=max(dp[i-1],profit)   
        
        return dp[-1]   
