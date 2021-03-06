###############################################################################################
# 采用直接将数转化成字符串，不过这样会造成额外的开销
###########
# 时间复杂度：O(n/2)，n为字符串数的长度
# 空间复杂度：O(n)，创建了一个字符串
###############################################################################################
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_ = str(x)
        len_ = len(str_)
        for i in range(len_//2):
            if str_[i] != str_[len_-i-1]:
                return False
        return True