def threeSum(nums):
    # sort the array
    nums = sorted(nums)
    solutions = []
    hash = {}
    for i in range(0, len(nums)):
        if nums[i] not in hash:
            hash[nums[i]] = [i]
        else:
            hash[nums[i]].append(i)
    
    # iterate through all unique pairs of array elements, then search the array to see if the complement exists
    for i in range(0, len(nums)-2):
        if i>0 and nums[i-1] == nums[i]:
            continue
        for j in range(i+1, len(nums)-1):
            if nums[j] == nums[j-1] and j!= i+1:
                continue
            complement = (nums[i] + nums[j])*-1
            if complement in hash:
                for k in hash[complement]:
                    if k>j:
                        solutions.append([nums[i],nums[j],complement])
                        break
            # how do i only check for a solution for the first of a length of repeats...
                        
            
    print(hash)
    return solutions

a_rray = [0,0,0,0]

[-4, -1, -1, 0, 1, 2]


def threeSum2ptr(nums):
    # sort the array
    nums = sorted(nums)
    solutions = []

    #for each element in the array, find pairs of elements in the remainder of the array that sum to the complement
    for i in range(len(nums)):
        # after first element in array, start skipping duplicates
        if i>0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1

        complement = nums[i]*-1

        while left<right:
            # solution found
            if nums[left]+nums[right] == complement:
                solutions.append([nums[i],nums[left],nums[right]])
                # find index of next non-duplicate element
                left += 1
                while nums[left] == nums[left-1] and left<right:
                    left += 1
            elif nums[left]+nums[right] < complement:
                left += 1
            else:
                right -= 1
    
    
    return solutions

    #ensure that duplicate elements are skipped after a solution is found.



print(threeSum2ptr(a_rray))

# for i in range(0, len(a_rray)):
#     if i<len(a_rray)-1 and a_rray[i] == a_rray[i+1]:
#         continue
#     for j in range(i+1, len(a_rray)):
#         if j<len(a_rray)-1 and a_rray[j] == a_rray[j+1]:
#             continue
#         print(i,j)