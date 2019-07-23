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