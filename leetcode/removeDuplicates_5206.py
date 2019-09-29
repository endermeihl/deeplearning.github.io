class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        cha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
               "p", "q", "r", "s", "t", "u", "v", "w", "k", "y", "z"]
        chat = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t", "u", "v", "w", "k", "y", "z"]
        for n in range(1, k):
            for a in range(len(cha)):
                chat[a] = chat[a] + cha[a]
        for x in chat:
            if x in s: s = s.replace(x, "")
        return s
        # while True:
        #     for


print(Solution.removeDuplicates(1, "aadda", 2))
