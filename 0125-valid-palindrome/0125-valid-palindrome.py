class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Keep only alphabets and digits
        s = ''.join(ch.lower() for ch in s if ch.isalnum())

        # Check if the string is equal to its reverse
        if s == s[::-1]:
            return True
        else:
            return False