# 移动窗口法,时间复杂度O((N-L)L),空间复杂度O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h,n = len(haystack),len(needle)
        for i in range(h - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1


# 双指针，最佳时间复杂度O(N),最差线性复杂度O((N-L)L),空间复杂度O(1)
class solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)
        if not needle:
            return 0
        
        a = 0
        while a < h - n + 1:
            while haystack[a] != needle[0] and a < h - n + 1:
                a += 1
            b = c =0
            while a < h and b < n and haystack[a] == needle[b]:
                a += 1
                b += 1
                c += 1
            
            if c == n:
                return a - b
            a = a - c + 1
        return -1


# KMP算法, 前缀：包含首字母，不包含尾字母的所有字串,后缀：只包含尾字母，不包含首字母的所有字串
# 关键在于获得最长相等前后缀
class Handle:
    def KMP(self, haystack: str, needle: str):
        if not needle:
            return 0
        h, n = len(haystack), len(needle)
        prefix = self.GetNext(needle)
        j = 0
        for i in range(h):
            while j > 0 and needle[j] != haystack[i]:
                j = prefix[j]
            if needle[j] == haystack[i]:
                j += 1
                if j == n:
                    return i - n + 1
        return -1

    def GetNext(self, needle):
        n = len(needle)
        pnext = [0, 0]
        j = 0
        for i in range(1, n):
            while j > 0 and needle[i] != needle[j]:
                j = pnext[j]
            if needle[i] == needle[j]:
                j += 1
            pnext.append(j)
        return pnext

