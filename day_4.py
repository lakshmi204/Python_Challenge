class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(a, lst):
            for i in range(a, n + 2):
                if len(lst) == k:
                    ans.append(lst)
                    return
                elif len(lst) < k:
                    if i < n + 1:
                        helper(i + 1, lst + [i])

        helper(1, [])
        return ans
