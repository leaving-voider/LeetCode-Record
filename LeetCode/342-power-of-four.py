###############################################################################################
# 遍历了一遍，官方也给了数学方法
###########
# 时间复杂度：O(log(4)n)，n为输入的数值，时间复杂度为以4为底数的log
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 1
        while x <= n:
            if x == n:
                return True
            x *= 4
        return False