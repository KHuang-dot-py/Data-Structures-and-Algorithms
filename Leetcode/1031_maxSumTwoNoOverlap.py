
def maxSumTwoNoOverlap(nums: list[int], firstLen: int, secondLen: int) -> int:
    #thinking
    # sum of len will never be greater than len of nums, and only dealing with positive integers
    # array is not sorted and cannot be sorted, so we need to try all valid combinations of non-overlapping sub-arrays
    # trying all combinations is O(n^2) worst-case
    # instead, go through array twice, to find subarrays of length firstLen and secondLen, storing their start and end indices, as well as sum

    #approach in words
    # 2 sliding windows, a leading and lagging
    # 1. let L be sub-array of length firstLen, let M be sub-array of length secondLen
    # 2. 2 cases: L comes after M or M comes after L
    #   a. first case: L after M
    #       we start with first valid combination of L after M, note the sum and end indices of L, M, as well as their sum
    #           keep track of largest sub-array M left of current L 'max_left'
    #       Then, shift L right, add it's sum to max_left and update global max if necessary
    #       Shift M right and update max_left if necessary
    #           
    #       
    # 3. Repeat above scenario with L before M
    # 4. take max of both scenarios, return the sum


    # in the constraints, nums is at least 2 in length, no need to account for length 0 or 1 case
    

    def findmax(lead_len,lag_len):
        lag_max = 0
        lag = lag_len-1
        lead = lag+lead_len
        #initial sub-array_sums:
        lag_sum = sum(nums[0:lag+1])
        lead_sum = sum(nums[lag+1:lead+1])
        # initial lag_max and GLOBAL_max
        lag_max = lag_sum
        GLOBAL_max = lead_sum + lag_max
        print(lead_sum, lag_sum, lag_max, GLOBAL_max, sep = ", ")            
        #initial maxes:
        while lead < len(nums)-1:
            lead += 1
            lag += 1
            lead_sum = lead_sum + nums [lead] - nums[lag]
            lag_sum = lag_sum + nums[lag] - nums[lag-lag_len]
            lag_max = max(lag_max, lag_sum)
            GLOBAL_max = max(GLOBAL_max, lag_max + lead_sum)
            # print(lead_sum, lag_sum, lag_max, GLOBAL_max, sep = ", ")
        return GLOBAL_max


            

    global_max = max(findmax(firstLen, secondLen), findmax(secondLen, firstLen))
    return global_max

    #time complexity
    # 2 O(n) passes of array nums per scenario, so O(n) overall
    #space complexity
    # O(1) space to store a constant number of sums

a_rray = [2,0,6,3,6,7]
first = 2
second = 3

print(maxSumTwoNoOverlap(a_rray,first,second))