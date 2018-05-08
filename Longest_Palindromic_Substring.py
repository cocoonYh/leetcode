class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        tmp_palindromic = ""

        if len(s) < 2 or s == s[::-1]:
            return s

        def check(s, start, end):  # 从中间向两边扩充
            if s[start] != s[end]:
                return ""
            # 越界判断要写在while里面 不然会访问越界
            while start >= 0 and end < length and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1:end]

        for i in range(length - 1):  # 遍历到前一位
            tmp = check(s, i, i)
            if len(tmp) > len(tmp_palindromic):
                tmp_palindromic = tmp
            tmp = check(s, i, i + 1)
            if len(tmp) > len(tmp_palindromic):
                tmp_palindromic = tmp
        return tmp_palindromic
