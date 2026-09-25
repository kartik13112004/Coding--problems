class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        for i in range(1, len(strs)):
            for k in range(min(len(strs[0]), len(strs[i]))):
                if strs[0][k] != strs[i][k]:
                    strs[0] = strs[0][0:k]
                    break

            if len(strs[i]) < len(strs[0]):
                strs[0] = strs[i]

        return strs[0]