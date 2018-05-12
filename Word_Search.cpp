#include<iostream>
#include<vector>
#include<string>

using namespace std;

class Solution {
public:
	bool exist(vector<vector<char>>& board, string word) {
		int row = board.size(), col = board[0].size();
		if (row == 0 || col == 0) {
			return false;
		}
		if (word.size() == 0) {
			return true;
		}
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (BFS(board, word, i, j, 0)) {
					return true;
				}
			}
		}
		return false;
	}

	bool BFS(vector<vector<char>>& board, string word, int i, int j, int index) {
		bool result;
		if (index == word.size()) { // word边界判断 最优先
			return true;
		}
		if (i < 0 || j < 0 || i >= board.size() || j >= board[0].size()) { // board边界判断
			return false;
		}
		if (board[i][j] != word[index]) { //值检测
			return false;
		}
		char tmp = board[i][j];
		board[i][j] = ' '; // 记录当前位置
		result = BFS(board, word, i - 1, j, index + 1) || BFS(board, word, i + 1, j, index + 1) || BFS(board, word, i, j - 1, index + 1) || BFS(board, word, i, j + 1, index + 1);
		board[i][j] = tmp; // 修正当前位置
		return result;
	}
};