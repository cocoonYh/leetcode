#include<iostream>
#include<vector>
using namespace std;


// Definition for a binary tree node.
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
	TreeNode* sortedArrayToBST(vector<int>& nums) {
		int length = nums.size();
		if (length == 0) {
			return NULL;
		}
		int mid = length / 2;
		TreeNode* root = new TreeNode(nums[mid]);
		getLeftTree(nums, root, 0, mid - 1);
		getRightTree(nums, root, mid + 1, length - 1);
		return root;
	}
	void getLeftTree(vector<int>& nums, TreeNode* now, int left, int right) {
		if (left > right) {
			return;
		}
		if (left == right) {
			now->left = new TreeNode(nums[left]);
		}
		int mid;
		if ((left + right) % 2 == 0) {
			mid = (left + right) / 2;
		}
		else {
			mid = (left + right) / 2 + 1;
		}
		TreeNode* midTree = new TreeNode(nums[mid]);
		now->left = midTree;
		getLeftTree(nums, midTree, left, mid - 1);
		getRightTree(nums, midTree, mid + 1, right);
	}
	void getRightTree(vector<int>& nums, TreeNode* now, int left, int right) {
		if (left > right) {
			return;
		}
		if (left == right) {
			now->right = new TreeNode(nums[left]);
		}
		int mid;
		if ((left + right) % 2 == 0) {
			mid = (left + right) / 2;
		}
		else {
			mid = (left + right) / 2 + 1;
		}
		TreeNode* midTree = new TreeNode(nums[mid]);
		now->right = midTree;
		getLeftTree(nums, midTree, left, mid - 1);
		getRightTree(nums, midTree, mid + 1, right);
	}
};