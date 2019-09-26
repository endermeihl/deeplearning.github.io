class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        re = ""
        if len(strs) < 1:
            return ""
        for i in range(len(strs[0])):
            t = strs[0][i]
            for j in range(1, len(strs)):
                if i > len(strs[j]) - 1 or t != strs[j][i]:
                    t = ""
                    break
            re += t
            if t == "": break
        return str(re)


print(Solution.longestCommonPrefix(1, ["aca", "cba"]))
