def maxSubarraySum(nums: list[int], k: int) -> int:
    # we can use sub-array sum helper, run it with all multiples of k
    # we could sum adjacent sub-arrays in a single pass as well?
    
    # nums will always be length of at least 1.
    # returns maximum sum of subarray of length l
    def subSum(A, l):
        current_sum = sum(A[:l])
        max_sum = current_sum
        for i in range(l, len(nums)):
            current_sum += A[i]
            current_sum -= A[i-l]
            max_sum = max(max_sum,current_sum)
        return max_sum
    
    global_max = float('-inf')
    for i in range (k, len(nums)+1, k):
        max_length_l = subSum(nums,i)
        global_max = max(global_max, max_length_l)
    return global_max

a_rray = [1,2,3,4,5,6,7,8,9]
my_k = 3

maxSubarraySum(nums = a_rray,k = 3)