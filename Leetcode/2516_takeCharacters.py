class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        n = len(s)
        if n < k*3:
            return -1

        f = [0,0,0]
        offset = ord('a')
        for char in s:
            idx = ord(char) - offset
            f[idx] += 1 
        
        for count in f:
            if count < k: return -1

        l,r = 0,0
        max_window = 0

        for r in range(n):
            r_idx = ord(s[r]) - offset
            f[r_idx] -= 1

            while f[r_idx] < k:
                l_idx = ord(s[l]) - offset
                f[l_idx] += 1
                l += 1

            curr_window = r - l + 1
            max_window = max(max_window, curr_window)
        
        return n - max_window

tests = [
    ["aabaaaacaabc", 2, 8]
]

instance = Solution()


for t in tests:
    print(instance.takeCharacters(t[0], t[1]) == t[2])