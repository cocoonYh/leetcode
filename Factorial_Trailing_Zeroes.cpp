#include<iostream>

using namespace std;

class Solution {
public:
	int trailingZeroes(int n) {
		int res = 0;
		while (n / 5 > 0) {
			n /= 5;
			res += n;
		}
		return res;
	}
};