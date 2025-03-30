def threeSum(nums):
    # sort the array
    nums = sorted(nums)
    # for each element of the array, run modified two-sum on rest of the array to find pairs that add to 0
    # build a hashmap to store array elements, accounting for collisions
    solutions = []


    # finds all pairs of distinct elements that sum to a target, beginning at a start index in nums

    #two-pointer method to find pairs that sum to target, beggining at a spot in array, skipping duplicatesw
    def twoSumm2(target, start):
        print(target*-1)
        l = start
        r = len(nums) - 1
        for i in range(start, len(nums)-1):
            if nums[l]==nums[l-1]:
                l += 1
            elif r < len(nums) - 1 and nums[r] == nums[r+1]:
                r -= 1
            elif nums[l] + nums[r] == target:
                print(nums[start:])
                solutions.append([target*-1, nums[l], nums[r]])
                l += 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1

    # need to find pairs in rest of array, and make sure that no element is used twice. Additionally, solutions should be unique
    def twoSumm(target, start):
        hash = {}
        for i in range(start, len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = i
            complement = target - nums[i]           # calculate complement
            if complement in hash and hash[complement] != i:
                print(start,i, sep = ",")
                solutions.append([target*-1, nums[i], complement])
        # how to ensure unique sets of nums: 
    
        # for each element in the array, check for two numbers that sum to the complement in the hash map
    for i in range(0, len(nums)-2):
        if i>1 and nums[i] == nums[i-1]:
            continue
        else:
            twoSumm2(nums[i]*-1, i+1)
    
    return solutions
    
a_rray = [0,0,0,0]

print(threeSum(a_rray))
