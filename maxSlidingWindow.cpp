#include <set>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k)
    {
        multiset<int, greater<int>> ms;
        int left = 0, right = 0;
        int len = nums.size();
        vector<int> ans;

        while (right < len)
        {
            ms.emplace(nums[right]);
            if (right >= k)
                ms.erase(ms.find(nums[left++]));

            if (right >= k - 1)
                ans.emplace_back(*ms.begin());

            right++;
        }
        return ans;
    }
};