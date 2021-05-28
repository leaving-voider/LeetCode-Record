###############################################################################################
# 自己写的
###########
# 时间复杂度：O(logC)，C 在此题中为2^31，为数的范围，logC为31，31位二进制可表示所有数字
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        HMdist = 0
        for i in range(30, -1, -1):
            if (x >> i)&1 != (y >> i)&1:
                HMdist += 1
        return HMdist

###############################################################################################
# 官网给的，实测更慢
###########
# 时间复杂度：O(logC)，其中 C 是元素的数据范围，在本题中 log C=log 2^31 = 31
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        HMdist = 0
        s = x^y
        while(s):
            HMdist += s&1
            s >>= 1
        return HMdist