class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        n = len(s)
        # Iterate through each element in the array
        for i in range(n//2):
            j = n-1-i
            if s[i] != s[j]:
                    return False
        return True
        