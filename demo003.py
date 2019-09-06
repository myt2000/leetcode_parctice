'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # result = []
        # substr = []
        # string_length = len(s)
        # for i in range(0, string_length):
        #     if s[i] not in substr:
        #         substr.insert(0, s[i])
        #         result.append(len(substr))
        #     else:
        #         num = substr.index(s[i])
        #         substr = substr[:num]
        #         substr.insert(0, s[i])
        # if result:
        #     return max(result)
        # return 0

        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            print('s[j]:%s' % s[j])
            if s[j] in st:
                print(st[s[j]], i )
                i = max(st[s[j]], i)
            print('ans:%s, j-i+1:%s'% (ans, j-i+1))
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans

if __name__ == "__main__":
    # demo_string = 'abcabcbb'
    # demo_string = 'pwwkew'
    # demo_string = 'dvdf'
    demo_string = 'ohvhjdml'
    result = Solution().lengthOfLongestSubstring(demo_string)
    print(result)


