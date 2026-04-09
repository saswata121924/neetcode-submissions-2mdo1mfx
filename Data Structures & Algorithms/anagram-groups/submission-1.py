class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            d = [0]*26
            for i in range(len(s)):
                d[ord(s[i]) - ord('a')] += 1
            res[tuple(d)].append(s)
        return list(res.values())
