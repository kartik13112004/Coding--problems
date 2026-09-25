class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # If the list is empty, there is no common prefix
        if len(strs) == 0:
            return ""

        # If there is only one string, the entire string is the prefix
        if len(strs) == 1:
            return strs[0]

        # Compare the first string with every other string
        for i in range(1, len(strs)):

            # Compare characters up to the length of the shorter string
            for k in range(min(len(strs[0]), len(strs[i]))):

                # If characters at the same position are different
                if strs[0][k] != strs[i][k]:

                    # Keep only the characters before the mismatch
                    strs[0] = strs[0][0:k]

                    # Stop checking this string
                    break

            # If the current string is shorter than the current prefix,
            # make the current string the new prefix
            if len(strs[i]) < len(strs[0]):
                strs[0] = strs[i]

        # Return the final common prefix
        return strs[0]