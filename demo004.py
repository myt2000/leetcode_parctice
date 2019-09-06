'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m = len(nums1)
        n = len(nums2)
        if m < n:
            return self.findMedianSortedArrays(nums2, nums1)
        if n == 0:
            if (m % 2) == 1:
                middle = m // 2
                middle_num = nums1[middle]
            else:
                middle_num = (nums1[m // 2] + nums1[m // 2 - 1]) / 2
            return middle_num

        iMin = 0
        iMax = m
        while iMin <= iMax:
            i = (iMin + iMax) // 2
            j = (m+n+1)//2 - i
            print(i,j)
            if j != 0 and i != m and nums2[j-1] > nums1[j]:
                iMin = i+1
            elif i != 0 and j != n and nums1[i-1] > nums2[j]:
                iMax = i - 1
            else:
                maxLeft = 0
                if i == 0:
                    maxLeft = nums2[j-1]
                elif j == 0:
                    maxLeft = nums1[i-1]
                else:
                    maxLeft = max(nums1[i-1], nums2[i-1])
                if (m+n)%2 ==1:
                    return maxLeft

                minRight = 0
                if i == m:
                    minRight = nums2[j]
                elif j==n:
                    minRight= nums1[j]
                else:
                    minRight = min(nums2[j], nums1[i])

                return (maxLeft+minRight)/2.0
        return 0.0


        # nums1.extend(nums2)
        # nums1.sort()
        # length = len(nums1)
        # if (length % 2) == 1:
        #     middle = length // 2
        #     middle_num = nums1[middle]
        # else:
        #     middle_num = (nums1[length // 2] + nums1[length // 2 - 1]) / 2
        # return middle_num
        # 第二种解法和上面的没啥太大差别 只要用了sort就是时间复杂度O(nlogn)
        # nums1.extend(nums2)
        # nums1.sort()
        # if len(nums1) % 2 == 0:
        #     return sum(nums1[len(nums1) // 2 - 1:len(nums1) // 2 + 1:]) / 2
        # else:
        #     return nums1[(len(nums1) - 1) // 2]






    def median(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
                print(i, j, nums1[i], nums2[j - 1])
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
                print(i,j,nums1[i],nums2[j-1])
            else:
                # i is perfect

                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    print(i, j, nums1[i], nums2[j - 1])
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                print(i, j, nums1[i], nums2[j - 1])
                return (max_of_left + min_of_right) / 2.0


if __name__ == "__main__":
    nums1 = [1,2,3,4,5]
    nums2 = [-1,1,3,5,7,9]
    # nums1 = [2]
    # nums2 = []
    test = Solution()
    # result = test.findMedianSortedArrays(nums1, nums2)
    result = test.median(nums1, nums2)
    print(result)