from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k <= 0:
            return False
        record = set()
        
        #get index and value
        for i, n in enumerate(nums):
            if n in record:
                return True
            record.add(n)

            #managing sliding window by removing the oldest element 
            if len(record) > k:
                record.remove(nums[i-k])
        return False