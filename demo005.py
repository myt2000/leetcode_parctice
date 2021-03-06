'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         pass
    
# if __name__ == "__main__":
#     # a = "babad"
#     # a = "cbbd"
#     # a = ""
#     # a = "a"
#     # a = "ac"
#     # a = "babadada"
#     a = "aaabaaaa"
#     # a = "abcdbbfcba"
#     test = Solution()
#     result = test.longestPalindrome(a)
#     print(result)

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         '''
#         马拉车算法
#         '''
#         if s == "":
#             return ""
#         s1 = '$#' + '#'.join(s) + '#@'
#         mx = 0  # 已遍历的最大右边界
#         mid = 0  # 对应的中心点
#         l = len(s1)
#         dp = [0] * l
#         for i in range(1, l - 1):
#             if i < mx:  # 可以利用之前保存的值
#                 dp[i] = min(mx - i, dp[mid * 2 - i])  # 不能超过已遍历的右边界
#             t = 0
#             while 1:  # 继续扩张
#                 if s1[i + dp[i] + t] != s1[i - dp[i] - t]:
#                     break
#                 t += 1
#             dp[i] += t - 1
#             if i + dp[i] > mx:  # 更新边界值
#                 mx = i + dp[i]
#                 mid = i
#         maxlen, maxidx = 0, 0
#         for i in range(l):  # 找最大子串
#             if dp[i] > maxlen:
#                 maxlen = dp[i]
#                 maxidx = i
#         return s1[maxidx - maxlen:maxidx + maxlen + 1].replace('#', "")


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         currten_res = ""
#         if len(s) > 1:
#             for i in range(len(s)):
#                 sub_str = s[i:-1]
#                 last_pos = sub_str.rfind(s[i])
#                 if i != last_pos:
#                         text = s[i:last_pos+1]
#                         if text == text[::-1]:
#                             if len(text) > len(currten_res):
#                                 currten_res = text
#             for i in range(len(s)-1, 0, -1):
#                 sub_str = s[i:-1]
#                 first_pos = sub_str[0:i+1].find(s[i])
#                 if i != first_pos:
#                     text = s[first_pos:i+1 ]
#                     if text == text[::-1]:
#                         if len(text) > len(currten_res):
#                             currten_res = text
#             if len(currten_res) > len(s[0]):
#                 return currten_res
#             return s[0]
#         elif len(s) == 1:
#             return s
#         else:
#             return s
import logging


# 中心扩展法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        max_length = 0
        center = 0
        for i in range(len(s)):
            begin = self.center_expand(s, i, i)  # 子串是偶数长度
            end = self.center_expand(s, i, i+1)  # 子串是奇数长度
            if max_length < max(begin, end):
                center = i
                max_length = max(begin, end)
        return s[center-(max_length -1)//2:center + max_length//2 +1]


    def center_expand(self, s: str, begin: int, end: int) -> int:
        '''
        :param s: 字符串
        :param begin: 字符串左边偏移起始位置
        :param end: 字符串右边偏移起始位置
        :return:  计算子字符串长度
        '''
        left = begin
        right = end
        while(left >=0 and right < len(s) and s[left] == s[right]):
            left-=1
            right+=1
        return right - left -1


if __name__ == "__main__":
    a = Solution()
    b = a.longestPalindrome("abcdbbfcba")
    # LOGGIONG_LEVEL = logging.INFO
    logging.basicConfig(level=logging.INFO)
    logging.info(b)
