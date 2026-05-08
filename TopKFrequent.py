class TopKFrequent:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        l=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1

        freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)

        for i in range(k):
            l.append(freq[i][0])
        return l    

        
