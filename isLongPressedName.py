class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True
        if not name or not typed:
            return False
        
        n = len(name)
        m = len(typed)
        slow, fast = 0, 0

        while fast < m:
            if slow < n and name[slow] == typed[fast]:
                slow += 1
                fast += 1
            else:
                if fast > 0 and typed[fast] == typed[fast - 1]:
                    fast += 1
                else:
                    return False
        
        return slow == n
