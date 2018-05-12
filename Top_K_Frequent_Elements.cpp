#include<iostream>
#include<queue>
#include<collection.h>
using namespace std;
class Solution {
public:
	vector<int> topKFrequent(vector<int>& nums, int k) {
		unordered_map<int, int> nums_map; // hashmap C++11������unorderd_map�滻
		for (int num : nums) {
			nums_map[num]++;
		}
		priority_queue<pair<int, int>> que; // priority_queue����
		for (auto nums_fre : nums_map) {
			que.push(pair<int, int>(nums_fre.second, nums_fre.first));
		}
		vector<int> result;
		while (k--){
			result.push_back(que.top().second);
			que.pop();
		}
		return result;
	}
};