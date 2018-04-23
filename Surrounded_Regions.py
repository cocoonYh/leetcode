class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = len(board)  # 如果不到三行或者三列就肯定不会被包围
        if rows < 3:
            return
        cols = len(board[0])
        if cols < 3:
            return
        o_matrix = dict()  # 记录那些是"O"
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    o_matrix[(i, j)] = False
        for i in range(rows):  # 遍历首尾列
            if board[i][0] == "O":
                self.check_and_change(o_matrix, (i, 0), rows, cols)
            if board[i][cols - 1] == "O":
                self.check_and_change(o_matrix, (i, cols - 1), rows, cols)
        for i in range(cols):  # 遍历首尾行
            if board[0][i] == "O":
                self.check_and_change(o_matrix, (0, i), rows, cols)
            if board[rows - 1][i] == "O":
                self.check_and_change(o_matrix, (rows - 1, i), rows, cols)
        for pos in o_matrix:  # 找到没有被遍历到的矩阵元素
            if not o_matrix[pos]:
                board[pos[0]][pos[1]] = "X"
        return

    def check_and_change(self, o_matrix, pos, rows, cols):
        if pos[0] < 0 or pos[0] > rows - 1 or pos[1] < 0 or pos[1] > cols - 1:  # 如果不在矩阵内
            return
        if pos not in o_matrix:  # 如果不是"O"
            return
        if o_matrix[pos]:  # 如果已经遍历过
            return

        o_matrix[pos] = True

        self.check_and_change(o_matrix, (pos[0] - 1, pos[1]), rows, cols)
        self.check_and_change(o_matrix, (pos[0] + 1, pos[1]), rows, cols)
        self.check_and_change(o_matrix, (pos[0], pos[1] - 1), rows, cols)
        self.check_and_change(o_matrix, (pos[0], pos[1] + 1), rows, cols)
