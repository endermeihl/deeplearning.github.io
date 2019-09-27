class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)

        brackets_tag = {"(": 0, ")": 0, "}": 0, "{": 0, "]": 0, "[": 0}
        brackets_num = {"(": 0, ")": 0, "}": 0, "{": 0, "]": 0, "[": 0}
        if length % 2 != 0:
            return False
        for n in range(0, length):
            brackets_tag[s[n]] += n
            brackets_num[s[n]] += 1
        # print(brackets_num)
        # print(brackets_tag)
        if brackets_num[")"] != brackets_num["("] or brackets_num["{"] != brackets_num["}"] or brackets_num["["] != \
                brackets_num["]"]:
            return False
        if (brackets_tag[")"] - brackets_tag["("]) % 2 == (brackets_num[")"] % 2) and (
                brackets_tag["]"] - brackets_tag["["]) % 2 == brackets_num["["] % 2 and (
                brackets_tag["}"] - brackets_tag["{"]) % 2 == brackets_num["{"] % 2:
            return True
        return False


print(Solution.isValid(1, "()[]{}"))
print(Solution.isValid(1, "(]"))
print(Solution.isValid(1, "([)]"))
print(Solution.isValid(1, "{[]}"))
print(Solution.isValid(1, "[(({})}]"))
print(Solution.isValid(1, "[([]])"))
print(Solution.isValid(1, "(([]){})"))
