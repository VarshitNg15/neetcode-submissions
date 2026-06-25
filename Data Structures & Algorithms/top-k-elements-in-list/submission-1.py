class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = collections.defaultdict(int)
        res = []

        for n in nums:
            frq[n] += 1
        
        # Sort dictionary keys by their values (frequencies) in descending order
        sorted_elements = sorted(frq.keys(), key=lambda x: frq[x], reverse=True)
        
        # Take the first k elements
        return sorted_elements[:k]