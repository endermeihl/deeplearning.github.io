class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        s = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        check = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for n in text:
            if n in check.keys(): check[n] += 1
        min = int(check["b"] / s["b"])
        for key in check.keys():
            num = int(check[key] / s[key])
            if num == 0 or num < min: min = num
        return min


print(Solution.maxNumberOfBalloons(1, "lloo"))
