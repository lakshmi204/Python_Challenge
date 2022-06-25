class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = [""] * numRows
        i = 0
        j = 0
        k = numRows - 2
        while i < len(s):
            if k == 0 and j == numRows:
                j = 0
                k = numRows - 2
                # print(arr)
            if j < numRows and k >= 0:
                arr[j] += s[i]
                j += 1
                # print(arr)
            elif j == numRows:
                arr[k] += s[i]
                k -= 1
                # print(arr)

            i += 1
        return "".join(arr)
    