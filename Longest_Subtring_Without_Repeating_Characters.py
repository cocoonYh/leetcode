# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         s_dict = set()
#         max_length = 0
#         left, right = 0, 0
#         for i in range(len(s)):
#             if s[i] in s_dict:
#                 if len(s_dict) > max_length:
#                     max_length = len(s_dict)
#                 while (s[i] in s_dict):
#                     left += 1
#                     s_dict = set(s[left:right])
#             s_dict.add(s[i])
#             right = i
#         if len(s_dict) > max_length:
#             max_length = len(s_dict)
#         return max_length
"""
用dict来维护字符出现的位置
用left, right来维护当前子串
用max_length来维护最大长度
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = dict()
        left, right = 0, 0
        max_length = 0
        if s == "":  # 如果是空直接返回
            return 0
        for i in range(len(s)):
            if s[i] in s_dict and s_dict[s[i]] >= left:  # 出现在字典里且位置在当前子串中
                if right - left + 1 > max_length:  # 更新最大长度
                    max_length = right - left + 1
                left = s_dict[s[i]] + 1  # 更新子串位置
            s_dict[s[i]] = i
            right = i
        if right - left + 1 > max_length:  # 最后更新一遍
            max_length = right - left + 1
        return max_length
