# 374. Guess Number Higher or Lower

# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

#  Example 1:
# Input: n = 10, pick = 6
# Output: 6

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            if res == 0:
              return mid
            elif res == +1:
                left = left + 1
            else:
                right = n + 1    
