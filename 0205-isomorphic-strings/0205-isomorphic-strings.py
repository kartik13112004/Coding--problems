class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Store mapping from s → t
        d1 = {}

        # Store mapping from t → s
        d2 = {}

        for i in range(len(s)):

            # If s character already has a different mapping → False
            if s[i] in d1 and d1[s[i]] != t[i]:
                return False

            # If t character already belongs to a different s character → False
            if t[i] in d2 and d2[t[i]] != s[i]:
                return False

            # Save the s → t mapping
            d1[s[i]] = t[i]

            # Save the t → s mapping
            d2[t[i]] = s[i]

        # All mappings are correct
        return True