class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:

            # Opening bracket → push
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)

            else:
                # Closing bracket but stack is empty
                if len(stack) == 0:
                    return False

                # Get the last opening bracket
                top = stack.pop()

                # Check matching pair
                if ch == ')' and top != '(':
                    return False

                if ch == ']' and top != '[':
                    return False

                if ch == '}' and top != '{':
                    return False

        # Valid only if nothing is left
        return len(stack) == 0