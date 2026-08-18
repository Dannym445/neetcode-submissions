class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        for s in strs:
            new="".join(sorted(s))
            ret[new].append(s)
        return list(ret.values())

        