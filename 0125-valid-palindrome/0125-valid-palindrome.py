class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        rev = s[::-1]
        if s == rev:
            return True
        else:
            return False