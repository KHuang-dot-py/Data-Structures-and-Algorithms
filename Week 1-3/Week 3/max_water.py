def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # area is calculated as:
    # depth = min(height[left], height[right])
    # length = right-left
    # area = depth*length

    max_area = 0
    
    # instead of comparing each pair and calculating area, let's start at the maximum possible length and seek larger pairs of heights
    if len(height)<2: return max_area #base case

    l = 0
    r = len(height)-1
    
    def calc_area(l, r):
        depth = min(height[l], height[r])
        length = r-l
        area = depth*length
        return area
    
    def find_next(i, increment):
        # increment left or right
        i += increment
        # until it is greater than the last value checked
        while height[i] <= height[i-increment] and 0 <= i < len(height):
            i += increment
        return i
        
    # while the two pointers have not yet met
    while l < r:
        max_area = max(calc_area(l,r), max_area)
        if height[l] < height[r]:
            l = find_next(l, 1)
        else:
            r = find_next(r, -1)

    return max_area

height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))
