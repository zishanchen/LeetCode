class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1

            """
            using the original array as tracker
            nums[index] > 0: unseen
            """
            if nums[index] > 0:
                nums[index] = -nums[index]
            """
            nums[index] < 0: index+1 exists
            nums[index] > 0: index+1 is missing
            """
        result = []
        for i, num in enumerate(nums):
            if num > 0:
                result.append(i+1)
        return result