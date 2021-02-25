#include <vector>
#include <set>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    vector<int> fairCandySwap(vector<int> &A, vector<int> &B)
    {
        int size1 = A.size();
        int size2 = B.size();
        int pivot1 = 0, pivot2 = 0;
        set<int> setB(B.begin(), B.end());

        for (int i = 0; i < size1; ++i)
            pivot1 += A[i];
        for (int i = 0; i < size2; ++i)
            pivot2 += B[i];

        int count = (pivot1 - pivot2) / 2;
        for (int i = 0; i < size1; ++i)
        {
            int temp = A[i] - count;
            if (setB.find(temp) != setB.end())
            {
                return {A[i], temp};
            }
        }

        return {};
    }
};