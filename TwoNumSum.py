
# 哈希值查找
def twoSum(nums: list[int], target: int) -> list[int]:
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums - i] = i
    return []


# 查找字典
def SumTwo(nums, target):
    numDict = {}
    for i, n in enumerate(nums):
        if (target - n) in numDict:
            return [numDict[target - n], i]
        else:
            numDict[n] = i
            
