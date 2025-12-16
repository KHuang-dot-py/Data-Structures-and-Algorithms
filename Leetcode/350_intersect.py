def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    #intuition
    # we should go through each array once, and store the values we find
    # as we go through, we should check whether that value is in the other array.
    # if so, we append it to our answer sheet, twice, and "consume" that instance of that number, so that the result array only has as many occurrences as appears in the one with less.

    #approach
    # let's create a hash map to store numbers and appearances of the first array
    # then, iterate through the second and if it appears in the hashmap, append to the solution array and "consume" that occurrence in the hasmap.

    #time complexity:
    # O(m) to create and insert into hashmap, O(n) traversal of second array
    # Total O(m+n)

    #space complexity
    # O(m), single hashmap and solution array
    f = {}
    intersect = []
    for x in nums1:
        if x in f:
            f[x] += 1
        else:
            f[x] = 1
    
    for y in nums2:
        if y not in f:
            continue
        if f[y] > 0:
            f[y] -= 1
            intersect.append(y)
        else:
            del f[y]
    
    return intersect

nums1 = [1,2,3,4,5,6,7,8,9]
nums2 = [1,3,5,7,9]
        
print(intersect(nums1,nums2))

# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
    # If the given array is already sorted, we can have 1 pointer for each array
    # we look for matching elements, and say it's sorted descending:
    # we increment the pointer of the array with a larger value untilL:
    #    it is equal (append to our answer array) or
    #    it is smaller (increment the other pointer)
    # this would be O(m + n) time but less space used O(1), since we are only storing pointers rather than a hashmap

# What if nums1's size is small compared to nums2's size? Which algorithm is better?
#   If num1 is smaller, then we should use num1 as the hashmap, and stop when it is empty.
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
#   hash partition join...
#   partition both tables by the same number ranges, then run the algorithm for each partition and append

