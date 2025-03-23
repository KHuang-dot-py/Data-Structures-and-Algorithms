import copy

def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    solutions = []
    # return empty array if candidates is empty, no solutions
    if len(candidates) == 0: return solutions
    #else, sort the array
    cand_sorted = sorted(candidates)

    def find_combo(array, target, parent_combo):
        if len(array) == 0: return
        for i in range(len(array)-1,-1,-1):
        # if current greater than target, move to next element
            current = array[i]
            if current > target:
                pass
            else:
                # if target is divisible by current element, this is a solution.
                if target%current == 0:
                    solutions.append(parent_combo + [current]*(target//current))
                # then, for each number of repeats of current up til greater than target
                max_repeats = target//current
                # find combos for each number of repeats in the remaining array (barring current)
                for j in range(1,max_repeats+1):
                    find_combo(array[0:i], target - j*current, parent_combo + [current]*j)
    
    find_combo(candidates, target, [])

    return solutions


def combinationSumDFS(candidates, target):
    solutions = []
    DFS(target, [], target)
    # overall approach: explore all possibilities by exploring different paths, returning when the target is not achieved and
    # ... sum of path is greater than the target
    def DFS(target, path, remaining):
        # base cases
        if remaining < 0:
            return
        # solution is found when sum is exactly the target
        if remaining == 0:
            solutions.extend(path)
        for i in range(0, len(candidates)):
            DFS(target-candidates[i])



a_rray = [2,3,6,7]
print(a_rray+[3]*2)

print(combinationSum(a_rray,7))
                         
                
