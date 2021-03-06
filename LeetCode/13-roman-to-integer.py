###############################################################################################
# 从前到后依次查看每个字符，如果该字符比右边的字符小，说明是起减法作用
###########
# 时间复杂度：O(n)，n为罗马字符s长度
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        dicts = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        len_ = len(s)
        for i in range(len_):
            value = dicts[s[i]]
            if i < len_ - 1 and value < dicts[s[i+1]]:
                num -= value
            else:
                num += value
        return num