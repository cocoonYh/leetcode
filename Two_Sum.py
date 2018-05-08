class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        新建一个字典，字典key为nums中的值，字典value为nums中值的下标
        由于有且只有一个解决方法，所以每个数字出现且仅出现一次
        对nums中的值hash后检测是否有target - nums[i]的值的时间复杂度为O(1)
        算法遍历一遍nums即可，时间复杂度为O(n)
        """
        nums_dict = dict()
        for i in range(len(nums)):
            if target - nums[i] in nums_dict:
                return nums_dict[target - nums[i]], i
            else:
                nums_dict[nums[i]] = i
