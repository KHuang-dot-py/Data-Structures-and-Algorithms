class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        # key:value = number:frequency
        freq = {}
        # returning xsums
        solutions = list()

        def calcXSum():
            # pairs of number/freq
            topk = sorted(freq.items(), key = lambda x: (-x[1],-x[0]))
            if x > len(topk):
                # print(sum(key*value for key, value in topk))
                return sum(key*value for key, value, in topk)
            else:
                # print(sum(key*value for key, value in topk[:x]))
                return sum(key*value for key, value in topk[:x])
       
        def addCount(num):
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            # print(freq, f"added 1 occurrence of {num}")
        
        def subCount(num):
            if num in freq:
                freq[num] -= 1
            # print(freq, f"removed 1 occurrence of {num}")


        #x-sum for nums[:k-1]
        for i in range(k):
            addCount(nums[i])
        solutions.append(calcXSum())
    
        #x-sum for all remaining subarrays of length k
        for i in range(n-k):
            subCount(nums[i])
            addCount(nums[i+k])
            solutions.append(calcXSum())
 
        return solutions

        