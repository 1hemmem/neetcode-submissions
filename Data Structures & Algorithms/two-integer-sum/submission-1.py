class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_idx, i in enumerate(nums):
            for j_idx, j in enumerate(nums):
                if i_idx != j_idx and i + j == target:
                    return [i_idx, j_idx]
        return []