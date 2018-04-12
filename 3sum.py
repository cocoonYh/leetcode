# 未成行的优化：
# 排序后三层for循环 检测是否在列表内 在每层循环加入判断 若>0 则break


# 解决方法：
# 固定一个i，然后j和k作为最左最右的两个指针往中间靠拢
# 若有相同的元素则跳过
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = list()
        length = len(nums)
        if length < 3:
            return result
        i = 0
        while i < length - 2:
            if i > 0 and nums[i] == nums[i - 1]:  # 如果后一个跟前一个相同就continue
                i += 1
                continue
            j, k = i + 1, length - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    tmp = [nums[i], nums[j], nums[k]]
                    result.append(tmp)  # 这里不用判断是否在result内，因为result里面肯定没有
                    while j < k and nums[j] == nums[j + 1]:  # 不循环与当前相同的数，下同
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
            i += 1  # 因为是while不是for，所以别忘了递增
        return result
