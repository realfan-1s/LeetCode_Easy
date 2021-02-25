class Solution:
    def isValid(self, s: str) -> bool:
        bracketList = []
        for item in s:
            if item in "([{":
                bracketList.append(item)
            elif item in ")]}":
                if not bracketList:
                    return False
                else:
                    if (item == ")" and bracketList[-1] in "[{") or (item == "]" and bracketList[-1] in "({") or (item == "}" and bracketList[-1] in "(["):
                        return True
                    else:
                        bracketList.pop()
        if bracketList:
            return False
        else:
            return True