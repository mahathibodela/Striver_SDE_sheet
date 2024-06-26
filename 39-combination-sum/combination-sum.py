class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def check(i, tar, subans, ans):
            if tar == 0:
                temp = [i for i in subans]
                ans.append(temp)
                return
            if i == n:
                return 
            
            for j in range(i, n):
                if j != i and candidates[j] == candidates[j - 1]: continue
                if candidates[j] <= tar:
                    subans.append(candidates[j])
                    check(j, tar - candidates[j], subans, ans)
                    subans.pop(-1)
                else:
                    return
        
        candidates.sort()
        n = len(candidates)
        ans = []
        check(0, target, [], ans)
        return ans