class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countsdict ={}
        for s in strs:
            temp = {}
            for l in s:
                temp[l] = temp.get(l,0) + 1
                countsdict[s] = temp

        returndict = {}
        for i,s in enumerate(strs):
            if s == "":
                returndict["empty"] = returndict.get("empty",[])+[""]
            else:
                key = tuple(sorted(countsdict[s].items()))
                returndict[key] = returndict.get(key, []) + [strs[i]]
        return list(returndict.values())
            