class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = set()
        for n in nums:
            if n in record:
                return True
            record.add(n)
        return False
        