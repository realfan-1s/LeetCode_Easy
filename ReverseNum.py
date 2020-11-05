# 栈思路
def reverse(self, x: int) -> int:
    strNum = str(x)
    numList = []
    reverseNum = []
    for i in strNum:
        numList.append(i)

    if numList[-1] == "0" and len(numList) > 1:
        numList.pop()

    for p in range(len(numList)):
        if numList[-1] in "0123456789":
            reverseNum.append(numList.pop())
        elif numList[-1] == "-":
            reverseNum.insert(0, numList.pop())
    strNum = "".join(reverseNum)
    if -2**31 < int(strNum) < 2**31 - 1:
        return int(strNum)
    else:
        return 0


# 整数思路
