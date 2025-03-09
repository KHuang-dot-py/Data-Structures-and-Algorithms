import copy

def permute(nums):

    p = []
    def create_permutations(p, nums_left, current_permutation):
        if len(nums_left) != 0:
            # for each number remaining to be added, we append it, remove it from the nums left
            for i in range(0, len(nums_left)):
                remaining_nums = copy.copy(nums_left)
                next_permutation = copy.copy(current_permutation)
                next_permutation.append(remaining_nums[i])
                remaining_nums.pop(i)
                create_permutations(p, remaining_nums, next_permutation)
        else:
            p.append(current_permutation)
    create_permutations(p, nums, [])

    return p
# issue is shallow copying

a_rray = [1,2,3,4]
# should return [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]


print(permute(a_rray))


