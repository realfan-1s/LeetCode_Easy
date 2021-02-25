# 暴力解法
def romanToInt(s: str):
    romanDict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum = 0
    i = 0
    while i < len(s):
        if (i < len(s) - 1) and ((s[i] == "I" and s[i + 1] in "VX") or
                                 (s[i] == "X" and s[i + 1] in "LC") or
                                 (s[i] == "C" and s[i + 1] in "DM")):
            sum = sum + romanDict[s[i + 1]] - romanDict[s[i]]
            i += 2
        else:
            sum += romanDict[s[i]]
            i += 1
    return sum


# 构建字典
def RomanToInt(s: str):
    d = {
        'I': 1,
        'IV': 3,
        'V': 5,
        'IX': 8,
        'X': 10,
        'XL': 30,
        'L': 50,
        'XC': 80,
        'C': 100,
        'CD': 300,
        'D': 500,
        'CM': 800,
        'M': 1000
    }
    return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))


print(RomanToInt("MDLXX"))
