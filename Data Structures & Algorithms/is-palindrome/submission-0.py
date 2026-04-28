class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        s = s.lower()
        s = ''.join(i for i in s if i.isalnum())
        n = len(s)
        right = n-1
        a = ''
        b = ''
        while left<=n and right >=0:
            a = a+ s[left]
            left+=1
            b = b + s[right]
            right = right -1
        if a == b:
            return True
        else:
            return False
        