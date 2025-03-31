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

a_rray = [-4, -1, -1, 0, 1, 2]

[-4, -1, -1, 0, 1, 2]



print(threeSum(a_rray))

# for i in range(0, len(a_rray)):
#     if i<len(a_rray)-1 and a_rray[i] == a_rray[i+1]:
#         continue
#     for j in range(i+1, len(a_rray)):
#         if j<len(a_rray)-1 and a_rray[j] == a_rray[j+1]:
#             continue
#         print(i,j)