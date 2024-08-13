class Solution(object):
    def combinationSum2(self,candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:  # skip duplicates
                    continue
                if candidates[i] > target:  # no need to continue if the candidate exceeds the target
                    break
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])
        
        candidates.sort()  # sort the candidates to handle duplicates
        result = []
        backtrack(0, target, [])
        return result

    
