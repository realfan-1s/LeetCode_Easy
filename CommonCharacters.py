def HashTable(A: list[str]):
    minfreq = [float("inf")] * 26
    for word in A:
        freq = [0] * 26
        for char in word:
            freq[ord(char) - ord("a")] += 1
        for i in range(26):
            minfreq[i] = min(minfreq[i], freq[i])

    res = []
    for i in range(26):
        res.extend(chr(i + ord("a")) * minfreq[i])

    return res

def HashMap(A: list[str]):
    if not A:
        return []

    res = []
    for char in set(A[0]):
        count = [w.count(char) for w in A]
        s = char * min(count, 0)
        res += s
    return res