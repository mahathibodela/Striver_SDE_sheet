class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def find(i, ans, subans, tot):
            if tot == target:
                temp = [k for k in subans]
                ans.append(temp)
                print(ans)
                return 
            if tot > target :
                return
            
            #pick 
            for j in range(i, len(candidates)):
                if j == i or candidates[j - 1] != candidates[j]:
                    if tot + candidates[j] <= target:
                        subans.append(candidates[j])
                        tot += candidates[j]
                        find(j + 1, ans, subans, tot)
                        tot -= candidates[j]
                        subans.pop(-1)
                    else:
                        return
            
            return

                
        
        candidates.sort()
        ans = []
        find(0, ans, [], 0)
        return ans