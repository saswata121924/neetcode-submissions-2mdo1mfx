class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not (len(s) == len(t)):
            return False
        map = {}
        for i in range(0,len(s)):
            if s[i] in map:
                map[s[i]]= map[s[i]]+1
            else:
                map[s[i]]=1
            if t[i] in map:
                map[t[i]] = map[t[i]]-1
            else:
                map[t[i]]= -1
        for i in map.keys():
            if map[i] != 0:
                return False
        return True