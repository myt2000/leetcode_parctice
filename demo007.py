'''
整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

'''
import logging

class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            x = abs(x)
            flag = 0
        num = str(x)
        num = num[::-1]
        result = int(num)
        if result<-2**31 or result>2**31-1:
            return 0
        elif flag:
            return result
        return 0-result

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    a = Solution()
    b = a.reverse(1534236469)
    logging.info(b)