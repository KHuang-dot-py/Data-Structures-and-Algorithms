class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead. Constant memory
        """
        #intuition
            # we can think of each array as a long integer, each place representing digits in a decimal system
            # thus, we want to modify the order such that this "number" is larger
            # while minimizing how much larger
            # ex:   [1,2,3,4,5] -> [1,2,3,5,4],
            #       [2,1,4,3,5] -> [2,1,4,5,3]
            #       [4,5,3,2,1] -> [5,1,2,3,4]
        #approach in words
        #time complexity
        #space complexity
        