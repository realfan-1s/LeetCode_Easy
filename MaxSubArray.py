# 贪心算法,若当前指针所指元素之前的和小于0，则丢弃当前元素之前的数列
# 时间复杂度O(N),空间复杂度O(1)
def Greddy(nums: list[int]):
    pre = 0
    maxNum = nums[0]
    for item in nums:
        pre = max(item, pre + item)
        maxNum = max(pre, maxNum)

    return maxNum


# 动态规划,若前一个元素大于0，则将其加到当前元素上
def DynamicProgramming(nums: list[int]):
    n = len(nums)
    maxNum = nums[0]
    for i in range(1, n):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
        maxNum = max(nums[i], maxNum)
    return maxNum


# 分治法
def Division(nums):
    mid = len(nums) // 2
    if len(nums) == 1:
        return nums[0]
    else:
        left = Division(nums[:mid])
        right = Division(nums[mid:])

    # 计算中间的最大子序和
    max_Left = nums[mid - 1]
    temp = 0
    for i in range(mid - 1, -1, -1):
        temp += nums[i]
        max_Left = max(max_Left, temp)
    max_Right = nums[mid]
    temp = 0
    for i in range(mid, len(nums)):
        temp += nums[i]
        max_Right = max(max_Right, temp)
    return max(left, right, max_Right + max_Left)