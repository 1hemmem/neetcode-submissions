class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        for num in nums:
            occurences[num] = occurences.get(num, 0) + 1
        
        # Sort items by frequency descending
        sorted_items = sorted(occurences.items(), key=lambda item: item[1], reverse=True)
        
        # Extract the top k keys
        return [item[0] for item in sorted_items[:k]]