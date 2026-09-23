class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # Convert the sentence into a list of words
        k = s.split()

        # Number of pattern characters and words must be same
        if len(pattern) != len(k):
            return False

        # pattern → word
        d1 = {}

        # word → pattern
        d2 = {}

        for i in range(len(pattern)):

            # Check if pattern character already has a different word
            if pattern[i] in d1 and d1[pattern[i]] != k[i]:
                return False

            # Check if word already belongs to a different pattern character
            if k[i] in d2 and d2[k[i]] != pattern[i]:
                return False

            # Store pattern → word mapping
            d1[pattern[i]] = k[i]

            # Store word → pattern mapping
            d2[k[i]] = pattern[i]

        # All mappings are correct
        return True