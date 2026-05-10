class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            groups.setdefault(sorted_str, []).append(s)
        return list(groups.values())