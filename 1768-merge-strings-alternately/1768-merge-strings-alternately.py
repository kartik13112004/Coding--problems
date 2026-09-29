class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Create an empty string to store the final answer
        result = ""

        # Loop until the shorter string ends
        for i in range(min(len(word1), len(word2))):

            # Take one character from word1 and one from word2
            # and add both to result
            result += word1[i] + word2[i]

        # Add any remaining characters from word1
        result += word1[i + 1:]

        # Add any remaining characters from word2
        result += word2[i + 1:]

        # Return the final merged string
        return result