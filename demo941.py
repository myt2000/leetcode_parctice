'''
给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

A.length >= 3
在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 



 

示例 1：

输入：[2,1]
输出：false
示例 2：

输入：[3,5,5]
输出：false
示例 3：

输入：[0,3,2,1]
输出：true
 

提示：

0 <= A.length <= 10000
0 <= A[i] <= 10000 
 
'''

class Solution:
    def validMountainArray(self, A) -> bool:
        # if 3<= len(A)<= 10000 and max(A)<= 10000 and min(A)>=0:
        #     max_num = max(A)
        #     max_loc = A.index(max_num)
        #     up = A[:max_loc+1]
        #     if not len(up):
        #         return False
        #     down = A[max_loc+1:]
        #     if not len(down):
        #         return False
        #     down.reverse()
        #     li = [up, down]
        #     for i in li:
        #         if len(i) > 1:
        #             for j in range(len(i)-1):
        #                 if i[j] >= i[j+1] and i[j+1] >= max(A):
        #                     return False
        #         elif len(i) <= 1 and max(i) == max_num:
        #             return False
        #     return True
        # return False

        if 3 <= len(A) <= 10000 and max(A) <= 10000 and min(A) >= 0:
            max_num = max(A)
            max_loc = A.index(max_num)
            if max_loc == len(A)-1 or max_loc == 0 or len(A[max_loc:]) <= 1:
                return False
            for i in range(0, max_loc):
                # print(A[i], A[i+1])
                if A[i] > max_num or A[i] >= A[i+1]:
                    return False
            for i in range(max_loc, len(A)-1):
                if A[i] > max_num or A[i] <= A[i+1]:
                    return False
            return True
        return False


if __name__ == '__main__':
    # a = [0, 3, 2, 1]
    # a = [3,5,5]
    # a = [2, 1]
    # a = [0, 3, 2, 1]
    # a = [0,1,2,3,4,5,6,7,8,9]
    # a = [0,1,2,1,2]
    # a = [1,7,9,5,4,1,2]
    a = [1,1,1,1,1,1,1,2,1]
    b = Solution()
    print(b.validMountainArray(a))