class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x = "1"
        y = "1"
        for i in range(1, n):
            y = ""
            t = x[0]
            num = 0
            for j in range(0, len(x)):
                if x[j] == t:
                    num += 1
                if t != x[j] or j == len(x) - 1:
                    y = y + str(num) + t
                    num = 1
                if x[j] != t and j == len(x) - 1:
                    y = y + "1" + x[j]
                    num = 0
                t = x[j]
            x = y
        return y


print(Solution.countAndSay(1, 7))
