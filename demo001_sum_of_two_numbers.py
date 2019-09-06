'''
1. 两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_dict = {}
        count = 0
        element = list(range(len(nums)))
        nums_dict = dict(zip(nums, element))
        for num in nums:
            dev = target - num
            number_dict[dev] = count
            count += 1
            if dev in nums_dict and number_dict[dev] != nums_dict[dev]:
                result = [number_dict[dev], nums_dict[dev]]
                return result


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sum_numbers = Solution()
    result = sum_numbers.twoSum(nums, target)
    print(result)