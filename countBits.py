class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]

        for i in range(n+1):
            num=i
            count=0

            while num>0:
                rem=num%2

                if rem==1:
                    count+=1
                num=num//2
            l.append(count)
        return l            
