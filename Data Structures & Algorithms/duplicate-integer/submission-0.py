class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicates = len(nums) != len(set(nums))
        if(has_duplicates):
            return True
        else:
            return False
