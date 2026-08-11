class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0)+1

        desired_freqs = sorted(count.values())[::-1][0:k]
        
        rtn = []
        for k,v in count.items():
            if v in desired_freqs:
                rtn.append(k)
        return rtn