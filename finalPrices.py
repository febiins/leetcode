class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer=prices[:]
        
        i=0
        while i < len(prices):
            j=i+1
            while j < len(prices):
                if prices[i]>=prices[j]:
                    answer[i]=prices[i]-prices[j]
                    break
                j+=1
            i+=1        

        return answer               

        
