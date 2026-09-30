class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        # Convert string into a list because strings cannot be changed directly
        s = list(s)

        # Move through the string in groups of 2*k characters
        for i in range(0, len(s), 2 * k):

            # Take the first k characters of the current group
            # and reverse them
            s[i:i+k] = s[i:i+k][::-1]

        # Convert the list back into a string
        return "".join(s)