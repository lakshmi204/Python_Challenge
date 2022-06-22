class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def combination(lst,candidates):
            for i in range(len(candidates)):
                if sum(lst)==target:
                    ans.append(lst)
                    break
                elif sum(lst)<target:
                    combination(lst+[candidates[i]],candidates[i:])
            return
        combination([],candidates)
        return ans
    