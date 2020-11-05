# 递归
def Recursion(n):
    if n == 1:
        return "1"

    s = Recursion(n - 1)
    i = 0
    ans = ""
    for j, n in enumerate(s):
        if s[i] != s[j]:
            ans += str(j - i) + s[i]
            i = j
    ans += str(len(s) - i) + s[-1]
    return ans


# 迭代
def Enumerator(n):
    res = "1"
    for _ in range(n - 1):
        i, ans = 0, ""
        for j, n in enumerate(res):
            if res[i] != n:
                ans += str(j - i) + res[i]
                i = j
        ans += str[len(res) - i] + res[-1]
    return ans


# 动态规划
def DynamicProgramming(n):
    def countAndSay(self, n: int) -> str:
    dp = ["" for _ in range(n+1)]
    dp[1] = "1"
    if n == 1:
        return "1"
    for i in range(2, n+1):
        left = 0     # left，right分别表示连续相同数字的两端
        l = len(dp[i-1])
        for right in range(l):
            if right == l-1 or dp[i-1][right+1] != dp[i-1][left] :
                dp[i] += str(right-left+1)+dp[i-1][left]
                if right != l-1:  # 如果是dp[i-1][right+1]!=dp[i-1][left]的情况，left需要更新
                    left = right+1
        # print(dp)
    return dp[n]

