class Solution:
    def reverseString(self, s: list[str]) -> None:
        # Create a new list to store the reversed string
        reversed = []

        # Traverse from the last character to the first
        for i in range(len(s) - 1, -1, -1):
            reversed.append(s[i])

        # Copy reversed characters back into s
        for i in range(len(s)):
            s[i] = reversed[i]