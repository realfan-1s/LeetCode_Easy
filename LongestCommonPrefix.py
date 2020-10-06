# 横向扫描法,时间复杂度是O(mn),空间复杂度是O(1)
class Solution:
    def LongestCommonPrefix(self, strs:list[str]):
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.Choose(prefix, strs[i])
            if not prefix:
                break
        return prefix

    def Choose(self, str1, str2):
        length = 0
        index = min(len(str1), len(str2))
        while length < index and str1[length] == str2[length]:
            length += 1
        return str[:index]
        

# 纵向扫描法，时间复杂度是O(mn),空间复杂度是O(1)
class Handle:
    def LongestCommonPrefix(self, strs:list[str]):
        if not strs:
            return ""

        for i in range(len(str[0])):
            c = strs[0][i]
            if any(i == str[j] or str[j][i] != c for j in range(1, len(strs))):
                return strs[0][:i]

        return strs[0]


# 分治法，时间复杂度为O(mn),空间复杂度是O(mlogN)
class Divide:
    def LongestCommonPrefix(self, strs:list[str]):
        def lcp(start, end):
            if start == end:
                return strs[start]
            
            mid = (start + end) // 2
            lcpLeft = lcp(start, mid)
            lcpRight = lcp(mid+1, end)
            minWord = min(lcpLeft, lcpRight)
            for i in len(minWord):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]
            return lcpLeft[:minWord]
        return ""if not strs else lcp(0, len(strs) - 1)


# 二分查找法,时间复杂度为O(MNlogN),空间复杂度为O(1)
class TwoPart:
    def LongestgCommonPrefix(self, strs:list[str]):
        def IsCommonPrefix(length):
            str0 = strs[0][:length]
            return all(strs[i][:length] == str[0] for i in range(1, len(strs)))

        if not strs:
            return "" 
        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if IsCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1
        return str[0][:low]