class Solution: #fibinocci series logic
    def climbStairs(self, n: int) -> int:
        x=1
        y=1
        
        for i in range(n-1):
            z=x+y
            x=y
            y=z
        return y     
