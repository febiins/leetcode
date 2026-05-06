class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                sums=nums[left]+nums[right]
                
                if sums == target:
                    return [left,right]
        return None
