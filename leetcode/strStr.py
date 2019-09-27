class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "": return 0
        for n in range(0, len(haystack)):
            if n + len(needle) <= len(haystack) and haystack[n:n + len(needle)] == needle: return n
        return -1


print(Solution.strStr(1, "hello", "ll"))
