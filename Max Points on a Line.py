from decimal import Decimal

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


# 固定一个点，然后遍历其余剩余点，计算斜率，以斜率为键值存储dict中，返回最大值 + 重复点
class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        length = len(points)
        if length < 3:
            return length
        ans = 0
        for i in range(length - 1):
            p0 = points[i]
            counter = {'max': 0}
            same_point = 1  # 初始值为 1 ，因为计算线上最多的点的时候要算上自己
            for j in range(i + 1, length):
                p1 = points[j]
                if p0.x == p1.x and p0.y == p1.y:
                    same_point += 1
                elif p0.x == p1.x:
                    counter['max'] += 1
                else:
                    # float的精度不够，引入Decimal
                    k = Decimal(p1.y - p0.y) / (p1.x - p0.x)
                    counter[k] = counter[k] + 1 if k in counter else 1
            try:
                ans = max(ans, max(counter.values()) + same_point)
            except ValueError:
                ans = max(ans, same_point)
        return ans
