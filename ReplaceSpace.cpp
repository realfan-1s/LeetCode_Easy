#include <string>

using namespace std;

class Solution
{
public:
    string replaceSpace(string s)
    {
        int len = s.size();
        int count = 0;
        for (int i = 0; i < len; ++i)
        {
            if (s[i] == ' ')
                ++count;
        }

        s.resize(len + 2 * count);
        for (int i = len - 1, j = s.size() - 1; i < j; --i, --j)
        {
            if (s[i] != ' ')
                j = i;
            else
            {
                s[j] = '0';
                s[j - 1] = '2';
                s[j - 2] = '%';
                j -= 2;
            }
        }

        return s;
    }
};