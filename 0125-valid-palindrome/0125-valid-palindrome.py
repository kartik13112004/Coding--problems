class Solution:
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1

        while i < j:

            # Skip invalid character from left
            if not s[i].isalnum():
                i += 1
                continue

            # Skip invalid character from right
            if not s[j].isalnum():
                j -= 1
                continue

            # Compare characters
            if s[i].lower() != s[j].lower():
                return False

            # Move both pointers
            i += 1
            j -= 1

        return True