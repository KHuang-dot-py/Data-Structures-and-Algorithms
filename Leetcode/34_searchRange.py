def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # binary search to find target and the range in which it was found
    # since any occurrences of the target must also be in that range. Otherwise, this would imply that ocurrences of the target
    # were present in both the left and right halves of the last step, which means that the target value would have been found.
    if len(nums) == 0:
        return [-1,-1]
    def binary_search2(arr, low, high, lookLeft = True):
        low = low
        high = high
        idx = -1
        while high >= low:
            mid = (high+low)//2
            # if mid is less than target look right
            if arr[mid] < target:
                low = mid+1
            # if mid is greater than target, look left
            elif arr[mid] > target:
                high = mid-1
            # if mid is equal to target
            else:
                idx = mid
                if lookLeft:
                    high = mid-1
                else:
                    low = mid+1
        return idx


    def binary_search(arr, low, high, target):
        if high >= low:
            mid = (high+low)//2
            if target == arr[mid]:
                return [mid, low, high]
            elif target < arr[mid]:
                return binary_search(arr, low, mid-1, target)
            else:
                return binary_search(arr, mid+1, high, target)
        else:
                return [-1,-1,-1]
    
    # find first ocurrence of target and returns the index
    def first_target(arr, low, high, target):
        if high >= low:
            mid = (high+low)//2
            # if mid is less than our target, search to right of mid
            if target > arr[mid]:
                return first_target(arr, mid+1, high, target)
            # termination when element to left of our target is less than target, and mid element equals target
            elif target == arr[mid] and (mid == low or arr[mid-1] < target):
                return mid
            # else search to left of mid
            else:
                return first_target(arr, low, mid-1, target)

        else:
                return -1
    #first last occurrence of target and returns the index
    def last_target(arr, low, high, target):
        if high >= low:
            mid = (high+low)//2
            # if mid is greater than our target, search to left of mid
            if target < arr[mid]:
                return last_target(arr, low, mid-1, target)
            # termination when element to right of our target is greater than target and mid element equals target
            elif target == arr[mid] and (mid == high or arr[mid+1] > target):
                return mid
            # else search to right of mid
            else:
                return last_target(arr, mid+1, high, target)

    (found, lower, upper) = binary_search(nums, 0, len(nums)-1, target)

    if found == -1:
        first,last = [-1,-1]
    else:
        #print(found, lower, upper, sep = ",")
        first = first_target(nums, lower, upper, target)
        #print(first)
        last = last_target(nums, lower, upper, target)
        # print(last)
    return [first,last]

a_rray = [0,1,2,3,4,5,6,7,8,9,9,9,9,9,14,15,16,17,18,19]
b_rray = [0,1,2,3,4]

print(searchRange(a_rray, 9))
