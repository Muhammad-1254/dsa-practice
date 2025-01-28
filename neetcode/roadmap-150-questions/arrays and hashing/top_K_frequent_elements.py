class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        freq_map = Counter(nums)
        most_common_elements = freq_map.most_common(k)
        result = [element for element, _ in most_common_elements]    
        return result