# 双指针，反向比大
def Merge(A: list[int], m: int, B: list[int], n: int):
    i, j = m - 1, n - 1
    cur = m + n - 1
    while i >= 0 and j >= 0:
        if B[j] >= A[i]:
            A[cur] = B[j]
            cur -= 1
            j -= 1
        else:
            A[cur] = A[i]
            cur -= 1
            i -= 1
    if j != -1:
        A[:j+1] = B[:j+1]
    

