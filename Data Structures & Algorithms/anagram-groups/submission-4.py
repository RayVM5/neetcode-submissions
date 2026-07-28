class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returndict = {}
        for s in strs:
            count = [0]*26
            for l in s:
                count[ord(l)-ord("a")] += 1 
            returndict[tuple(count)] = returndict.get(tuple(count),[]) + [s]

        return list(returndict.values())