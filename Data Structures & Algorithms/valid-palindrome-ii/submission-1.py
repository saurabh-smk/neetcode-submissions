class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        start, end = 0, len(s)-1
        
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            
            else:
                left = is_palindrome(start+1, end)
                right = is_palindrome(start, end-1)
                return (left or right)
        return True

        