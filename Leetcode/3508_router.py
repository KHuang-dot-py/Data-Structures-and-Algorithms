def binary_search_nearest(array, target, start, end):
    mid = (start + end)//2
    if array[mid] == target:
        print(mid)
        return mid
    # if base case is reached, return the nearest element
    elif start == end:
        return start
    elif array[mid] > target:
        return binary_search_nearest(array, target, start, mid-1)
    else:
        return binary_search_nearest(array, target, mid+1, end)


a_rray = [1,1,1,1,1]

found = binary_search_nearest(a_rray, 1, 0, len(a_rray)-1)
print(found)