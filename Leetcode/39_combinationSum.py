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
            # child combo is a copy of parent combo
            child_combo = copy.copy(parent_combo)
            ### print("i: ", i)
        # if current greater than target, move to next element
            current = array[i]
            if current > target:
                pass
            else:
                # if target is divisible by current element, this is a solution.
                if target%current == 0:
                    # extend child combo by num repeats
                    child_combo.extend([current]*(target//current))
                    # append solution to master array
                    solutions.append(child_combo)

                # then, for each number of repeats of current up til greater than target
                max_repeats = target//current
                ### print("max_repeats", max_repeats)

                for j in range(1,max_repeats+1):
                    # reset child_combo
                    child_combo = copy.copy(parent_combo)
                    # find combos for each number of repeats in the remaining array (barring current)
                    ### print("j:", j)
                    child_combo.extend([current]*j)
                    find_combo(array[0:i], target - j*current, child_combo)
    
    find_combo(candidates, target, [])

    return solutions

a_rray = [2,3,6,7]

print(combinationSum(a_rray,7))
                         
                
