class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        x = 0
        for n in range(len(s)):
            if s[n] == "V":
                x += 5
            if s[n] == "L":
                x += 50
            if s[n] == "D":
                x += 500
            if (n + 1 > len(s) - 1 and s[n] == "I") or (s[n] == "I" and s[n + 1] != 'V' and s[n + 1] != 'X'):
                x += 1
            if (n + 1 > len(s) - 1 and s[n] == "X") or (s[n] == "X" and s[n + 1] != 'L' and s[n + 1] != 'C'):
                x += 10
            if (n + 1 > len(s) - 1 and s[n] == "C") or (s[n] == "C" and s[n + 1] != 'D' and s[n + 1] != 'M'):
                x += 100
            if s[n] == "M":
                x += 1000
            if n + 1 <= len(s) - 1 and s[n] == "I" and (s[n + 1] == 'V' or s[n + 1] == 'X'):
                x -= 1
            if n + 1 <= len(s) - 1 and s[n] == "X" and (s[n + 1] == 'L' or s[n + 1] == 'C'):
                x -= 10
            if n + 1 <= len(s) - 1 and s[n] == "C" and (s[n + 1] == 'D' or s[n + 1] == 'M'):
                x -= 100
        return x


print(Solution.romanToInt(1, "MCMXCIV"))
