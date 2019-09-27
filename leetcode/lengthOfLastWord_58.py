class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        num = 0
        max = 0
        for n in s:
            if n != " ":
                num += 1
                max = num
            if n == " ":
                num = 0
        return max


print(Solution.lengthOfLastWord(1, "hello    w"))
