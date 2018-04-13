class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        flag, num = 1, 0
        str = str.strip()  # 去掉多余的空格
        if len(str) == 0:
            return 0
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            flag = -1
            str = str[1:]
        for x in str:
            if num > 2147483648:  # 如果达到上限就break
                break
            elif '0' <= x <= '9':
                num = num * 10 + ord(x) - ord('0')
            else:  # 如果遇到非数字就break
                break
        num *= flag
        num = num if num <= 2147483647 else 2147483647  # 正负上限不一样
        num = num if num >= -2147483648 else -2147483648
        return num
