###############################################################################################
# 完全用【486. 预测赢家】的动规来解
# dp[i][j]的含义：表示在[i, j]的左闭右闭区间，玩家能获得的最大利益
# 默认为玩家1先手，所以最后返回的dp[0][len_-1]的范围只能是玩家1的最大利益，若＞0则玩家1赢，小于0则玩家2赢
###########
# 时间复杂度：O(n^2)，n为数组 piles 长，计算数组中的状态
# 空间复杂度：O(n^2)，动规数组消耗
###############################################################################################
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 完全用【486. 预测赢家】的动规来解
        len_ = len(piles)
        dp = [[0]*len_ for _ in range(len_)] # dp[i][j]表示在i-j闭区间内玩家最大获益
        for i in range(len_-1, -1, -1):
            dp[i][i] = piles[i]
            for j in range(i+1, len_):
                dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
        return dp[0][len_-1] >= 0

###############################################################################################
# 同样，继续优化空间
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        len_ = len(piles)
        dp = [0]*len_
        for i in range(len_-1, -1, -1):
            dp[i] = piles[i]
            for j in range(i+1, len_):
                dp[j] = max(piles[i]-dp[j], piles[j]-dp[j-1])
        return dp[len_-1] >= 0

###############################################################################################
# 但此题和【486. 预测赢家】稍有不同，因为有两个额外的条件，使用如上动规时，并没有使用这两个条件
# 【数学】来了，将石头下标0-len-1根奇偶分为两组（使用了【数组的长度是偶数】这一条件），再稍加分析，先手玩家
# 可以一直在同一组进行选择，因此只需要判断哪一组石子更多，一直取就必胜（使用【数组的元素之和是奇数，所以没有平局】条件）
# 因此，先手总是可以胜利
###########
# 时间复杂度：O(1)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True