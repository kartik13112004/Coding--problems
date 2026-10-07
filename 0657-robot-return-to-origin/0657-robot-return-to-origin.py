class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Count each type of move
        R = moves.count("R")
        L = moves.count("L")
        U = moves.count("U")
        D = moves.count("D")

        # Right and left must cancel
        # Up and down must cancel
        return R == L and U == D