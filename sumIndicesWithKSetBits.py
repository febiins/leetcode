class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=[0]*n
        total=0

        for i in range(n):
            l[i]=l[i>>1]+(i&1)

            if l[i]==k:
                total+=nums[i]
        return total        
        
