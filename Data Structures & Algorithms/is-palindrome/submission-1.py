from string import punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = s.lower()
        # print(palindrome)
        x = "".join(palindrome.split())
        left, right = 0, len(x)-1
        # print(x)
        while left < right:
            if x[left] in punctuation:
                left += 1
            elif x[right] in punctuation:
                right -= 1
            elif x[left] == x[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        
         