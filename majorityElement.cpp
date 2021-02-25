#include <vector>

using namespace std;

// 摩尔投票法
class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        int count = 0;
        int candidate = -1;
        for (int num : nums)
        {
            if (candidate == num)
                count++;
            else if (--count < 0)
            {
                candidate = num;
                count = 1;
            }
        }

        return candidate;
    }
};

// 摩尔投票法模板
class MooreVote
{
public:
    int majorityElement(vector<int> &nums)
    {
        int count = 0;
        int majority = -1;
        for (int num : nums)
        {
            if (count == 0)
            {
                count = 1;
                majority = num;
            }
            else
            {
                if (majority == num)
                    ++count;
                else
                    --count;
            }
        }

        int counter = 0;
        if (count <= 0)
        {
            return -1;
        }
        else
        {
            for (int num : nums)
            {
                if (num == majority)
                    ++counter;
            }
        }

        return counter > nums.size() / 2 ? majority : -1;
    }
};