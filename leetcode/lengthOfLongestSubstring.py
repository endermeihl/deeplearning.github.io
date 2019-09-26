class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        lookup = set()
        n = len(s)
        cur_l = 0
        max_l = 0
        for i in range(n):
            cur_l += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                cur_l -= 1
                left += 1
            if cur_l > max_l:
                max_l = cur_l
            lookup.add(s[i])
        return max_l
