class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)  # 先换成set类型，提高查询效率
        if endWord not in wordList:  # 如果结束词不在集合里直接返回
            return 0
        now_words = {beginWord, }
        end_words = {endWord, }
        result = 1
        while len(now_words) > 0:
            tmp_words = set()
            for word in now_words:  # 对现在列表里的每个单词
                for i in range(len(word)):  # 遍历该单词每个可以被替换的位置
                    for chr in 'qazwsxedcrfvtgbyhnujmikolp':  # 替换每一种可能性
                        if chr == word[i]:  # 如果跟现在的是一样的就进入下一次循环
                            continue
                        tmp_word = word[:i] + chr + word[i + 1:]
                        if tmp_word in wordList:  # 如果出现在wordList里就在wordList里删除然后添加进下一层结点里
                            if tmp_word in end_words:  # 如果当前字符串在结果集里面
                                return result + 1
                            tmp_words.add(tmp_word)
            now_words = tmp_words
            if len(now_words) > len(end_words):  # 交换较小的结果集，减少遍历次数
                now_words, end_words = end_words, now_words
            wordList -= now_words  # 从总集里面减去初始集
            result += 1
        return 0
